#!/usr/bin/env python3

from typing import List

class obj:
    def __init__(self):
        self.corch = []
        self.parent = []
        self.comilla = []
        self.comm = []
        self.size = 0
        self.full = []

def untoken(X: List) -> str:
    s = ""
    for i in X:
        s += str(i)
    return s

def tokenize(X: str) -> List[str]:
    retobj = obj()
    TT = []
    S = ""
    D = False # []
    P = False # ()
    C = False # ""
    SP = False
    for i in X:
        if i == "[" and not D and not C: # Abre corchetes
            D = True
            S += i
            continue
        if i == "]" and D and not C: # Cierra corchetes
            D = False
            S += i
            TT.append(S)
            S = ""
            SP = True
            continue
        if i == '(' and not P and not D: # Abre paréntesis
            P = True
            S += i
            continue
        if i == ')' and P and not D: # Cierra paréntesis
            P = False
            S += i
            TT.append(S)
            S = ""
            SP = True
            continue
        if i == '"' and not C and not P and not D: # Abre comillas
            C = True
            S += i
            continue
        if i == '"' and C and not P and not D: # Cierra comillas
            C = False
            S += i
            TT.append(S)
            S = ""
            SP = True
            continue
        if i == " " and (not S == "" or SP) and not D and not P and not C: # Espacios
            if SP:
                SP = False
                continue
            TT.append(S)
            S = ""
            continue
        S += i
    if not S == "":
        TT.append(S)
    S = ""
    for i in TT:
        if i.startswith('"'):
            retobj.comilla.append(i)
            continue
        elif i.startswith('['):
            retobj.corch.append(i)
            continue
        elif i.startswith('('):
            retobj.parent.append(i)
            continue
        else:
            retobj.comm.append(i)
            continue
    retobj.size = len(X)
    retobj.full = TT
    return retobj

if __name__ == "__main__":
    X = input("> ")
    O = tokenize(X)
    print("Completo: {}".format(O.full))
    print("Tamaño: {}".format(O.size))
    print("Corchetes: {}".format(O.corch))
    print("Paréntesis: {}".format(O.parent))
    print("Comillas: {}".format(O.comilla))
    print("Otro: {}".format(O.comm))
