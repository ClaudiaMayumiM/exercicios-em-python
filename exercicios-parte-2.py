# Faça um script que receba um número e retorne uma lista com todos os números pares até seu número correspondente negativo 

numero = int(input('Informe um numero: '))
pares = []

for numero in range(-numero, numero + 1):
    if numero % 2 == 0:
        pares.append(numero)
    pares.sort()

print(pares[::-1])




# Faça um script que peça um input de número inteiro ao usuário 
# E imprima 1 asterisco na primeira linha, 2 * na segunda, 3 * na terceira, até n * na N linha

numero_linhas = int(input('Informe a quantidade de linhas desejada: '))

for i in range(numero_linhas + 1):
    print(i * '*')




# Faça uma função que retorne o reverso de um número inteiro informado ex: 127 -> 721

def retorna_reverso():
    numero = int(input('Digite um número: '))
    numero_reverso = str(numero)
    print(f'O número reverso é: {numero_reverso[::-1]}')
    
retorna_reverso()




# Faça um script que receba um número e imprima na tela, por exemplo:
# Digite um número: 5
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

def imprime_nlinhas(numero):
    for i in range(1, numero + 1):
        print(f'{i} ', end = '')
    print()
        
def imprime_prox(numero):
    for numero in range(numero + 1):
        imprime_nlinhas(numero)

numero = int(input('Digite um número: '))
imprime_prox(numero)




# Em Matemática, um número perfeito é um número natural para o qual a soma de todos os seus divisores naturais próprios é igual ao próprio número.
# Faça um script que receba um número e retorne true caso ele seja perfeito ou false caso não seja

numero = int(input('Digite um número: '))

def numero_perfeito(numero):
    contador = 1
    numeros_divisores = []

    while contador < numero:
        if numero % contador == 0:
            numeros_divisores.append(contador)
        contador += 1
    return (sum(numeros_divisores) == numero)

numero_perfeito(numero)




# Faça uma função que receba um conjunto de números inteiros e retorne um dicionário, separando-os em pares e ímpares 

def par_impar():
    pares = []
    impares = []

    for numeros in range(10):
        conjunto = int(input('Digite um numero inteiro: '))
        if conjunto % 2 == 0:
            pares.append(conjunto)
        else:
            impares.append(conjunto)

    d = {}
    d['pares'] = pares
    d['impares'] = impares 
    print(d)

par_impar()




# Faça uma função que receba uma frase e retorne um dicionário contendo o número de vezes que cada palavra da frase é usada

def conta_palavras():
    frase = input('Digite uma frase: ').split()
    palavras = {}
    
    for palavra in frase:
        if palavra in palavras:
            palavras[palavra] += 1
        else:
            palavras[palavra] = 1
    print(palavras)
    
conta_palavras()