
# Autor: Gabriel Lourenço de Paula Graton
# CTF: https://github.com/alex-bellon/ctf-challenges/blob/master/2020-fall/ctf3-amongusctf/crypto-shamir-secret-sharing/prompt.md

"""

- Problema

Reconstruction

In order to reconstruct the secret, any 3 points are sufficient

Consider using the 3 points



Primeiro foi entender a concepção do problema, o que é secret sharing e como funciona.
Visto que não vimos isso em aula e poderia ser algo novo, foi pesquisado sobre o assunto e encontrado o seguinte:

https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing

Tem uma biblioteca em python que faz isso, mas não foi utilizada:

https://pypi.org/project/shamirs/

"""
# Import

import shamirs
import numpy as np


# Pontos dados
x = np.array([1, 2, 3])
y = np.array([1798644, 109600, 7492910])

p = 8602812

# Calcular o polinômio interpolador de grau 2 (polinômio de Lagrange) - Que nem na Wikipedia
coefficients = np.polyfit(x, y, 2)

# Os coeficientes retornados são na ordem decrescente de grau, ou seja, [a2, a1, a0]
a2, a1, a0 = coefficients

# O polinômio interpolador é então a0 + a1 * x + a2 * x^2 - Com isso teremos o polinômio interpolador
polinomio_interpolador = f'{a2:.6f}x^2 + {a1:.6f}x + {a0:.6f}'

print(f"Polinômio interpolador: {polinomio_interpolador}")

# Para finalizar, temos que pegar o a0 ( termo sem o x) e calcular o resto da divisão por p

flag = a0 % p

# Encontramos nossa flag
flag = int(flag)
print("utflag{" + str(flag) + "}")
