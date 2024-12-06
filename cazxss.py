import requests
import re
import os

def scan_xss(url):
    response = requests.get(url)
    xss_vulnerable = False
    if os.name == 'nt':  
        file_path = 'C:\\Users\\LSCK\\payloads.txt'
    else:  # Linux
        file_path = 'payloads.txt'
    
    with open(file_path, 'r', encoding='utf-8') as file:
        payloads = file.read().splitlines()
    
    for payload in payloads:
        new_url = url + payload
        new_response = requests.get(new_url)

        if payload in new_response.text:
            print(f"Potential vulnerability detected at: {new_url}")
            xss_vulnerable = True
            break  
    
    if not xss_vulnerable:
        print("No vulnerabilities found.")


banner = """
\33[94m
==================================================================================================================================================================================================================
 $$$$$$\                                           $$$$$$\                      $$\       $$\   $$\                            $$$$$$\                                                             
$$  __$$\                                         $$  __$$\                     \__|      $$ |  $$ |                          $$  __$$\                                                            
$$ /  \__| $$$$$$\  $$$$$$$$\ $$$$$$$$\ $$\   $$\ $$ /  \__| $$$$$$\   $$$$$$$\ $$\       \$$\ $$  | $$$$$$$\  $$$$$$$\       $$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$ |       \____$$\ \____$$  |\____$$  |$$ |  $$ |\$$$$$$\  $$  __$$\ $$  _____|$$ |       \$$$$  / $$  _____|$$  _____|      \$$$$$$\  $$  _____|\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |       $$$$$$$ |  $$$$ _/   $$$$ _/ $$ |  $$ | \____$$\ $$ /  $$ |$$ /      $$ |       $$  $$<  \$$$$$$\  \$$$$$$\         \____$$\ $$ /      $$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$\ $$  __$$ | $$  _/    $$  _/   $$ |  $$ |$$\   $$ |$$ |  $$ |$$ |      $$ |      $$  /\$$\  \____$$\  \____$$\       $$\   $$ |$$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |\$$$$$$$ |$$$$$$$$\ $$$$$$$$\ \$$$$$$$ |\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$ |      $$ /  $$ |$$$$$$$  |$$$$$$$  |      \$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |$$ |  $$ |\$$$$$$$\ $$ |      
 \______/  \_______|\________|\________| \____$$ | \______/  \______/  \_______|\__|      \__|  \__|\_______/ \_______/        \______/  \_______|\_______|\__|  \__|\__|  \__| \_______|\__|      
                                        $$\   $$ |                                                                                                                                                 
                                        \$$$$$$  |                                                                                                                                                 
                                         \______/                                                                                                                                                  
==================================================================================================================================================================================================================
\033[36m
"""
print(banner)
print("#Example: https://xss.secrash.com/vuln.php?name=*&id_number=1337&submit=r")
print("By using the (*) character on the parameter you want to inject, this tool will inject it into that parameter")
print("# Note: if http is automatically redirected to https, then use the https protocol on the website you want to scan")
url = input("Website url: ")
scan_xss(url)

