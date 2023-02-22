# -*- coding: utf-8 -*-
import json as js
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import clipboard
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from colorama import Fore
import os 
import random
from plyer import notification
from random_username.generate import generate_username
import json

def isRandomNameGen(count):
    count = int(count)
    namelist = []
    for _ in range(count):
        name = generate_username(1)[0]+"_."+"whitehole"
        namelist.append(name)
        print(name)
    f = open("./acc_gen/random_names.txt", "a")
    for i in namelist:
        f.writelines(f"{i}\n")
    print(f"{Fore.LIGHTCYAN_EX}[+] 랜덤 이름 {count}개 생성이 완료 되었습니다!")
    return input("아무 키를 눌러 종료 해 주세요.")

def isSendMsg(msg):
    notification.notify(
    title = 'WhiteHole Instagram Account Generator',
    message = msg,
    app_name = "Insta Acc Gen",
    #app_icon = 'ico'
    timeout = 10,  
)


def isStartGen():
    with open("config.json") as read:
        load_data = js.load(read)
        WENHOOK_LOG  = load_data["Discord_Webhook_log"]
        PASSWORD = load_data["password"]
        random_name = load_data["Random_name"]
        proxy = load_data["proxy"]
        webhook_url = load_data["Discord_Webhook-URL"]
    name_ = 0
    email = 0
    email_ = []
    account = {"accounts" : []}
    if random_name == "Y":
        name___ = open("./acc_gen/names.txt" , "r" )
        real_names = name___.read().split("\n")
        name_ = random.choice(real_names)
        print(f"{Fore.LIGHTGREEN_EX}[+] NAME : {name_} {Fore.RESET}")
        print(f"{Fore.LIGHTGREEN_EX}[+] 랜덤 이름 으로 시작 됩니다.\nFile : names.txt{Fore.RESET} ")
    elif random_name == "N":
        real_name = input(f"{Fore.LIGHTBLUE_EX} [+] 유저 이름을 적어주세요 (특수문자 사용 가능) :  {Fore.RESET}")
        name_ = real_name
    else:
        return input(f"{Fore.RED} [-] please check 'Random_name' in config.json {Fore.RESET}")
    
    li = ["1997","1996","1995"]

    if proxy == "Y":
        prox = open("./acc_gen/proxies.txt" , "r" )
        PROXIES = prox.read().split("\n")
        PROXY = random.choice(PROXIES)
        print(PROXY)
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL"
        }
    try:
        msg = f"인스타그램 계정 생성을 시작합니다.\n\n랜덤이름 여부 : {random_name}\n\n프록시 사용 여부 : {proxy}\n\n웹훅 로그 사용 여부 : {WENHOOK_LOG}"
        isSendMsg(msg)
        options = Options()
        #options.add_argument("headless")
        chrome = Service("./acc_gen/chromedriver.exe")
        client = webdriver.Chrome(service=chrome, options=options)
        client.get("https://www.instagram.com/accounts/emailsignup/")
        sleep(2)
        client.execute_script('window.open("https://temp-mail.org/");')
        sleep(1)
        client.switch_to.window(client.window_handles[-1])
        print(f"{Fore.LIGHTGREEN_EX} Email getting.. {Fore.RESET}")
        #sleep(21)
        sleep(20)
        WebDriverWait(client, 70).until(EC.presence_of_element_located(( By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/button'))).click()
        email = clipboard.paste() #클립보드에 복사
        email_.append(email)
        email = "".join(email_)
        print(f"{Fore.LIGHTGREEN_EX} Email : {email} {Fore.RESET}")
        sleep(1)
        client.switch_to.window(client.window_handles[0])
        sleep(3)
        send_email = WebDriverWait(client, 70).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input')))
        print(send_email.text)
        send_email.send_keys(email) 
        sleep(1)
        name = WebDriverWait(client, 70).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input')))
        name.send_keys(f"화_이_트_홀") # 인스타 그램 이름 
        sleep(1)
        user_name = WebDriverWait(client, 70).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input')))
        user_name.send_keys(name_) #인스타 그램 아이디
        sleep(1)
        password = WebDriverWait(client, 70).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input')))
        password.send_keys(PASSWORD) #pw
        sleep(2)
        WebDriverWait(client, 70).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button'))).click()
        sleep(5)
        years = Select(WebDriverWait(client, 70).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select'))))
        years.select_by_visible_text(random.choice(li))
        sleep(2)
        WebDriverWait(client, 70).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[6]/button'))).click()
        sleep(2) 
        client.switch_to.window(client.window_handles[-1])
        sleep(25)
        for i in range(3): # 화면 내리기
            client.execute_script("window.scrollTo(0, 730)")
        code = WebDriverWait(client, 70).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[2]/span/a'))).text
        real_code = f"{code[0]}{code[1]}{code[2]}{code[3]}{code[4]}{code[5]}" # code 텍스트에서 인덱스 5번째까지가 인증 코드 
        print(real_code)
        sleep(3)
        client.switch_to.window(client.window_handles[0])
        input_code = WebDriverWait(client, 70).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input')))
        input_code.send_keys(real_code)
        sleep(1)
        WebDriverWait(client, 70).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]'))).click()
        sleep(1)
        WebDriverWait(client, 70).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[3]/div[1]/div[2]/input'))).click()
        sleep(3)
        WebDriverWait(client, 70).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/button'))).click()
        sleep(10)
        print("success")
        os.system("cls")
        print(f"{Fore.GREEN} [+] 성공적으로 인스타그램 계정을 생성 완료 하였습니다!\nEmail : {email}\nPassword : {PASSWORD} {Fore.RESET}")
        acc = {}
        acc["EMAIL"] = email
        acc["PASSWORD"] = PASSWORD
        acc["INSTA_ID"] = name_
        acc["INSTA_NAME"] = "화_이_트_홀"
        account["accounts"].append(acc)
        with open('./acc_gen/Account.json', 'w',encoding="UTF-8") as w:
            w.write(json.dumps(account, indent=4))
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
        client.quit()
        return input("Please ENTER to quit.")
    except Exception as e:
        return input(f"ERROR! {e}\nPlease ENTER to quit.")