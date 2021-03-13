import amino
import json


class Say:
    def __init__(self, comm, achat):
        cli = amino.Client()
        f = open("creds", "r")
        creds = json.load(f)
        cli.login(**creds)
        sub = None #Client() Podrá mandar y leer mensajes??
    def say(self, x, y):
        sub.send_message(x, y)
