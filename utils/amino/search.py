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

from tokens import tokenize
from typing import List

def compare(x, y):
    coin = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            coin += 1
    perc = coin*100/len(x)
    return (coin, perc)

def alg(x: List[str], y: List[str]) -> str:
    # x memelist, y meme solicitado
    start = 0
    for a in range(len(x)): # main list
        #determinar el comienzo del meme
        for b in range(len(x[a])): # sublist
            if len(x[a][b]) == len(y[0]):
                comp = compare(x[a][b], y[0])
                if comp[1] >= 60:
                    start = (a, b)
    if start == 0:
        raise(RuntimeError)
    print(comp)
    print("start",start)
    x = x[start[0]][start[1]:]
    return x


def search(x: List[str]) -> str:
    #crear listas en memelist
    memelist = ["abran paso a un par de emprendedores", "ahí viene", "ahora si se viene lo chido", "ah shit here we go again", "algo anda mal", "algo no anda bien en lazy town", "anota eso anota eso", "argentina un país con buena gente", "bueno quién tiene hambre", "cerebrón", "demonios", "diablos señorita", "eres como hitler", "esas preguntas no me dejan dormir", "es el día opuesto", "es el viejo jenkins", "eso no me lo esperaba", "eso tiene sentido para mí", "esta", "hackerman", "hay destinos peores que la muerte", "hola señor turner", "horrified gumball", "i love democracy", "jaja qué dice el boludo de arriba", "komo lo zupo", "las cosas como son", "llamada del circo", "maravillosa jugada", "me da asco solo verlo", "me perturba", "me recordó a mí", "mike sullivan", "mi manera es la manera de los dioses", "miren es mi día de suerte", "mucho texto", "muy sospechoso", "nada no hay no existe", "no confundas las cosas negro", "noice", "no necesito dormir necesito respuestas", "no seas tan crédulo mcfly", "parece que aún tengo aliados en el olimpo", "pero hey las risas no faltaron", "que trucazo no", "quien io", "quita tu cochinada de aquí", "rae", "según mi perapod eso es imposible", "si es real podría valer una fortuna", "soy admin", "soy el sucio dan", "stonks", "te atreves a usar mis propios hechizos", "this is fine", "tu suerte acaba de terminarse", "un clásico", "vivan las mentiras", "ya estoy hasta la puta madre", "yo sólo sé decir de nada"]
    for i in range(len(memelist)):
        memelist[i] = tokenize(memelist[i]).full
    try:
        B=alg(memelist, x)
    except:
        return "Plantilla no encontrada"
    print(B)

if __name__=="__main__":
    x = input(">")
    y=search(tokenize(x).full)
    if y == "Plantilla no encontrada":
        print(False)
