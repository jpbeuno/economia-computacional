""" 
Programa: lelista3
Descrição: Escreva um código para ler 3 números inteiros de um usuário e guarde-os em uma lista
Autor: João Pedro Martins Bueno
Data: 16/04/2025
Versão: 0.0.2
"""

# Alocação de memória

i = 0

numeros = []

# Entrada de dados

while i<3:
    numeros.append(int(input(f"\nDigite o número {i+1}: ")))
    i = i+1

# Saída de dados
print(numeros)    