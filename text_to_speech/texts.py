import requests

files = {
    "file": open("Ocean_Facts.pdf", "rb")
}
response = requests.post("http://localhost:8000/upload", files=files)


if response.status_code == 200:
    with open("output_audio.mp3", "wb") as audio_file:
        audio_file.write(response.content)
    print("Success Audio saved to output_audio.mp3")
else:
    print(f"Error: {response.status_code}")
    print(response.text)