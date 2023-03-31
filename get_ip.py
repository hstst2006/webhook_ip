#! /usr/bin/env python

from time import sleep

import socket
import requests
import json
from datetime import datetime

# Set socket to do connections using UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

attempts = 0

webhook = "YOUR WEBHOOK HERE"

while(attempts < 300):
    try:
        s.connect(("8.8.8.8", 1))
    except:
        pass
    #Read the socket's own address, if there is no address sleep and loop again
    #Else POST ip to webhook
    my_IP = s.getsockname()[0]
    if str(my_IP) != "0.0.0.0":
        current_time = datetime.now()
        formatted_time = current_time.strftime("%d/%m/%Y %H:%M")
        payload = {"content": f"({formatted_time}) Raspberry pi online!\n{my_IP}"}
        request = requests.post(webhook, data=json.dumps(payload), headers={"Content-type" : "application/json"})
        break
    else:
        attempts += 1
        sleep(1)
