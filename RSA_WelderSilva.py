__authors__ = 'Carlos Daniel Almeida Gomes & Welder Paulo da Silva'

import random
from math import gcd

# Lista cripto tudo que esta nela é mensagem criptografada
cripto = []

# Lista decripto é ond esta mensagem decriptografada
decripto = []

# Lista lista_e onde é armazenado valores para selecionar o E
lista_e = []
# Lista para armazenar primos e escolher aleatórimente valores de P e Q
primo_pq = []

s = input("Digite um texto para Criptografar:")

# Percorrendo lista s e tranformando os caracteres digitados em código ASCII usando a função ord
txt = [ord(x) for x in s]

# P e Q numeros primos gerados automaticamente
for numero in (i + 2 for i in range(100)):

    if (numero % 2 != 0) and (numero % 3 != 0) and (numero % 5 != 0) and (numero % 7 != 0):

        primo_pq.append(numero)
primo_pq.append(2)
primo_pq.append(3)
primo_pq.append(5)
primo_pq.append(7)


P = random.choice(primo_pq)
Q = random.choice(primo_pq)

# Calculo do produto de P e Q
N = P * Q

# Definiçao phiN
phiN = (P - 1) * (Q - 1)

# Chave publica E gerada a partir da condição onde E tem que ser maior que 1 e menor que Phi(N), e também ser primo entre Phi(N).Os valores que atendem essa condição são armazenados na lista_e, e posteriormente usando a função random.choice é escolhido um valor da lista aleatóriamente para ser o valor E.
for i in range(phiN):
    primo = gcd(i, phiN)
    if (i > 1) and (i < phiN) and (primo == 1):
        lista_e.append(i)
E = random.choice(lista_e)

# Definicao chave privada D, fazendo calculo inverso modular
D = pow(E, phiN -1, phiN)

# Criptografa a  mensagem
for i in txt:
    C = (i ** E) % N
    cripto.append(C)
print(cripto)

# Print valor criptografado
print(''.join(chr(i) for i in cripto))

# Descriptografa mensagem
for i in cripto:
    C = (i ** D) % N
    decripto.append(C)
print(decripto)
# Print valor descriptografado
print(''.join(chr(i) for i in decripto))

