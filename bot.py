import requests, time
from datetime import datetime
OB_LOW=86000
OB_HIGH=87250
BOS=85000
RISK=10
LEV=20
TOKEN="8749773045:AAF4F6k9SbbICNSelo7dA_AUuYQ92kwqRsQ"
CHAT="7133342437"
def tg(m):
    try: requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id":CHAT,"text":m}, timeout=10)
    except: pass
def get_price():
    r=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd", timeout=10).json()
    return float(r['bitcoin']['usd'])
tg(f"🚀 SMC Bot 24/7 LIVE!\nWatching OB {OB_LOW}-{OB_HIGH}")
while True:
  try:
    p=get_price()
    in_ob=p>=OB_LOW and p<=OB_HIGH
    print(f"{datetime.now()} BTC ${p} InOB:{in_ob}", flush=True)
    if in_ob:
        sl=OB_HIGH+400
        size=RISK/abs(p-sl) if p!=sl else 0
        rr=abs(p-BOS)/abs(p-sl) if p!=sl else 0
        tg(f"⚠️ BTC IN OB! ${p:.0f}\nOB {OB_LOW}-{OB_HIGH}\nSL ${sl:.0f}\nSize {size:.4f} BTC\nRR 1:{rr:.1f}\nCheck 4h wick then SHORT!")
        time.sleep(3600)
  except Exception as e: print(e, flush=True)
  time.sleep(60)
  
