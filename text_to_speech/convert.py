import main
import asyncio
from pypdf import PdfReader
import boto3
from dotenv import load_dotenv


load_dotenv()

polly = boto3.client('polly')

async def pdf_to_text():
    file_content = await main.upload_file()
    reader = PdfReader(file_content)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + " "

    return full_text


def synthesize_pdf_text(text):
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Joanna"
    )

    if "AudioStream" in response:
        with open('speech.mp3', 'wb') as file:
            file.write(response["AudioStream"].read())

        print("Speech successfully saved to speech.mp3")

pdf_content = pdf_to_text()
synthesize_pdf_text(pdf_content)