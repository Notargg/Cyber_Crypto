
# Autor: Gabriel Lourenço de Paula Graton
# CTF: https://github.com/alex-bellon/ctf-challenges/blob/master/2020-fall/ctf1-introctf/crypto-custom-sub-cipher/prompt.md

"""

- Problema

🦈🎩👽👀🤠👾{👽🤠🎩🤠👀_🤠👀👽🤠👀👽🤠_👽👀🦈👽👽}

I came across these ancient runes; they must have a very deep meaning behind them...

Sabemos que a flag começa com "utflag{", então podemos usar isso para descobrir o resto da flag.


Bastante Simples, o problema inicial é somente lembrar a forma como está escrita a chave e dela fazer um dicionário para substituir os emojis pelas letras.

🦈 = u
🎩 = t
👽 = f
👀 = l
🤠 = a
👾 = g

"""


# Função para substituir os emojis para letras

def emoji_to_letra(texto):
    texto = texto.replace('🦈', 'u')
    texto = texto.replace('🎩', 't')
    texto = texto.replace('👽', 'f')
    texto = texto.replace('👀', 'l')
    texto = texto.replace('🤠', 'a')
    texto = texto.replace('👾', 'g')
    return texto

# Carregamento da mensagem

mensagem = "🦈🎩👽👀🤠👾{👽🤠🎩🤠👀_🤠👀👽🤠👀👽🤠_👽👀🦈👽👽}"
flag = emoji_to_letra(mensagem)

print("Mensagem :", mensagem)
print("Flag:", flag)