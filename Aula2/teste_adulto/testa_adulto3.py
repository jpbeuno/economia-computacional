"""
Programa testa_adulto3.py
Descrição:
Faça um programa que pergunte a idade de uma pessoa. Se a
idade for menor que 13 anos, imprima na tela "Oi! Você é uma
criança.". Se idade for de 13 a 17, imprima "Oi, Você é um
adolescente.". Se a idade maior que 17 anos imprima "Oi! Você
é um adulto.".

Autor: João Pedro Bueno
Data: 02/04/2025
Versão: 0.0.3

"""

# Alocação de memória

idade = 0

frase = ""

# Entrada de dados

idade = int(input("Qual é a sua idade?"))

# Processamento de dados
if idade < 13:
    frase = "Oi! Você é uma criança."
elif idade >= 13 and idade < 17:
    frase = "Oi, Você é um adolescente."
else:
    frase = "Oi! Você é um adulto."

# Saída de dados

print(frase)