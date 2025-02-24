print('\033[1;30;45mOlá, mundo!\033[m')
#colocar \033[m pra não pegar a linha inteira, mas apenas a frase

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[30:107m',
         'cinzaeroxo':'\033[37:45m'}

nome = 'Vitoria'
print(f'{cores['cinzaeroxo']}Olá! Muito prazer em te conhecer,{cores['limpa']} \033[1;30;45m{nome}\033[m')

# \033[style;text;back(letra "m" no final)
# style = 0 é padrão, 1 é negrito, 4 é sublinhado e 7 é negativo
# text \\ back (abaixo)
# 30 \\ 40 = preto
# 31 \\ 41 = vermelho
# 32 \\ 42 = verde
# 33 \\ 43 = amarelo
# 34 \\ 44 = azul
# 35 \\ 45 = roxo
# 36 \\ 46 = ciano
# 37 \\ 47 = cinza
# 97 \\ 107 = branco