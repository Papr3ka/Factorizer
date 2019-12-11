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
def wait():
    if waitsetc == 2:
        wait = str(input("Press enter to continue..."))
        clear()
    if waitsetc == 1:
        clear()
        wait = str(input("Press enter to continue..."))
    if waitsetc == 0:
        wait = str(input("Press enter to exit..."))
def inttest(x):
    decval = int(x) - x
    if decval == 0:
        return True
    else:
        return False
waitsetc = 1
clear()
fact = int(input("Factorize:"))
wait()
clear()
print("Factorizing...")
factors = [1]
tstart = time.perf_counter()
for x in range(1,int(fact / 2) + 1,1):
    ans = fact / x
    if inttest(ans):
        factors.append(int(ans))
tend = time.perf_counter()
factors.sort()
clear()
print("Done\n")
if len(factors) > 2:
    print(fact,"Has",len(factors),"Factors")
else:
    print(fact,"Is a prime number")
print("Showing Factors for",fact)
print("\n")
for x in factors:
    print(x)
print("\nTime",int((tend - tstart) * 10000) / 10000,"Seconds")
waitsetc = 0
wait()        
