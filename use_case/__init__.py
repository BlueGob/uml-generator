import requests

def use_case(code:str,type:str)->str:
    url = f"http://localhost:8080/{type}/{code}"
    headers = {
        "accept": "image/avif,image/webp,*/*",
        }
    response = requests.get(url, headers=headers)
    return response.content