# -*- coding: utf-8 -*-
import json as js
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from time import sleep
import clipboard
from selenium.webdriver.support.ui import Select
from random_username.generate import generate_username
from colorama import Fore
import os ,sys


def printf(text):
    for char in text: print("" + char, end="");sys.stdout.flush();sleep(0.045)


def main_menu():
    try:
        printf(f"[!] Setting config...")
        if os.path.isfile("config.json"):
            printf(f"\n[+] Success load!")
            os.system("cls")
            os.system("title WhiteHole Instagram account gen")
            sleep(1)
            os.system("mode 200,40")
            print(f"""{Fore.LIGHTBLUE_EX}
            
                
                ██     ██ ██   ██ ██ ████████ ███████ ██   ██  ██████  ██      ███████     ██ ███    ██ ███████ ████████  █████       █████   ██████  ██████      ██████  ███████ ███    ██ 
                ██     ██ ██   ██ ██    ██    ██      ██   ██ ██    ██ ██      ██          ██ ████   ██ ██         ██    ██   ██     ██   ██ ██      ██          ██       ██      ████   ██ 
                ██  █  ██ ███████ ██    ██    █████   ███████ ██    ██ ██      █████       ██ ██ ██  ██ ███████    ██    ███████     ███████ ██      ██          ██   ███ █████   ██ ██  ██ 
                ██ ███ ██ ██   ██ ██    ██    ██      ██   ██ ██    ██ ██      ██          ██ ██  ██ ██      ██    ██    ██   ██     ██   ██ ██      ██          ██    ██ ██      ██  ██ ██ 
                 ███ ███  ██   ██ ██    ██    ███████ ██   ██  ██████  ███████ ███████     ██ ██   ████ ███████    ██    ██   ██     ██   ██  ██████  ██████      ██████  ███████ ██   ████ 
                                                                                                                                                                                                                                                                        
                                        Dev : WhiteHole
                                        Telegram : https://t.me/whitehole0906



        ┌─  Instagram Account generator ────────────────────────────────────┐
        │  [1] Gen Start                                                    │
        │  [2] about                                                        │
        │  [3] Exit                                                         │
        │  [4] reload                                                       │
        └───────────────────────────────────────────────────────────────────┘
            {Fore.RESET}""")
            go_ = input(f'''{Fore.LIGHTBLUE_EX}
        │
        │
        └─> {Fore.RESET}''')

            if go_.upper() in ['1']:
                Start_GEN()
            elif go_.upper() in ['2']:
                print(f"""{Fore.BLUE}
                개발자 : 화이트홀
                디스코드 : Not WhiteHole#1162 or 화이트홀미만잡#8210
                텔레그램 : @whitehole0906
                깃허브 : https://github.com/WhiteHole00
                {Fore.RESET}""")  
            elif go_.upper() in ['3']:
                input("Please ENTER to quit.")
            elif go_.upper() in ['4']:
                main_menu()
    except Exception as e:
        print(e)
        return input(f"{e}\nPlease ENTER to quit.")





def Start_GEN():
    with open("config.json") as read:
        load_data = js.load(read)
        WENHOOK_LOG  = load_data["Discord_Webhook_log"]
        PASSWORD = load_data["password"]
        random_name = load_data["Random_name"]
        proxy = load_data["proxy"]
        webhook_url = load_data["Discord_Webhook-URL"]
    global name_
    global email
    name_ = 0
    email = 0
    if random_name == "Y":
        name___ = open("names.txt" , "r" )
        real_names = name___.read()
        name_ = real_names
    elif random_name == "N":
        real_name = input(f"{Fore.LIGHTBLUE_EX} [+] 유저 이름을 적어주세요 (특수문자 사용 가능) :  {Fore.RESET}")
        name_ = real_name
    else:
        return input(f"{Fore.RED} [-] please check 'Random_name' in config.json {Fore.RESET}")
    
    li = ["1997","1996","1995"]

    if proxy == "Y":
        prox = open("proxies.txt" , "r" )
        PROXIES = prox.read()
        print(PROXIES)
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXIES,
        "sslProxy": PROXIES,
        "proxyType": "MANUAL"
        }
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--start-maximized")
        client = webdriver.Chrome(executable_path=CM().install(), options=options)
        client.set_window_size(1920,1080)
        client.get("https://www.instagram.com/accounts/emailsignup/")
        sleep(2)
        client.execute_script('window.open("https://temp-mail.org/");')
        sleep(1)
        client.switch_to.window(client.window_handles[-1])
        print("Email get..")
        sleep(23)
        print("SUCCESS")
        WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/button'))).click()
        email = clipboard.paste()
        print(email)
        sleep(1)
        client.switch_to.window(client.window_handles[0])
        sleep(3)
        send_email = WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input')))
        send_email.send_keys(email)
        sleep(1)
        name = WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input')))
        name.send_keys(f"{name_}")
        sleep(1)
        user_name = WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input')))
        user_name.send_keys(name_)
        sleep(1)
        password = WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input')))
        password.send_keys(PASSWORD)
        sleep(2)
        WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button'))).click()
        sleep(5)
        years = Select(WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select'))))
        years.select_by_visible_text("1997")
        sleep(2)
        WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[6]/button'))).click()
        sleep(2) 
        client.switch_to.window(client.window_handles[-1])
        sleep(25)
        for i in range(3):
            client.execute_script("window.scrollTo(0, 730)")
        code = WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a'))).text
        real_code = f"{code[0]}{code[1]}{code[2]}{code[3]}{code[4]}{code[5]}"
        print(real_code)
        sleep(3)
        client.switch_to.window(client.window_handles[0])
        input_code = WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input')))
        input_code.send_keys(real_code)
        sleep(1)
        WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]'))).click()
        sleep(1)
        WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[3]/div[1]/div[2]/input'))).click()
        sleep(3)
        WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/button'))).click()
        sleep(10)
        print("success")
        os.system("cls")
        print(f"{Fore.GREEN} [+] 성공적으로 인스타그램 계정을 생성 완료 하였습니다!\nEmail : {email}\nPassword : {PASSWORD} {Fore.RESET}")
        with open('account.txt', 'a',encoding="UTF-8") as w:
            w.write(f"{email}:{PASSWORD}:{name_}")

        web_msg = f"""
            **```css
            [+] Instagram Account LOG
            ```

            **```yaml
            EMAIL : {email}
            ID : {name_}
            ```**

            ```
            https://github.com/WhiteHole00
            화이트홀미만잡#8210
            https://t.me/whitehole0906
            ```
        """
        if WENHOOK_LOG == "Y":
            data = {
                "username":"WhiteHole Instagram Account Generator LOG",
                "avatar_url": f"https://ghanainsider.com/wp-content/uploads/2022/07/0e4b_5410131.jpg",
                "content": web_msg     
                        }
            import requests as req
            req.post(webhook_url, json=data)
        return input("Please ENTER to quit.")
    except Exception as e:
        return input(f"ERROR! {e}\nPlease ENTER to quit.")
    
if __name__ == "__main__":
    main_menu()