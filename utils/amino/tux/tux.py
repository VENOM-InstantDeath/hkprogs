#!/usr/bin/env python3

import amino
import json
import action.act
import color
import multiprocessing
from os import listdir, system
from time import sleep
from getpass import getpass

cli = amino.Client()
print("\033[2J")

while True:
    if "creds" not in listdir():
        print("\t\tInicia sesión\n\n")
        CREDS = {"email": input("Correo electrónico: "), "password": getpass("Contraseña: ")}
        try:
            cli.login(**CREDS)
        except amino.exceptions.InvalidAccountOrPassword:
            print("\nCorreo o contraseña incorrectos")
            print("Presiona enter para continuar.")
            input()
            system("clear")
            continue
        F = open("creds", "w+")
        F.write(json.dumps(CREDS, indent=4))
        print("\033[2J")
    else:
        F = open("creds", "r")
        CREDS = json.load(F)
        cli.login(**CREDS)
        print("\033[2J")
    break

while True:
    print(f"{color.red}\t\t¿En qué comunidad deseas iniciar el bot?{color.nm}\n\n")
    COMM = input("aminoId: ")
    try:
        COMM = cli.search_community(COMM).comId[0]
        cli.join_community(COMM)
    except amino.exceptions.CommunityNotFound:
        print("Comunidad inexistente.")
        sleep(1)
        print("\033[2J")
        continue
    break

sub = amino.SubClient(COMM, cli.profile)
processes = []

while True:
    print("\033[2J")
    print(f"\t\t{color.red}Selecciona uno o más chats para iniciar el bot{color.nm}\n\n")
    chats = sub.get_public_chat_threads()
    for i in range(len(chats.title)):
        print(f"[{i}] {chats.title[i]}")
    chat = input("\nNúmero: ")
    if chat.isdigit() and int(chat) < len(chats):
        multiprocessing.Process(target=action.act.main, args=(COMM, chats.chatId[chat]))

    elif chat == "done":
        break

    else:
        print("Número inválido.")
        continue

print("Done!")
