import requests
import time
import pycenter
import colorama
import os
from colorama import init, Fore
from requests import delete
from requests.api import request
from pycenter import center
init(autoreset=True)
os.system("cls && title 𝙒𝙚𝙗𝙝𝙤𝙤𝙠 𝙏𝙤𝙤𝙡")
logo = """
 _    _      _     _                 _      _____           _ 
| |  | |    | |   | |               | |    |_   _|         | |
| |  | | ___| |__ | |__   ___   ___ | | __   | | ___   ___ | |
| |/\| |/ _ \ '_ \| '_ \ / _ \ / _ \| |/ /   | |/ _ \ / _ \| |
\  /\  /  __/ |_) | | | | (_) | (_) |   <    | | (_) | (_) | |
 \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\   \_/\___/ \___/|_|
"""
print(center(logo))
url = input(center("\n[>>] \n"))
r = requests.get(url)
os.system("cls")
print(center(logo))
response = f'The status code: {Fore.RED}{r}.'
print(center(response))
print(center("\nInformations : "))
name = requests.get(url).json()['name']
avatar = requests.get(url).json()['avatar']
token = requests.get(url).json()['token']
print(center (f'Name: {Fore.RED}{name}\n{Fore.WHITE}Avatar: {Fore.RED}{avatar}\n{Fore.WHITE}Token: {Fore.RED}{token}'))
delete = input(center('Does I delete webhook ? (y/n): '))
if delete == "y":
    requests.delete(url)
    os.system("cls")
    print(center(logo))
    print(center(f'{Fore.GREEN}\n[DELETED]'))
    input()
elif delete == "n":
    time.sleep(1)




