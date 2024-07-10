def countChar(S: str)->str:
    '''Outputs character along with its frequency.'''
    i=1
    count=1
    prevChar = S[0]
    outS = ""
    while(i<len(S)):
        if(S[i]==prevChar):
            count+=1
        else:
            outS = outS + prevChar + str(count)
            count = 1
            prevChar = S[i]
        i+=1
    outS = outS + prevChar + str(count)
    return outS

def hexCount(S:str)->str:
    i = 0
    outS = ""
    while(i<len(S)):
        ch = S[i]
        count = int(S[i+1])
        try:
            count = count*10 + int(S[i+2])
            i+=3
        except:
            i+=2
        hexCount = hex(count)
        outS = outS + ch + hexCount[2:]
    return outS
