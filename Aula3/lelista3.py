""" 
Programa: lelista3
Descrição: Escreva um código para ler 3 números inteiros de um usuário e guarde-os em uma lista
Autor: João Pedro Martins Bueno
Data: 16/04/2025
Versão: 0.0.1
"""

# Com repetição manual
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número:" ))
n3 = int(input("Insira o terceiro número: "))

lista = [n1, n2, n3]

print(lista)

# Com repetição automática
i = 0

numeros = [0,0,0]

while i<3:
    numeros[i] = int(input(f"Digite o número {i+1}: "))
    i = i+1
print(numeros)    