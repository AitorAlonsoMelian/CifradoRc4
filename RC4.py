# Práctica 2 - Cifrado RC4
# Autor: Aitor Alonso Melián
# Asignatura: Seguridad en Sistemas Informáticos

def KSA(key): # Key Scheduling Algorithm
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    return S
    
def PRGA(S, size): # Pseudo-random generation algorithm
    i = 0
    j = 0
    key=[]

    while size > 0:
        size = size-1
        i = (i+1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        key.append(K)
    return key


def main():
    key = input("Introduzca la clave: ")
    Text = input("Introduzca el texto: ")
    print()
    S = KSA(key)
    keystream = PRGA(S, len(Text))

    asciText = []
    for i in range(len(Text)):
        asciText.append(ord(Text[i]))

    cifrado = []
    for i in range(len(Text)):
        cifrado.append(asciText[i] ^ keystream[i])
    print("Cifrado en Decimal: ", cifrado)
    
    cifradoHex = [] 
    for i in range(len(cifrado)):
        cifradoHex.append(hex(cifrado[i]))
    print("Cifrado en Hexadecimal: ", cifradoHex)


main()