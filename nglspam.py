import requests
import random
from itertools import cycle

def send_post_spam(username, message, proxy):
    url = 'https://ngl.link/api/submit'
    payload = {'username': username, 'question': message, 'deviceId': ""}
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, json=payload, headers=headers, proxies=proxy)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def read_proxies_from_file(filename):
    with open(filename, 'r') as file:
        proxies = [{'http': line.strip()} for line in file.readlines()]
        return proxies

def main():
    banner_text = """
========[NGL SPAMMER]========
=============================
█▄░█ █▀▀ █░░ █▀ █▀█ ▄▀█ █▀▄▀█
█░▀█ █▄█ █▄▄ ▄█ █▀▀ █▀█ █░▀░█
=============================
[+] Made By: @Heru_Dev
[+] Github: LyxnDev
[+] Facebook: Jay mar
=============================
    """
    banner = f"\033[91m{banner_text}\033[0m"
    print(banner)
    username = input("\033[94m[</>]-username: \033[0m")
    message = input("\033[94m[</>] message: \033[0m")
    amount = int(input("\033[94m[</>] amount: \033[0m"))
    
    proxy_file = "proxy.txt"
    proxies = read_proxies_from_file(proxy_file)

    proxy_pool = cycle(proxies)
    success_count = 0
    for i in range(amount):
        proxy = next(proxy_pool)
        status_code = send_post_spam(username, message, proxy)
        if status_code == 200:
            success_count += 1
            colored_message = f"\033[93m[{success_count}][Success]: [💀]-Message sent to target: {username}\033[0m"
            print(colored_message)
if __name__ == "__main__":
    main()
    
