import os
import sys
import time



print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█                           RUN.PY                             █
█                                    Created By Pavan Yadav    █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")


print("\033[1;34m\n[++] Starting Mysqld ... \033[1;m")
time.sleep(2)
apache=os.system("mysqld")
print("\033[1;34m\n[++] Press Enter To Countinue ... \033[1;m")
print("\033[1;34m\n[++] Enter The path of the file ... \033[1;m")
path=input()
print("\033[1;34m\n[++] Enter The Address Ex. 127.0.0.1:8080 ... \033[1;m")
add=input()
php=os.system("php -t "+path+" -S "+add+"")

print("\033[1;34m\n[++] Enter To Countinue ... \033[1;m")

print("\033[1;34m\n[++] Enter The NGROK PORT Ex 8080 ... \033[1;m")

port=input()

os.system("./ngrok http "+port+"")



