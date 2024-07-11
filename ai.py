import os
from openai import AzureOpenAI



client = AzureOpenAI(
  api_key = "",
  api_version = "2024-02-01",
  azure_endpoint = ""
)


def generate_response(conversation_text):
    response = client.chat.completions.create(
        model="gpt-4",  # Adjust if using a specific deployment name.
        messages=[
            {"role": "system", "content": "You are an AI trained as a cybersecurity expert. Your task is to analyze network scan results and recommend further detailed scans if necessary. Based on the scan results, decide whether a service scan or an operating system scan should be conducted next.Start your recommendation with the keyword 'Recommendation:' followed by the type of scan. if no further scans are required do not use the recomendation key word, just provide a conclusive response on the situation, you have an initial scan that gives you the first response , then a service scan for the services and an os scan for the os "},
            
            {"role": "user", "content": conversation_text}
        ]
    )
    return response.choices[0].message.content