import threading, os
from flask import Flask
import requests, time
from datetime import datetime

app = Flask(__name__)
@app.route('/')
def home():
    return "SMC Bot Running 24/7"
def run_web():
    app.run(host='0.0.0.0', port=10000)
threading.Thread(target=run_web, daemon=True).start()

OB_LOW=86000
OB_HIGH=87250
BOS=85000
RISK=10
LEV=20
TOKEN=os.environ.get("TOKEN", "8749773045:AAF4F6k9SbbICNSelo7dAyB1")
CHAT=os.environ.get("CHAT", "7133342437")

def tg(m):
    try: requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id":CHAT,"text":m})
    except: pass

def get_price():
    r=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
    return float(r['bitcoin']['usd'])

tg(f"🚀 SMC Bot 24/7 LIVE!\nWatching OB {OB_LOW}-{OB_HIGH}")

while True:
    try:
        p=get_price()
        print(f"{datetime.now()} BTC {p}")
        if p>=OB_LOW and p<=OB_HIGH:
            tg(f"⚠️ BTC in OB zone: {p}")
        time.sleep(30)
    except Exception as e:
        print(e)
        time.sleep(30)
