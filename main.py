# -*- coding: utf-8 -*-
from time import sleep
import os ,sys
from colorama import Fore

def printf(text):
    for char in text: print("" + char, end="");sys.stdout.flush();sleep(0.045)

def main_menu():
    try:
        printf(f"[!] Setting config...")
        if os.path.isfile("config.json"):
            printf(f"\n[+] Success load!")
            os.system("cls")
            os.system("title WhiteHole Instagram Account Gen")
            sleep(1)
            os.system("mode 200,40")
            print(f"""{Fore.LIGHTBLUE_EX}
            
                
                ██     ██ ██   ██ ██ ████████ ███████ ██   ██  ██████  ██      ███████     ██ ███    ██ ███████ ████████  █████       █████   ██████  ██████      ██████  ███████ ███    ██ 
                ██     ██ ██   ██ ██    ██    ██      ██   ██ ██    ██ ██      ██          ██ ████   ██ ██         ██    ██   ██     ██   ██ ██      ██          ██       ██      ████   ██ 
                ██  █  ██ ███████ ██    ██    █████   ███████ ██    ██ ██      █████       ██ ██ ██  ██ ███████    ██    ███████     ███████ ██      ██          ██   ███ █████   ██ ██  ██ 
                ██ ███ ██ ██   ██ ██    ██    ██      ██   ██ ██    ██ ██      ██          ██ ██  ██ ██      ██    ██    ██   ██     ██   ██ ██      ██          ██    ██ ██      ██  ██ ██ 
                 ███ ███  ██   ██ ██    ██    ███████ ██   ██  ██████  ███████ ███████     ██ ██   ████ ███████    ██    ██   ██     ██   ██  ██████  ██████      ██████  ███████ ██   ████ 

                 {Fore.RESET}
                                {Fore.LIGHTMAGENTA_EX}                                                                                                                                                                                                                                     
                                Dev : WhiteHole
                                Telegram : https://t.me/whitehole0906\
                                {Fore.RESET}


        {Fore.CYAN}
        ┌─  Instagram Account generator ────────────────────────────────────┐
        │  [1] Gen Start                                                    │
        │  [2] about                                                        │
        │  [3] Exit                                                         │
        │  [4] reload                                                       │
        │  [5] Random Name Gen                                              │
        └───────────────────────────────────────────────────────────────────┘
            {Fore.RESET}""")
            go_ = input(f'''{Fore.LIGHTBLUE_EX}
        │
        │
        └─> {Fore.RESET}''')

            if go_ == "1":
                from acc_gen.AccountGen import isStartGen
                isStartGen()
            elif go_ == "2":
                print(f"""{Fore.LIGHTBLUE_EX}
                개발자 : 화이트홀
                디스코드 : Not WhiteHole#1162 or 화이트홀미만잡#8210
                텔레그램 : @whitehole0906
                깃허브 : https://github.com/WhiteHole00
                {Fore.RESET}""")  
            elif go_=="3":
                input("Please ENTER to quit.")
            elif go_=="4":
                main_menu()
            elif go_ == "5":
                from acc_gen.AccountGen import isRandomNameGen
                cnt = int(input("[+] 횟수를 입력 해 주세요 >> "))
                isRandomNameGen(cnt)
    except Exception as e:
        print(e)
        return input(f"{e}\nPlease ENTER to quit.")

    
if __name__ == "__main__":
    main_menu()