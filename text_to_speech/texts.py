import requests

files = {
    "file": open("Ocean_Facts.pdf", "rb")
}
response = requests.post("http://localhost:8000/upload", files=files)
print(response.json())
