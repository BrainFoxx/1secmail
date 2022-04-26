import json
import requests
import random
import time


def onesec():
    for _ in range(5):
        sec = ""
    for _ in range(5):
        sec += random.choice("qwertyuiopasdfghjklzxcvbnm")
    print(sec + "@yoggm.com")
    for _ in range(10):
        r = requests.get(
            f"https://www.1secmail.com/api/v1/?action=getMessages&login={sec}&domain=yoggm.com"
        ).text
        if r == "[]":
            time.sleep(5)
        else:
            break
    try:
        json_data = json.loads(r)
        re = requests.get(
            f"https://www.1secmail.com/api/v1/?action=readMessage&login={sec}&domain=yoggm.com&id={json_data[0]['id']}"
        ).text
        print(
            f"""Тема:{json_data[0]['subject']}\nОт:{json_data[0]['from']}\nID : {json_data[0]['id']}\nСообщение : {json.loads(re)['textBody']}"""
        )
    except:
        print("ERROR")


if __name__ == "__main__":
    onesec()
