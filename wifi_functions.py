import subprocess
from datetime import datetime

def get_wifi_name():
    command=("networksetup -listallhardwareports"
            +"| awk '/Wi-Fi/{getline; print $2}'"
            +"| xargs networksetup -getairportnetwork")

    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    wifi_name = result.stdout.strip("Current Wi-Fi Network:").strip()
    return wifi_name

def ping_wifi_by_name(wifi_name: str):
    print(f"{datetime.now().replace(microsecond=0)}")
    if wifi_name != 'You are not associated with an AirPort network.':
        print("*"*100)
        print(f"Name of the current wifi network: {wifi_name}")
        print(f"Checking internet connection to 8.8.8.8")
        print("*"*100)
        ping_local_cmd = 'ping -a -c 5 8.8.8.8'
        ping_local_result = subprocess.run(
            ping_local_cmd,
            shell=True,
            capture_output=True,
            text=True,
        )
        print(f"ping_local_result:\n{ping_local_result}")
        splitted_newline_result = ping_local_result.stdout.split("\n")
        print(f"splitted_newline_result:\n{splitted_newline_result}")

        for n in splitted_newline_result:
            print(f"current newline:{n}")



        print("*"*100)
        print(f"Checking internet connection to google.com")
        ping_google_cmd = 'ping -a -c 5 8.8.8.8'
        subprocess.run(
            ping_google_cmd,
            shell=True,
            # capture_output=True,
            # text=True,
        )
        print("*"*100)
    else:
        print("you are not connected to either of known wifi now")

