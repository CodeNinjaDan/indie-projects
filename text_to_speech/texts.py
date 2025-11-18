import requests

files = {
    "file": open("The-Metamorphosis-Franz-Kafka.pdf", "rb")
}
response = requests.post("http://localhost:8000/upload", files=files)
print(response.json())
