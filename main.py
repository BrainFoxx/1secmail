import json
import requests
import random
import time
domain = 'esiix.com' # For e.g

def onesec():
    for _ in range(5):
        sec = ""
    for _ in range(5):
        sec += random.choice("qwertyuiopasdfghjklzxcvbnm")
    print(sec + f"@{domain}")
    while True:
        r = requests.get(
            f"https://www.1secmail.com/api/v1/?action=getMessages&login={sec}&domain={domain}"
        ).text
        if r == "[]":
            time.sleep(5)
        else:
            break
    try:
        json_data = json.loads(r)
        re = requests.get(
            f"https://www.1secmail.com/api/v1/?action=readMessage&login={sec}&domain={domain}&id={json_data[0]['id']}"
        ).text
        print(
            f"Subject:{json_data[0]['subject']}\nFrom:{json_data[0]['from']}\nID : {json_data[0]['id']}\nMessage : {json.loads(re)['textBody']}"
        )
    except:
        print("ERROR")


if __name__ == "__main__":
    onesec()
