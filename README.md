# Webhook script
This python script attempts to obtain the local IP-address of the device and then post the current date and message together with the IP to a webhook.

## Why?
My Raspberry Pi is not connected to a screen or keyboard, and has a dynamic IP address on my home network. 
I use this script to post the IP of the device to a webhook in case the IP changes.

## What it does
It obtains the local IP-address by attempting to connect to an arbitrary IP address, and then obtains the local IP of the device once it has established network connection. The script attempts a new connection every second for at most 5 minutes, or until it obtains a connection.

## Running the script on boot
I have run into issues using scripts in /etc/network/if-up.d/ and have therefore opted to run this script with crontab

```bash
# Edit crontab
crontab -e

# In crontab
# Run this script every time the system boots
@reboot python <script location>
```
