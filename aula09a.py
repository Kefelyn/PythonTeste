frase = 'Curso em Video Python'
frase1 = '   Curso em Video  '

print(frase[3:12])
 # Este é o FATIAMENTO, ele fatia a frase conforme os números desejados
 # Lembrando que o Python sempre ignora o último número, ou seja: "[0:6]" é na verdade até o 5 caracter°
 # E lembrando que a contagem dos caracteres se inicia em 0 e conta espaços
 # "[3:6:2]" = começa na 3° letra, vai até a 5° pulando de dois em dois
 # "[7::3]" = começa na 7° letra, vai até o final (pois não tem especificação) da frase pulando de três em três
 # "[:9]" = começa do início da frase (não tem especificação) e vai até a 8° letra da frase.
print(frase[:6])
print(frase[8::3])
print(frase[10:])

print(frase.count('o'))
# Usando o COUNT para contar quantas letras "o" tem na frase
# O Python faz diferência entre o maiúsculo e o minúsculo

print(frase.upper())
# O UPPER transforma todas as letras da frase em letras maiúsculas
print(frase.upper().count('o'))

print(frase.lower())
# O LOWER transforma todas as letras da frase em letras minúsculas

print(len(frase))
# Pode usar o LEN para saber qual é o tamanho da frase

print(frase.replace('Python', 'Android'))
# No Replace você troca uma palavra na frase por outra
# Mas não é permanente, a menos que fosse "frase = frase.replace....."

print(frase1.strip())
# O STRIP tira os espaços extremos indesejados da frases
# O RSTRIP tira os espaços extremos do lado direito (right)
# O LSTRIP tira os espaços extremos do lado esquerdo (left)
print(frase1.rstrip())
print(frase1.lstrip())

print('Curso' in frase)
# Está perguntando se a palavra "Curso" está dentro da frase

print(frase.find('video'))
# Mostra em qual posição está a palavra
# O resultado "-1" significa que a palavra não está na frase
print(frase.lower().find('video'))

print(frase.split())
# O SPLIT divide as palavras da frase de acordo com o espaçamento
# e cria uma lista com cada uma delas, colocando em cochete ([])
# Lembrando que a contagem dos itens e das letras de cada item da lista se inicia em 0
divido = frase.split()
print(divido[2][3])
# Está pedindo para pegar o item 2 da lista e mostrar a 3° letra

print("""
USANDO TRÊS ASPAS, CONSIGO ESCREVER UM TEXTO LONGO E
COM LINHAS SEPARADAS SEM PRECISAR COLOCAR O PRINT()
A CADA LINHA DE TEXTO.
""")