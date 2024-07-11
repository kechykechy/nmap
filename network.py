import nmap
from ai import generate_response  # Ensure this is properly imported

def initial_scan(ip_address):
    print("Performing initial scan to identify open and filtered ports...")
    return perform_scan('', ip_address, 'Initial scan')  # No arguments for a basic port scan

def service_scan(ip_address):
    print("Performing service scan to identify services on open/filtered ports...")
    return perform_scan('-sV', ip_address, 'Service scan')  # Service scan

def os_scan(ip_address):
    print("Performing OS scan to identify operating systems of the devices...")
    return perform_scan('-O', ip_address, 'OS scan')  # OS detection scan

def perform_scan(arguments, ip_address, scan_description):
    nm = nmap.PortScanner()
    nm.scan(ip_address, arguments=arguments)
    return format_scan_results(nm, arguments, scan_description)  # Pass arguments to format_scan_results

def format_scan_results(nm, arguments, scan_description):  # Include arguments in the parameter list
    output = f"{scan_description} results:\n"
    for host in nm.all_hosts():
        output += f'Host: {host} ({nm[host].hostname()}) State: {nm[host].state()}\n'
        for proto in nm[host].all_protocols():
            output += f'----------\nProtocol: {proto}\n'
            for port in sorted(nm[host][proto].keys()):
                service = nm[host][proto][port]
                output += f'Port: {port} State: {service["state"]}'
                if '-sV' in arguments or '-O' in arguments:  # Append service details for service or OS scans
                    output += f' Service: {service.get("name", "n/a")}'
                output += '\n'
    print(output)
    return output

def main_scan_logic(ip_address):
    scan_results = initial_scan(ip_address)
    ai_response = generate_response(scan_results)
    print("AI's Explanation:", ai_response)

    if 'service scan' in ai_response.lower():
        scan_results = service_scan(ip_address)
        ai_response = generate_response(scan_results)
        print("AI's Explanation:", ai_response)

    if 'os scan' in ai_response.lower():
        scan_results = os_scan(ip_address)
        ai_response = generate_response(scan_results)
        print("AI's Explanation:", ai_response)

if __name__ == "__main__":
    ip_address = '192.168.1.1'  # Replace with the target IP
    main_scan_logic(ip_address)
