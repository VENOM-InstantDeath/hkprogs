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

import shlex
from typing import List

def untoken(X: List, Y=False) -> str:
    if Y:
        s = ""
        for i in X:
            s += "{} ".format(str(i))
        return s.strip()
    s = ""
    for i in X:
        s += str(i)
    return s

def tokenize(x):
    x=shlex.split(x)
    return x

if __name__=="__main__":
    x=input(">")
    tokenize(x)
