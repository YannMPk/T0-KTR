#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser(prog="star.py", usage="python %(prog)s <number>")
parser.add_argument("L", type=int)
args = parser.parse_args()

L = args.L

if L < 0:
    print("usage : star.py <number>")
    exit()
elif L == 0:
    exit()

dim = 2*L+1

#TRIANGLE HAUT
if L == 1:
    print(" ",end="")
for i in range(1, L+1):
    for j in range(1, dim+L-i+1): 
        print(" ",end="")

    for j in range(1, 2*i):
        if j == 1 or j == 2*i-1:
            print("*",end="")
        else:
            print(" ",end="")

    print()

#LIGNE BASE TRIANGE 
b = 0
if L == 1:
    dim = 2*L+2
elif L==2:
    dim = 2*L+1
print(" ",end="")
for j in range(1, dim):
        print("*",end="")
        b+=1
for j in range(1, 2*L):
    if j == 1 or j == 2*L-1:
        if L == 1:
            print(" ",end="")
            break
        print("*",end="")
        b+=1
    else:
        print(" ",end="")
        b+=1
for j in range(1, dim):
        print("*",end="")

#DESCENTE MILIEU 1
print()
if L == 1:
    print(" ",end="")
if L > 2:
    nd = 0
    dd = L
elif L == 1:
    dd = 1
    nd = 0
else :
    nd = 1
    dd = L
for k in range(dd, nd, -1):
    print(" ",end="")

    for j in range(L-k+2, 1, -1):
        if L == 1 :
            continue
        print(" ",end="")

    for j in range(1, 2*k+(b-1)):
        if j == 1 or j ==  2*k+(b-2) :
            print("*",end="")
        else:
            print(" ",end="")
            if L == 1:
                print("  ",end="")

    if L <= 2 :
        print("",end="")
    print()

#DESCENTE MILIEU 2
for k in range(1, L):
    print(" ",end="")
    for j in range(1, L-k+1):
        print(" ",end="")

    for j in range(1, 2*k+(b-1)+2):
        if j == 1 or j ==  2*k+(b-2)+2 :
            print("*",end="")
        else:
            print(" ",end="")
    print()

#LIGNE BASE TRIANGLE INVERSE 
b = 0
if L == 1:
    dim = 2*L+2
elif L==2:
    dim = 2*L+1
print(" ",end="")
for j in range(1, dim):
        print("*",end="")
        b+=1
for j in range(1, 2*L):
        if j == 1 or j == 2*L-1:
            if L == 1:
                print(" ",end="")
                break
            print("*",end="")
            b+=1
        else:
            print(" ",end="")
            b+=1
for j in range(1, dim):
        print("*",end="")
print()

#POINTE TRIANGLE INVERSE
for i in range(L+1, 1, -1):
    for j in range(dim+L-i, 1, -1):
        print(" ",end="")
    for j in range(2*i, 1, -1):
        if j == 2 or j == 2*i-2:
            print("*",end="")
        else:
            print(" ",end="")

    print()
