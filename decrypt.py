def decCount(S:str)->str:
    i=0
    outS = ""
    while(i<len(S)):
        ch = S[i]
        hexCount = S[i+1]
        count = int(hexCount, 16)
        outS = outS + ch + str(count)
        i+=2
    return outS

def addChar(S:str)->str:
    i=0
    outS = ""
    while(i<len(S)):
        ch = S[i]
        count = int(S[i+1])
        try:
            count = count*10 + int(S[i+2])
            i+=3
        except:
            i+=2
        for j in range(count):
            outS += ch
    return outS
