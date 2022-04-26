# Faça um  script que receba o valor do salário do colaborador e retorne o valor do salário antes do reajuste, o valor do salário reajustado, o percentual de aumento e o valor do aumento aplicado.
# Considere:
# Salários até $2800 -> 20% reajuste
# Salários até $7000 -> 15% reajuste
# Salários até $15000 -> 10% reajuste
# Outros valores -> 5% reajuste


salario = float(input('Digite o valor do salario atual: '))

if salario <= 2800.0:
    percentual = 20
elif salario <= 7000.0:
    percentual = 15
elif salario <= 15000.0:
    percentual = 10
else:
    percentual = 5

print(f'O valor do salario antes do reajuste é R${salario}.')
print(f'O percentual de aumento é de {percentual}%.')

percentual = percentual / 100
aumento = salario * percentual
salario_reajustado = salario + aumento 

print(f'O valor do aumento aplicado é R${aumento}.')
print(f'O valor do salário reajustado é R${salario_reajustado}.')



# Faça um script que receba um número e retorne o valor dos números somados entre si sequencialmente 

numero = int(input('Digite um número: '))
soma = 0 
contador = 1

while contador <= numero:
    soma = soma + contador 
    contador = contador + 1 
print(f'O valor dos números somados entre si sequencialmente é: {soma}.')



# Faça um script que receba X números (enquanto os números informados forem diferentes de 0) e retorne a soma dos números informados

numero = int(input('Digite um número: '))
soma = 0

while numero != 0:
    soma += numero
    numero = int(input('Digite um número: '))
  
print(f'A soma dos números informados é {soma}.')



# Faça um script que receba um número e retorne a quantidade de divisores desse número, assim como quais são eles

numero = int(input('Digite um número: '))
contador = 1
numeros_divisores = []

while contador <= numero:
    if numero % contador == 0:
        numeros_divisores.append(contador)
    contador += 1

print(f'A quantidade de divisores de {numero} é {len(numeros_divisores)}')
print(numeros_divisores)



# Faça um script que receba 10 números e devolva duas listas: uma com os números ímpares e outra com os números pares 

pares = []
impares = []

for numeros in range(10):
    conjunto = int(input('Digite um numero inteiro: '))
    if conjunto % 2 == 0:
        pares.append(conjunto)
    else:
        impares.append(conjunto)

print(f'São pares: {pares}!')
print(f'São ímpares: {impares}!')



# Faça um script que retorne o valor do fatorial do número informado

numero = int(input('Digite um número para verificar o seu fatorial: '))

fatorial = 1

for i in range(1, numero + 1):
    fatorial = fatorial * i 

print('O fatorial de', numero, 'é', fatorial)