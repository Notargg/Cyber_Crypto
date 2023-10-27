import asyncio
import base64
import math
import string
from collections import Counter


englishFreq = {
    b'a':  0.08167,
    b'b':  0.01492,
    b'c':  0.02782,
    b'd':  0.04253,
    b'e':  0.1270,
    b'f':  0.02228,
    b'g':  0.02015,
    b'h':  0.06094,
    b'i':  0.06966,
    b'j':  0.00153,
    b'k':  0.00772,
    b'l':  0.04025,
    b'm':  0.02406,
    b'n':  0.06749,
    b'o':  0.07507,
    b'p':  0.01929,
    b'q':  0.00095,
    b'r':  0.05987,
    b's':  0.06327,
    b't':  0.09056,
    b'u':  0.02758,
    b'v':  0.00978,
    b'w':  0.02360,
    b'x':  0.00150,
    b'y':  0.01974,
    b'z':  0.00074,
}
if isinstance(b'a'[0], int):
    englishFreq = {x[0]: y for x, y in englishFreq.items()}

def hex2base64(hex):
    b = bytes.fromhex(hex)
    return base64.b64encode(b)

def xor(a, b):
	return bytes(i ^ j for i, j in zip(a, b))

#single-byte xor
def sxor(a, byte):
	return bytes(i ^ byte for i in a)

#retorna verdadeiro caso a string de bytes contenha apenas caracteres printaveis
def isPrintable(bytestring):
	result = True
	for char in bytestring:
		try:
			dchar = char.to_bytes().decode()
		except:
			return False
		result = result and (dchar in string.printable)
	return result


#utiliza o teste qui-quadrado para comparar a frequencia de caracteres
#de um input 'a' com a frequencia esperada na lingua inglesa
#quanto menor o qui-quadrado maior a proximidade da amostra com o esperado
def scoreFrequency(a):
	frequency = Counter(a.lower())          #gera um dicionario com caracter nas chaves e frequencia nos valores
	length = len(a)
	chi2 = 0
	for char in englishFreq:
		observed = frequency.get(char, 0)
		expected = englishFreq[char] * length
		chi2 += (observed - expected)**2 / expected
	return chi2


#challenge 1

'''
hex = ("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
b64 = hex2base64(hex)
print("hex = ", hex)
print("b64 = ", b64)
'''

#challenge 2

'''
a = bytes.fromhex("1c0111001f010100061a024b53535009181c")
b = bytes.fromhex("686974207468652062756c6c277320657965")
expected = bytes.fromhex("746865206b696420646f6e277420706c6179")
result = xor(a, b)
print("a = ", a, ", b = ", b)
print("a xor b = ", result)
print("expected = ", expected)
'''

#challenge 3

hex = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
results = [sxor(hex, byte) for byte in range(256)]
printable = {}

#seleciona apenas os resultados printaveis
for r in results:
	if isPrintable(r):
	    printable[scoreFrequency(r)] = r

#ordem crescente de qui-quadrado
printable = dict(sorted(printable.items()))

#5 menores qui-quadrados
top5 = {k: printable[k] for k in list(printable)[:5]} 

print("5 most likely results:")
for i in top5:
	print(i, top5[i])