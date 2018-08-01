'''

Author: Pranav Surampudi
Date: 01-August-2018
Encoding: Utf-8

'''
VAR_A = 24
VAR_B = 56
if isinstance(VAR_A, str) or isinstance(VAR_B, str):
    print("Strings are involved")
elif int(VAR_A) > int(VAR_B):
    print("bigger")
elif int(VAR_A) == int(VAR_B):
    print("equal")
elif int(VAR_A) < int(VAR_B):
    print("smaller")
