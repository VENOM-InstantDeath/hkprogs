#!/usr/bin/env python3

import color
import sys


class Bar:
    def __init__(self, y: int, x: int) -> None:
        sys.stdout.write(f"\033[{y};{x}f")
        sys.stdout.write(f"{color.green}[")
        for i in range(10):
            sys.stdout.write("-")
        sys.stdout.write(f"]{color.nm}")
        print()

        self.coords = [y, x]
        self.prog = 0
        self.unit = 10

    def wprog(self) -> None:
        sys.stdout.write(color.green)
        sys.stdout.write(f"\033[{self.coords[0]};{self.coords[1] + 1}f")
        for i in range(int(self.prog / 10)):
            sys.stdout.write("#")
        sys.stdout.write(color.nm)
        print()

    def kprog(self) -> None:
        sys.stdout.write(f"\033[{self.coords[0]};{self.coords[1]}f")
        for i in range(12):
            sys.stdout.write(" ")


if __name__=="__main__":
    sys.stdout.write("\033[2J")
    bar1 = Bar(40, 60)
    arr = [0,0,0,0,0,0,0,0,0]
    from time import sleep
    bar1.unit = ((1*100/len(arr)))
    c = 0
    while int(bar1.prog) != int(bar1.unit*len(arr)):
        sleep(1)
        arr[c] = 8
        c += 1
        bar1.prog += bar1.unit
        bar1.wprog()
        print(f"\033[40;50f{int(bar1.prog)}%")
        print(f"\033[41;50fArray: {arr}")
        print(f"\033[42;50fLength: {len(arr)}")
        print(f"\033[43;50fVar $c: {c}")
        print(f"\033[44;50fcycles: {bar1.unit*len(arr)}")
        print(f"\033[45;50fProgress: {bar1.prog}")
    bar1.kprog()
    sleep(1)
    sys.stdout.write("\033[f")
