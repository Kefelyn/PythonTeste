import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)

print(f'A raiz quadrada de {num} é {raiz:.2f}')

print('--------- ou ---------')

from math import sqrt
num = int(input('Digite um numero: '))
raiz = sqrt(num)

print(f'A raiz quadrada de {num} é {raiz:.2f}')

print('\n--------- números aleatórios ---------\n')

import random
num1 = random.random()

print(num1)

print('--------- ou ---------')

import random
num1 = random.randint(1,10)

print(num1)

import emoji
print(emoji.emojize("Olá, mundo :sunglasses:", language='alias'))