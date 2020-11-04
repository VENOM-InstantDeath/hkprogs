#!/usr/bin/env python3

def tokenize(X: str) -> list:
    TT = []
    S = ""
    D = False
    C = False
    SP = False
    for i in X:
        if i == "[" and not D:
            D = True
            S += i
            continue
        if i == "]" and D:
            D = False
            S += i
            TT.append(S)
            S = ""
            SP = True
            continue
        if i == '"' and not C and not D:
            C = True
            S += i
            continue
        if i == '"' and C and not D:
            C = False
            S += i
            TT.append(S)
            S = ""
            SP = True
            continue
        if i == " " and (not S == "" or SP) and not D and not C:
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
    return TT

if __name__ == "__main__":
    X = input("> ")
    print(tokenize(X))
