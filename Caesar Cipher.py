
def ceasarCipher(sent, move):


    lower = []
    upper = []
    result= ""


    for i in range(0,len(sent)):
        if sent[i] == ' ':
            result += sent[i]
        else:
            if sent[i].isupper():
                a = ord(sent[i])
                b = chr((a + move-65)%26+65)
                result += b
            else:
                a = ord(sent[i])
                b = chr((a + move-97)%26+97)
                result += b
    print(result)

ceasarCipher("To jest przykladowy tekst", 1)