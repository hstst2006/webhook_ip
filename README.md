# Webhook script
This python script attempts to obtain the local IP-address of the device and then post the current date and message together with the IP to a webhook.

It obtains the local IP-address by attempting to connect to an arbitrary IP address, and then obtaining the IP of the local interface once it has established network connection. The script attempts a new connection every second for 5 minutes, so it can be used with crontab even before the networks are up.

My Raspberry Pi is not connected to a screen or keyboard, and has a dynamic IP address on my home network. 
I use this script to post the IP of the device to a Discord webhook in case the IP changes.
