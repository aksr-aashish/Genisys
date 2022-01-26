import requests
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, pyfiglet
from colorama import init, Fore
import os, random
from time import sleep

init()

lg = Fore.LIGHTGREEN_EX
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
r = Fore.RED
n = Fore.RESET
colors = [lg, r, w, cy, ye]

def banner():
    f = pyfiglet.Figlet(font='slant')
    banner = f.renderText('Genisys')
    print(f'{random.choice(colors)}{banner}{n}')
    print(r+'  Version: 2.5 | Author: Cryptonian'+n+'\n')
#print('Author: github.com/Cryptonian007\n')
#sleep(4)

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    #print(r)
    banner()
    #print(n)
    print(lg+'[1] Add new accounts'+n)
    print(lg+'[2] Filter all banned accounts'+n)
    print(lg+'[3] List out all the accounts'+n)
    print(lg+'[4] Delete specific accounts'+n)
    #print(lg+'[5] Update your Genisys'+n)
    print(lg+'[5] Quit')
    a = int(input(f'\nEnter your choice: {r}'))
    if a == 1:
        with open('vars.txt', 'ab') as g:
            newly_added = []
            while True:
                a = int(input(f'\n{lg}Enter API ID: {r}'))
                b = str(input(f'{lg}Enter API Hash: {r}'))
                c = str(input(f'{lg}Enter Phone Number: {r}'))
                p = ''.join(c.split())
                pickle.dump([a, b, p], g)
                newly_added.append([a, b, p])
                ab = input('\nDo you want to add more accounts?[y/n]: ')
                if 'y' not in ab:
                    print('\n'+lg+'[i] Saved all accounts in vars.txt'+n)
                    g.close()
                    sleep(3)
                    clr()
                    print(lg + '[*] Logging in from new accounts...\n')
                    for added in newly_added:
                        c = TelegramClient(f'sessions/{added[2]}', added[0], added[1])
                        try:
                        	c.start(added[2])
                        	print(f'n\n{lg}[+] Logged in - {added[2]}')
                        	c.disconnect()
                        except PhoneNumberBannedError:
                        	print(f'{r}[!] {added[2]} is banned! Filter it using option 2')
                        	continue
                        print('\n')
                    input(f'\n{lg}Press enter to goto main menu...')
                    break
        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        with open('vars.txt', 'rb') as h:
            while True:
                try:
                    accounts.append(pickle.load(h))
                except EOFError:
                    break
        if not accounts:
            print(r+'[!] There are no accounts! Please add some and retry')
            sleep(3)
        else:
            for account in accounts:
                api_id = int(account[0])
                api_hash = str(account[1])
                phone = str(account[2])
                client = TelegramClient(f'sessions\\{phone}', api_id, api_hash)
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        client.sign_in(phone, input('[+] Enter the code: '))
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' is banned!'+n)
                        banned_accs.append(account)
            if not banned_accs:
                print(lg+'Congrats! No banned accounts')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Id = a[0]
                        Hash = a[1]
                        Phone = a[2]
                        pickle.dump([Id, Hash, Phone], k)
                k.close()
                print(lg+'[i] All banned accounts removed'+n)
            input('\nPress enter to goto main menu')
    elif a == 3:
        display = []
        with open('vars.txt', 'rb') as j:
            while True:
                try:
                    display.append(pickle.load(j))
                except EOFError:
                    break
        print(f'\n{lg}')
        print('API ID  |            API Hash              |    Phone')
        print('==========================================================')
        for z in display:
            print(f'{z[0]} | {z[1]} | {z[2]}')
        print('==========================================================')
        input('\nPress enter to goto main menu')

    elif a == 4:
        accs = []
        with open('vars.txt', 'rb') as f:
            while True:
                try:
                    accs.append(pickle.load(f))
                except EOFError:
                    break
        print(f'{lg}[i] Choose an account to delete\n')
        for i, acc in enumerate(accs):
            print(f'{lg}[{i}] {acc[2]}{n}')
        index = int(input(f'\n{lg}[+] Enter a choice: {n}'))
        phone = str(accs[index][2])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        with open('vars.txt', 'wb') as f:
            for account in accs:
                pickle.dump(account, f)
            print(f'\n{lg}[+] Account Deleted{n}')
            input(f'{lg}Press enter to goto main menu{n}')
    elif a == 5:
    	clr()
    	banner()
    	quit()
'''
    elif a == 5:
        print(f'{lg}Checking for updates...')
        try:
            import requests
            version = requests.get('link for the version file')
            file_version = int(open('version.txt', 'r').readline())
            if version > file_version:
                print(f'{lg} [*] New update available[Version:{version}]')
                prompt = str(print(f'{lg} [~] Do you want to install new update?[y/n]: {r}'))
                if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
                    print(f'{lg}[i] Installing updates...')
'''