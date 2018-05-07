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
os.system("mysqld&")
print("\033[1;34m\n[++] it lokks Like Mysql Service started ... \033[1;m")
print("\033[1;34m\n[++] Initializing Php ... \033[1;m")
input()
print("\033[1;34m\n[++] Enter The path of the file ... \033[1;m")
path=input()
print("\033[1;34m\n[++] Enter The Address Ex. 127.0.0.1:8080 ... \033[1;m")
php=os.system("php -t "+path+" -S "+add+" &")
input()
print("\033[1;34m\n[++] Enter The NGROK PORT Ex 8080 ... \033[1;m")

port=input()

os.system("./ngrok http "+port+"")



