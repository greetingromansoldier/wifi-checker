import subprocess
import os

def get_wifi_name():
    command=("networksetup -listallhardwareports"
            +"| awk '/Wi-Fi/{getline; print $2}'"
            +"| xargs networksetup -getairportnetwork")

    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    wifi_name = result.stdout.strip("Current Wi-Fi Network:").strip()
    return wifi_name

def ping_wifi_by_name(wifi_name: str):
    if wifi_name != 'You are not associated with an AirPort network.':
        print("*"*100)
        print(f"Name of the current wifi network: {wifi_name}")
        print(f"Checking internet connection to 8.8.8.8")
        print("*"*100)
        os.system(command='ping -a -c 5 8.8.8.8')
        print("*"*100)
        print(f"Checking internet connection to google.com")
        os.system(command='ping -a -c 5 google.com')
        print("*"*100)
    else:
        print("you are not connected to either of known wifi now")

