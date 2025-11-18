import requests

files = {
    "file": open("", "rb")
}
response = requests.post("http://localhost:8000/upload", files=files)
print(response.json())
