import os

import requests

# Define file paths and names
file_path = "Input/merged.pdf"
file_name_gcloud = "output.wav"

OPEN_AI_URL = "https://api.openai.com/v1/chat/completions"
OPEN_AI_KEY = os.environ.get("OPENAI_KEY")
public_key = os.environ.get("ILOVEPDF_KEY")

# PDF extraction using ilovepdf API
with open(file_path, "rb") as pdf_file:
    # Authenticate and get token from ilovepdf
    token = requests.post("https://api.ilovepdf.com/v1/auth", json={"public_key": public_key}).json()['token']
    header = {"Authorization": f"Bearer {token}"}

    # Start PDF extraction task
    start = requests.get("https://api.ilovepdf.com/v1/start/extract", headers=header).json()
    assigned_server = start['server']
    task_nr = start['task']

    # Upload PDF file
    upload = requests.post(f"https://{assigned_server}/v1/upload", headers=header, data={'task': task_nr},
                           files={"file": pdf_file}).json()
    server_file_name = upload['server_filename']

    # Process PDF extraction
    process = requests.post(f"https://{assigned_server}/v1/process", headers=header,
                            json={"task": task_nr, "tool": "extract",
                                  "files": [
                                      {"server_filename": server_file_name, "filename": file_path.split("/")[-1]}]})

    # Download processed file
    download = requests.get(f"https://{assigned_server}/v1/download/{task_nr}", headers=header)

    # Check if download is successful
    if download.status_code == 200:
        file_content = download.content
        with open('Output/processed_file.txt', 'wb') as f:
            f.write(file_content)
    else:
        print(download.json())

# Read extracted text from processed file
with open("Output/processed_file.txt", "r", encoding='utf-16') as f:
    all_text = f.read()

headers_open_ai = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPEN_AI_KEY}"
}
input_to_open_ai = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant. You will get a presentaion tranformed to a text that you will have to make notes from, so it looks nice and readable in appliction Evernote, that stores notes from lessons."
        },
        {
            "role": "user",
            "content": all_text
        }
    ]
}
response = requests.post(OPEN_AI_URL, headers=headers_open_ai, json=input_to_open_ai).json()

with open(f"Output/output.txt", "w") as f:
    f.write(response["choices"][0]["message"]["content"])
