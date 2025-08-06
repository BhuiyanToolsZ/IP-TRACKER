import requests
import os
import time

# Color codes
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[0m'
BOLD    = '\033[1m'

def clear_screen():
    os.system("clear")

def banner():
    print(rf"""
{YELLOW}
   _______    _________  ___  _______ _________ 
  /  _/ _ \  /_  __/ _ \/ _ |/ ___/ //_/ __/ _ \\
 _/ // ___/   / / / , _/ __ / /__/ ,< / _// , _/
/___/_/      /_/ /_/|_/_/ |_\___/_/|_/___/_/|_| 
                                                
                                                V1.0
{RED}
---------------------------------------{MAGENTA}
AUTHOR   :{YELLOW} BhuiyanToolz {MAGENTA}
GITHUB   :{YELLOW} github.com/BhuiyanToolz {MAGENTA}
FACEBOOK :{YELLOW} Yeasin Bhuiyan {RED}
---------------------------------------
{RESET}
""")

def track_ip(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        res = requests.get(url).json()

        if res['status'] == 'success':
            print(f"\n{GREEN}[✓] IP Information Found:{RESET}\n")
            print(f"{YELLOW}IP          : {RESET}{res['query']}")
            print(f"{YELLOW}Country     : {RESET}{res['country']}")
            print(f"{YELLOW}Region      : {RESET}{res['regionName']}")
            print(f"{YELLOW}City        : {RESET}{res['city']}")
            print(f"{YELLOW}Time Zone   : {RESET}{res['timezone']}")
            print(f"{YELLOW}AS          : {RESET}{res['as']}")
            print(f"{YELLOW}ISP         : {RESET}{res['isp']}")
            print(f"{YELLOW}Org         : {RESET}{res['org']}")
            print(f"{YELLOW}ZIP         : {RESET}{res['zip']}")
            print(f"{YELLOW}Lat         : {RESET}{res['lat']}")
            print(f"{YELLOW}Lon         : {RESET}{res['lon']}")
            
            print(f"\n\n{YELLOW}Google Maps : {BLUE}https://www.google.com/maps/search/?api=1&query={res['lat']},{res['lon']}{RESET}\n")
        else:
            print(f"{RED}[✘] Failed to fetch data for this IP!{RESET}\n")
    except Exception as e:
        print(f"{RED}[!] Error: {e}{RESET}\n")

def my_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
        print(f"{GREEN}[✓] Your Public IP Address is: {RESET}{ip}")
        track_ip(ip)
    except Exception as e:
        print(f"{RED}[!] Error: {e}{RESET}\n")

def back_or_exit():
    while True:
        choice = input(f"{CYAN}Back to Menu (M) or Exit (E)? : {RESET}").strip().lower()
        if choice == 'm':
            return True  # back to menu
        elif choice == 'e':
            print(f"{RED}Exiting...{RESET}")
            exit()
        else:
            print(f"{RED}Invalid input! Please enter M or E.{RESET}")

def menu():
    while True:
        clear_screen()
        banner()
        print(f"""{YELLOW} 
[1]{RED}   >> {RESET}IP TRACK {YELLOW}
[2]{RED}   >> {RESET}MY IP TRACK   {YELLOW}
[3]{RED}   >> {RESET}EXIT           
{RESET}""")

        op = input(f"{GREEN}[+] Enter Your Option: {RESET}")

        if op == "1":
            print(f"{YELLOW}🔍 IP TRACK selected...{RESET}")
            ip = input(f"{CYAN}[?] Enter IP Address: {RESET}")
            track_ip(ip)
            if not back_or_exit():
                break
        elif op == "2":
            print(f"{YELLOW}🌐 MY IP TRACK selected...{RESET}")
            my_ip()
            if not back_or_exit():
                break
        elif op == "3":
            print(f"{RED}Exiting...{RESET}")
            exit()
        else:
            print(f"{RED}Invalid option! Try again.{RESET}")

if __name__ == "__main__":
    menu()