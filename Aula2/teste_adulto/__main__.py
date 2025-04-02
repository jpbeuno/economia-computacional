"""
Programa testa_adulto2.py
Descrição: 
Faça um programa que pergunte a idade de uma pessoa e, se esta
for maior que ou igual a 18 anos, imprima na tela "Oi! Você é
um adulto.". Caso contrário, imprima "Oi! Você é menor de idade."

Autor: João Pedro Bueno
Data: 02/04/2025
Versão: 0.0.2
"""

# Alocação de memória

idade = 0

frase = ""

# Entrada de dados

idade = int(input("\nQual a sua idade?"))

# Processamento de dados

if idade >= 18:
    frase = "Oi! Você é um adulto"
else:
    frase = "Oi! Você é menor de idade"

# Saída de dados

print(frase)