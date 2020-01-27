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
def checkprime(x):
    if x >= 2:
        for y in range(2,x,1):
            if not( x % y ):
                return False
    else:
        return False
    return True
waitsetc = 1
tstart = 0
tend = 0
clear()
try:
    fact = int(input("Factorize:"))
    if not(checkprime(fact)):
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
        print(fact,"Has",len(factors),"Factors")
    else:
        print("Done\n")
        factors = [1,fact]
        clear()
        print(fact,"Is a prime number")
    print("Showing Factors for",fact)
    print("\n")
    for x in factors:
        print(x)
    print("\n")
    print("Time:",'%.4f'%(tend - tstart),"Seconds")
except:
    print("Invalid Input")
waitsetc = 0
wait()
clear()
# End of Program
