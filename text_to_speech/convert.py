import io
from pypdf import PdfReader
from dotenv import load_dotenv
import boto3

load_dotenv()

polly = boto3.client('polly')

def extract_pdf_from_bytes(pdf_bytes):
    pdf_content = io.BytesIO(pdf_bytes)
    reader = PdfReader(pdf_content)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + " "

    return full_text


def synthesize_text_to_audio(text):
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Joanna"
    )

    if "AudioStream" in response:
        return response["AudioStream"].read()
    return None
