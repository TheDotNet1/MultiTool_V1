import random
import os
from re import S
import sys
from time import sleep
from typing import Text, clear_overloads
import requests
import socket
from colorama import Fore

user = os.getlogin()

os.system("clear")

print(f"Benvenuto {user}")
print("""Cosa vuoi fare?
         1) Scan di un target;
         2) Ping di un target;
         3) Tracciare posizione IP (Posizione approssimativa)""")

def scan():
    os.system("clear")
    print("""Che tipo di scansione desideri fare?
            1) Scan veloce;
            2) Scan dettagliato (Richiede qualche minuto);""")

    tipoScan = input()

    if tipoScan == "1":
        target = input("Inserire IP target: ")
        os.system("clear")
        print("Avviando la scansione...")
        sleep(3)
        os.system("clear")
        print("Scan avviata!")
        os.system(f"nmap {target} -o {target}_scan.txt")
        print("Scansione terminata... Chiudere il programma?")
        closeProg = input("S o N: ")
        if closeProg == "S" or "s":
            sys.exit("Sto chiudendo, Buona giornata!")
        elif closeProg == "N" or "n":
            print("Va bene, torno al Menu' principale...")
            sleep(1)
            mainMenu()
        else:
            print("Errore, sto riavviando...")
            mainMenu()

    elif tipoScan == "2":
        target = input("Inserire IP target: ")
        os.system("clear")
        print("Avviando la scansione...")
        sleep(3)
        os.system("clear")
        print("Scan avviata!")
        os.system(f"nmap -sV -sC {target} -o {target}_scan.txt")
        print("\nScansione terminata... Chiudere il programma?")
        closeProg = input("S o N: ")
        if closeProg == "S" or "s":
            sys.exit("Sto chiudendo, Buona giornata!")
        elif closeProg == "N" or "n":
            print("Va bene, torno al Menu' principale...")
            sleep(1)
            mainMenu()
    else:
        print("Errore, sto riavviando...")
        scan()

def trackIp():

    target = input("Inserire IP target: ")

    url = "http://ip-api.com/json/{target}"

    req = requests.get(url.format(target=target))

    print(req.json())

    input("Premere un tasto per tornare al Menu' Principale... ")

    os.system("clear")

    mainMenu()

def pingIp():
    try:

        os.system("clear")

        print("Configurazione in corso...")

        sleep(2)

        os.system("clear")

        target = input("Inserire IP target: ")
        port = input("Inserire PORTA target: ")

        def tcpping(ip,port):
            try:
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((ip,port))
                print(f"{Fore.GREEN}Connetto a {Fore.MAGENTA}{target} {Fore.GREEN} sulla porta {Fore.WHITE}{port}!")
            except:
                print(f"{Fore.MAGENTA}{target} {Fore.GREEN} is DOWN!")

    except KeyboardInterrupt:
        print("Andando al menu principale")
        exit()



    while True:
        tcpping(target, int(port))
        sleep(1)


def mainMenu():
    os.system("clear")
    print(f"Benvenuto {user}")
    print("""Cosa vuoi fare?
            1) Scan di un target;
            2) Ping di un target;
            3) Tracciare posizione IP (Posiziona approssimativa)""")

    scelta = input()

    if scelta == "1":
    	scan()
    elif scelta == "2":
    	pingIp()
    elif scelta == "3":
    	trackIp()
    else:
        print("Errore, Sto riavviando...")
        mainMenu()

	
scelta = input()

if scelta == "1":
    scan()
elif scelta == "2":
    pingIp()
elif scelta == "3":
    trackIp()
else:
    print("Errore, Sto riavviando...")
    mainMenu()
