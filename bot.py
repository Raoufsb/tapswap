import json
import requests
import os

TOKEN = "7065378380:AAHOpNIoEtFe7Q_iHaOiuf9UKISX5zMwMFA"
CHAT_ID = "6847136391"
DATA_FILE = "query.txt"
SENT_IDS_FILE = "ids.json"

def send_texts_from_file():
    sent_ids = set()

    if os.path.exists(SENT_IDS_FILE):
        with open(SENT_IDS_FILE, "r") as file:
            sent_ids = set(json.load(file))

    with open(DATA_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line and line not in sent_ids:
                send_message(chat_id=CHAT_ID, text=line)
                sent_ids.add(line)

    with open(SENT_IDS_FILE, "w") as file:
        json.dump(list(sent_ids), file)

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

send_texts_from_file()
