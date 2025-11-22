import requests

files = {"file": open("colorful_img.jpg", "rb")}

response = requests.post("http://localhost:8000/upload-image", files=files)

if response.status_code == 200:
    print(f"The most common colors are {response.content}")
else:
    print(f"Sorry your request failed. Error {response.status_code}")