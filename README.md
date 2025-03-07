Here’s an updated **cool and visually appealing README** for your Flask-based AI-powered call system with symbols to make it stand out! You can directly copy and paste this:

---

# 📞 **AI-Powered Interactive Call System**

🚀 This Flask application is an **AI-powered interactive call system** that integrates with **Twilio** and **ElevenLabs** to handle both inbound and outbound calls. It dynamically interacts with users, answers their queries, supports multiple Indian languages, and provides real-time responses with conversational calming techniques.

---

## ✨ **Features**

✅ **AI-Powered Outbound Calls**  
   - 🗣️ Calls are made with a **natural Indian accent** using **ElevenLabs**.  
   - 🎧 Simulates **background noise** for added realism.  
   - 🤖 Conversations are indistinguishable from human agents.

✅ **Interactive Conversational AI**  
   - 💬 Borrowers can ask real-time questions about:  
     - Outstanding dues and penalties.  
     - Due dates and repayment options.  
   - 🛑 Handles aggressive borrowers using **calming techniques**.  
   - 📩 Sends an SMS with a payment link upon agreement to pay.

✅ **Multi-Language Support**  
   - 🌐 Supports **Hindi**, **Marathi**, **Punjabi**, **Tamil**, **Telugu**, and other Indian languages.  
   - 🗺️ Uses dialect-aware NLP models for accurate communication.

✅ **Encryption for Security**  
   - 🔒 Borrower data is securely encrypted using the `cryptography` library.

✅ **Real-Time Speech Recognition (STT)**  
   - 🎙️ Uses Google Speech-to-Text API to transcribe user responses during calls.

✅ **Dynamic Query Handling**  
   - 🤔 Responds dynamically to borrower queries such as loan amount, EMI details, interest rate, etc.

✅ **Twilio Integration**  
   - 📞 Handles both inbound and outbound calls using Twilio's programmable voice features.

---

## 🛠️ **Setup Instructions**

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo-name/flask-ai-call-system.git
cd flask-ai-call-system
```

### 2️⃣ Install Dependencies
Create a virtual environment and install the required libraries:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file in the project directory and add the following credentials:
```plaintext
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number

ELEVENLABS_API_KEY=your_elevenlabs_api_key
VOICE_ID=your_voice_id

GOOGLE_APPLICATION_CREDENTIALS=path_to_google_credentials.json
```

### 4️⃣ Borrower Data File
Ensure you have a file named `borrower-input.txt` in the project directory containing borrower details in JSON format.

Example `borrower-input.txt`:
```json
{
    "Name": "John Doe",
    "Phone": "+9876543210",
    "amount_overdue": "60000",
    "emi_due_date": "2025-01-01",
    "loan_amount": "1000000",
    "loan_tenure": "24",
    "interest_rate": "12",
    "monthly_emi": "5000"
}
```

---

## 🚀 **How to Run**

### 1️⃣ Start the Flask App
Run the Flask server:
```bash
python app.py
```

The application will be accessible at `http://127.0.0.1:5000`.

### 2️⃣ Expose Local Server (For Testing)
Use `ngrok` to expose your local server to the internet so Twilio can access it:
```bash
ngrok http 5000
```
Copy the public URL provided by ngrok and use it in your Twilio webhook settings.

### 3️⃣ Configure Twilio Webhooks
- Go to your Twilio Console > Phone Numbers > Manage Numbers > Active Numbers.
- Set the webhook for incoming calls to `http:///handle_call`.

---

## 🔗 **Endpoints**

### `/handle_call`
Handles incoming calls by greeting the user and recording their query for processing.

### `/handle_recording`
Processes user queries by transcribing speech using Google Speech-to-Text API and responding dynamically based on borrower data.

### `/make_call`
Initiates an outbound call to a borrower with a custom message.

Request Body Example (JSON):
```json
{
    "name": "John Doe",
    "phone": "+9876543210"
}
```

---

## 🌟 **Features in Detail**

1. 🗣️ **AI-Powered Outbound Calls**:  
   Uses ElevenLabs for generating realistic speech with an Indian accent. Simulates background noise for added realism during calls.

2. 💬 **Interactive Conversational AI**:  
   Dynamically responds to borrower queries such as outstanding dues, EMI due dates, repayment options, penalties, loan amount, tenure, interest rate, etc. Handles aggressive tones using calming techniques like empathetic responses.

3. 📩 **SMS Payment Link**:  
   Sends an SMS with a payment link upon agreement to pay using Twilio's messaging API.

4. 🌐 **Multi-Language Support**:  
   Supports multiple Indian languages (Hindi, Marathi, Punjabi, Tamil, Telugu) using dialect-aware NLP models powered by SpeechT5.

5. 🔒 **Encryption for Security**:  
   Borrower data is securely encrypted using the `cryptography` library.

---

## 📊 Example Interaction

1️⃣ User calls the system or receives an outbound call.  
2️⃣ The bot greets the user:  
   *"Hello! This is a call from the loan department. How can we assist you today?"*  

3️⃣ User asks: *"What are my outstanding dues?"*  
4️⃣ Bot responds:  
   *"Your outstanding dues are 60000."*  

5️⃣ User agrees to pay: *"I would like to make the payment."*  
6️⃣ Bot sends an SMS with a payment link:  
   *"Please make your payment using this link: https://example.com/payment."*

---

## 🛠️ Dependencies

Install all required libraries using pip:
```bash
pip install flask cryptography twilio requests transformers SpeechRecognition google-cloud-speech soundfile sentencepiece numpy
```

---

## 🚀 Future Enhancements

📌 Add support for more regional languages and dialects.  
📌 Integrate advanced NLP models for better query understanding.  
📌 Enable voice modulation for more human-like interactions.

---

## 🙌 Credits

- 💻 [Twilio](https://www.twilio.com/) for programmable voice APIs.
- 🎙️ [ElevenLabs](https://elevenlabs.io/) for text-to-speech capabilities.
- ☁️ [Google Cloud](https://cloud.google.com/) for Speech-to-Text API integration.

---

🔥 This README is designed to provide everything you need to set up and run your Flask-based AI-powered call system while showcasing its cool features in style! Copy-paste it directly into your project! 😎
