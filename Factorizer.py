# -*- coding: utf-8 -*-
# Copyright (c) 2019 Benjamin Yao
import platform
import os
import time
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
def inttest(x):
    decval = int(x) - x
    if decval == 0:
        return True
    else:
        return False
clear()
fact = int(input("Factorize:"))
clear()
factors = [fact]
for x in range(1,fact,1):
    ans = fact / x
    if inttest(ans):
        print(x)
        factors.append(ans)
        