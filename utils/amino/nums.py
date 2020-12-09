#!/usr/bin/env python3

#   This file is part of hkprogs

#   hkprogs is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   hkprogs is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

from tokens import untoken
from typing import List
import re
#"(.?)+\("

class numres:
    def __init__(self):
        pass
    def res(self, x: List): # Recibe una lista y devuelve s y p
        s = [0,0] # índice - inicio y final del paréntesis más profundo
        p = [0,0] # paréntesis - contador de aperturas y cierres
        con = False
        for i in range(len(x)):
            if x[i] == '(':
                p[0] += 1
                if not con:
                    s[0] = i
            if x[i] == ')':
                p[1] += 1
                if not con:
                    s[1] = i
                    con = True
        return s, p

    def numtok(self, x: str) -> List: # separa numeros de operadores
        if x == "":
            raise RuntimeError
        TT = []
        S = ""
        O = ""
        aux = ""
        sym = ['+', '-', '*', '/', '(', ')', '[', ']']
        SP = False
        for i in range(len(x)):
            if SP:
                SP = False
                O += x[i]
                if S != "":
                    TT.append(S)
                S = ""
                TT.append(O)
                O = ""
                continue
            if not x[i] in sym:
                S += x[i]
                continue
            elif x[i] in sym and x[i] == "*" and x[i+1] == "*":
                O += x[i]
                SP = True
                continue
            elif x[i] in sym:
                if S != "":
                    TT.append(S)
                S = ""
                TT.append(x[i])
                continue
        if S != "":
            TT.append(S)
            S = ""
        return TT

    def recsec(self, x: List[str]):
        acu = 0
        s = [0, []]
        LI = 200
        SP = False
        sym = ['+', '-', '*', '/', '(', ')', '[', ']']
        for i in range(len(x)):
            if SP:
                if x[i] == '**':
                    continue
                elif x[i] in sym or i == len(x)-1:
                    if int(s[0]) > 99999:
                        LI = 10
                    for e in s[1]:
                        if acu > LI:
                            raise RuntimeError
                        if acu == 0:
                            acu += int(e)
                        acu *= acu
                        if acu > 200:
                            raise RuntimeError
                        
                    SP = False
                    s = [0, []]
                    continue
                else:
                    s[1].append(x[i])
            if x[i] == '**':
                s[0] = x[i-1]
                SP = True

    def inum(self, x): # Master
        x = x.replace('"','')
        osym = ['+', '-', '*', '/', '**']
        x = x.replace(' ', '')
    
        for i in x:
            if re.match("[0-9\+\-\*\/\(\)\.]", i):
                pass
            else:
                raise ValueError
        TT = self.numtok(x)
        self.recsec(TT)
        while re.match("(.?)+\(", untoken(TT)):
            s,p = self.res(TT)
            ss = untoken(TT[s[0]:s[1]+1])
            del TT[s[0]:s[1]+1]
            TT.insert(s[0], eval(ss))
            if TT[s[0]-1] not in osym and TT[s[0]-1] != '(' and s[0] != 0:
                TT.insert(s[0],'*')
                s[0] += 1
    
        return eval(untoken(TT))
    
if __name__=="__main__":
    nu = numres()
    X = input("> ")
    print(nu.inum(X))
