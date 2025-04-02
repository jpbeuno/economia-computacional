"""Programa testa_adulto.py
Descrição:
Faça um programa que pergunte a idade de uma pessoa. Se a idade
for maior do que 18 anos, o programa imprime na tela o texto
"Oi, você é um adulto".
Autor: João Pedro Bueno
Data: 02/04/2025
Versão: 0.0.1
"""

# Alocação de memória

idade = 0

texto = "Oi, você é um adulto!"

# Entrada de dados

idade = int(input("Qual a sua idade?")) 
# int server para ler apenas números inteiros

# Processamento de dados

if idade > 18:
    print(texto)