"""
Trabalho realizado por:
        João Algarve
        PDM-B
        1º ano
        nº 45304
"""
#--------------------------------1--------------------------------



#--------------------------------1--------------------------------


#--------------------------------2--------------------------------



#--------------------------------2--------------------------------


#--------------------------------3--------------------------------

import math

class Calculadora:

    def soma(n1, n2):
        return print("\nResultado: ", n1 + n2)

    def subtrair(n1, n2):
        return print("\nResultado: ", n1 - n2)

    def divisao(n1, n2):
        return print("\nResultado: ", n1 / n2)

    def multiplicacao(n1, n2):
        return print("\nResultado: ", n1 * n2)

    def raiz_quadrada(n1):
        return print("\nResultado: ", math.sqrt(n1))

    def resto_div(n1, n2):
        return print("\nResultado: ", n1 % n2)

    def fatorial(n1):
        return print("\nResultado: ", math.factorial(n1))


resposta = True

while(resposta):

    print("\n------Calculadora------")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("5 - Raiz quadrada")
    print("6 - Resto da Divisão")
    print("7 - Fatorial")
    print("8 - Sair")
    print("-----------------------")

    operacao = int(input("Escolha a operação: "))

    if operacao == 1:
        n1 = float(input("\nInsira o 1º número: "))
        n2 = float(input("Insira o 2º número: "))
        Calculadora.soma(n1, n2)

    elif operacao == 2:
        n1 = float(input("\nInsira o 1º número: "))
        n2 = float(input("Insira o 2º número: "))
        Calculadora.subtrair(n1, n2)

    elif operacao == 3:
        n1 = float(input("\nInsira o 1º número: "))
        n2 = float(input("Insira o 2º número: "))
        Calculadora.divisao(n1, n2)

    elif operacao == 4:
        n1 = float(input("\nInsira o 1º número: "))
        n2 = float(input("Insira o 2º número: "))
        Calculadora.multiplicacao(n1, n2)

    elif operacao == 5:
        n1 = float(input("\nInsira o número para a raiz quadrada: "))
        Calculadora.raiz_quadrada(n1)

    elif operacao == 6:
        n1 = float(input("\nInsira o 1º número: "))
        n2 = float(input("Insira o 2º número: "))
        Calculadora.resto_div(n1, n2)

    elif operacao == 7:
        n1 = float(input("\nInsira o número para o fatorial: "))
        Calculadora.fatorial(int(n1))

    elif operacao == 8:
        resposta = False

    else:
        print("\nError operacao invalida!")
#--------------------------------3--------------------------------