from wifi_functions import (get_wifi_name,
                            ping_wifi_by_name)

def main():
    wifi_name = get_wifi_name()
    ping_wifi_by_name(wifi_name)

if __name__ == '__main__':
    main()

