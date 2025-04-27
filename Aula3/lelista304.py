"""
Programa: lelista3
Descrição: Escreva um código para ler 3 números inteiros de um usuário e guarde-os em uma lista
Autor: João Pedro Martins Bueno
Data: 16/04/2025
Versão: 0.0.4
"""

i = 0

numeros = []

for i in range(3):
    numeros.append(int(input(f"\nDigite o número {i+1}: ")))

print(numeros)  