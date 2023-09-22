import requests

def coder(text:str)->str:
    url = "http://localhost:8080/coder"
    headers = {
        "Content-Type": "text/plain",
        "accept": "*/*",
        }
    response = requests.post(url, headers=headers, data=text)
    return response.text
