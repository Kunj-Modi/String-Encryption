from ioFunc import *
from encrypt import *
from decrypt import *

# def reverseString(S: str)->str:
#     return S[::-1]

reverseString = lambda S: S[::-1]

cont = True

# main loop
while(cont):
    user = input("Encrypt - 0\nDecrypt - 1\nExit - 2: ")

    if (user == "0"):
        # input
        S = takeInputString()

        # encrypt
        S = countChar(S)

        S = hexCount(S)

        S = reverseString(S)

        # output
        giveOutputString(S)

    elif (user == "1"):
        # input
        S = takeInputString()

        # decrypt
        S = reverseString(S)

        S = decCount(S)

        S = addChar(S)

        # output
        giveOutputString(S)

    elif (user == "2"):
        cont = False
    
    else:
        print("Wrong input")
