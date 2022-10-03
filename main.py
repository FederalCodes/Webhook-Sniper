error = False
try:
    import os
    os.system("title " + "Webhook Sniper,   Made By Federal#6666,   Github: github.com/FederalCodes")
except:
    pass

import sys, time
def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)



try:
    import colorama, requests
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama requests")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()


webs = []


import random, time, threading
colorama.init(autoreset=True)
choice = "1234567890"
choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
def sniper():
    global webs
    while True:
        ide = random.choices(choice, k=18)
        ide = "".join(ide)
        code = random.choices(choices, k=68)
        code = "".join(code)
        webhook = "https://discord.com/api/webhooks/"+str(ide)+"/"+str(code)
        r = requests.get(webhook)
        if "200" in str(r):
            webs.append("Valid Webhook! "+webhook)
            if save == "y":
                valid = open("valid_webhooks.txt", "a")
                valid.write(webhook+"\n")
                valid.close()
        else:
            webs.append("Invalid Webhook! "+webhook)
            if save == "y":
                invalid = open("invalid_webhooks.txt", "a")
                invalid.write(webhook+"\n")
                invalid.close()
        time.sleep(float(delay))
def valid():
    sys.stdout.write(colorama.Fore.RED + "> ")
    print015("Enter A Valid Choice")
    return
while True:
    try:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Enter How Many Threads You Want: ")
        threads = input("")
        threads = int(threads)
        break
    except:
        valid()
while True:
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print01("Wanna Auto Save Webhooks (y/n): ")
    save = input("")
    if save == "y" or save == "n":
        break
    else:
        valid()
while True:
    try:
        sys.stdout.write(colorama.Fore.CYAN + "> ")
        print01("Enter Delay For Each Thread (0 = No Delay): ")
        delay = input("")
        delay = float(delay)
        break
    except:
        valid()
for u in range(int(threads)):
    threading.Thread(target=sniper).start()
    sys.stdout.write(colorama.Fore.CYAN + "> ")
    print("Started Thread")

den = 0

while True:
    for u in webs:
        webs.remove(u)
        den = int(den) + 1
        if "Invalid" in u:
            sys.stdout.write(colorama.Fore.RED + "> ")
            print(f"Invalid Webhook {colorama.Fore.RED}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.RED}]")


        if "Valid" in u:
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print(f"Valid Webhook {colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(den)}{colorama.Fore.CYAN}]")

