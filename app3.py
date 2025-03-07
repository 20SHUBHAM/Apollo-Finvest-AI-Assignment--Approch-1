from flask import Flask, request, jsonify
from twilio.twiml.voice_response import VoiceResponse, Gather
from cryptography.fernet import Fernet
import json
import requests

app = Flask(__name__)

# Encryption setup
from cryptography.fernet import Fernet
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

# Twilio credentials (replace with your credentials)
TWILIO_ACCOUNT_SID = 'AC2720ac7f9b1bebd5ced54754f8bcca74'
TWILIO_AUTH_TOKEN = '4254d7e51a1519099f4324a50bba4d6c'
TWILIO_PHONE_NUMBER = '+18144585212'

# ElevenLabs credentials (replace with your API key & voice ID)
ELEVENLABS_API_KEY = 'sk_23bb92a1648d7fd6a6d975437bf05183191950f8868e3da1'
VOICE_ID = 'MF4J4IDTRo0AxOO4dpFR'

# Load borrower data securely from file and encrypt it
with open('borrower input1.txt', 'r') as file:
    borrower_data = json.load(file)

encrypted_borrower_data = {key: cipher_suite.encrypt(str(value).encode()).decode() for key, value in borrower_data.items()}

def decrypt_borrower_data():
    return {key: cipher_suite.decrypt(value.encode()).decode() for key, value in encrypted_borrower_data.items()}

# Function to respond dynamically to borrower queries
def respond_to_query(query, borrower):
    query = query.lower()
    responses = {
        "outstanding dues": f"Your outstanding dues are {borrower_data['amount_overdue']} rupees.",
        "due date": f"Your EMI due date is {borrower_data['emi_due_date']}.",
        "repayment options": "You can repay via bank transfer or online payment portals.",
        "penalties": "Late payment penalties apply as per your loan agreement.",
        "loan amount": f"Your loan amount is {borrower_data['loan_amount']} rupees.",
        "loan tenure": f"Your loan tenure is {borrower_data['loan_tenure']} months.",
        "interest rate": f"Your interest rate is {borrower_data['interest_rate']} percent.",
        "monthly emi": f"Your monthly EMI is {borrower_data['monthly_emi']} rupees."
    }
    for key in encrypted_borrower_data:
        if key.lower() in query.lower():
            return encrypted_borrower_data[key]
    return "Sorry, I didn't understand your question clearly."

# Endpoint to initiate outbound call via Twilio API
@app.route('/initiate_call', methods=['POST'])
def initiate_call():
    from twilio.rest import Client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    phone_number = request.json.get('phone_number')

    call = client.calls.create(
        to=phone_number,
        from_=TWILIO_PHONE_NUMBER,
        url='http://127.0.0.1:5000/voice'  # Replace with your public URL or ngrok URL
    )
    return jsonify({"status": "success", "call_sid": call.sid})

# Endpoint handling the call interaction (Twilio webhook)
@app.route('/voice', methods=['POST'])
def voice():
    response = VoiceResponse()
    response.say("Hello! This is an automated call from the loan department. Please say your query after the beep.")
    response_url = '/process_query'
    response_url_full = request.url_root[:-1] + response_url  # full URL for callback

    response = VoiceResponse()
    response.record(
        action=response_url_full,
        method='POST',
        max_length=10,
        play_beep=True,
        timeout=3,
        transcribe=True,
        transcribe_callback=response_url_full,
    )
    return str(response)

@app.route('/process_query', methods=['POST'])
def process_query():
    recording_url = request.form.get('RecordingUrl')

    # Transcribe audio using Google's Speech-to-Text API via SpeechRecognition library
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    audio_file_url = recording_url + ".wav"

    audio_response = requests.get(audio_file_url)
    with open("user_query.wav", "wb") as f:
        f.write(audio_response.content)

    with sr.AudioFile("user_query.wav") as source:
        audio_data = recognizer.record(source)
        try:
            user_query_text = recognizer.recognize_google(audio_data=audio_data)
            print(f"User said: {user_query}")
            response_text = respond_to_query(user_query)
        except Exception as e:
            response_text = "Sorry, I couldn't understand you clearly. Please contact our support."

    # Generate realistic Indian accent audio using ElevenLabs API
    elevenlabs_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers_elevenlabs = {
      "xi-api-key": ELEVENLABS_API_KEY,
      "Content-Type": "application/json"
    }
    
    data_elevenlabs = {
      "text": response_text,
      "voice_settings": {"stability": 0.7,"similarity_boost":0.8}
    }

    elevenlabs_response = requests.post(elevenlabs_url, headers=headers_elevenlabs, json=data)

    with open("response_audio.mp3", "wb") as audio_f:
      audio_f.write(elevenlabs_response.content)

    # Upload this file to public storage and replace below URL accordingly.
    audio_public_url="https://your-audio-storage.com/response_audio.mp3"
    
    final_response=VoiceResponse()
    
    # Background noise simulation (call-center environment realism) can be pre-mixed into audio file before uploading.
    
    final_response=VoiceResponse()
    final_audio_with_noise=audio_public_url  # Audio includes background noise mixed manually or via editing tools.

    final_twiml=VoiceResponse()
    final_twiml.play(final_audio_public_url)
    
    return str(final_twiml)

if __name__ == "__main__":
  app.run(debug=True)
