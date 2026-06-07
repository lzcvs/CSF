import math

from art import *


def fatorial(n1: int):
    resultado = 1
    for n in range(1, n1 + 1):
        resultado *= n
    return resultado


def realizar_calculo(n1: float, op: str, n2: float):
    if op == "!":
        return fatorial(int(n1))
    if op == "+":
        return n1 + n2
    if op == "-":
        return n1 - n2
    if op == "*":
        return n1 * n2
    if op == "/":
        return n1 / n2 if n2 != 0 else "Erro: Divisão por zero."
    return "Operador inválido."


def calculadora():
    while True:
        try:
            num1 = float(input("\nDigite o primeiro número: "))
            operador = input("Digite o operador (+, -, *, /): ")
            if operador == "!":
                resultado = fatorial(int(num1))
                print(f"Resultado: {resultado}")
            num2 = float(input("Digite o segundo número: "))
            resultado = realizar_calculo(num1, operador, num2)
            print(f"Resultado: {resultado}")
            print(
                "--Caso queira sair pressione 'q' para sair, ou enter para continuar--"
            )
            saida = input()
            if saida == "q":
                break
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


def funcafim():
    print("insira as variaveis a, b")
    a = int(input())
    b = int(input())

    print(a, b)


def funcqrdt():
    while True:
        try:
            print("Insira as variaveis a, b e c:")
            var_a = float(input())
            var_b = float(input())
            var_c = float(input())

            delta = pow((-var_b), 2) - (4 * var_a * var_c)
            print(f"O delta é: {delta}")
            if delta < 0:
                print("Error: Delta negativo")
            elif delta > 0:
                x1 = -(var_b) + math.sqrt(delta)
                x2 = -(var_b) - math.sqrt(delta)
                final1 = x1 / (2 * var_a)
                final2 = x2 / (2 * var_a)
                print(f"x': {final1:.2f} \nx'': {final2:.2f}")

            print("---Caso queira sair pressione 'q', ou enter para continuar---")
            saida = input()
            if saida == "q":
                break
        except ValueError:
            print("Entrada invalida! Tente novamente")


# def fatoracao


def main():
    while True:
        tprint("CALC", font="sub-zero")
        tprint("    Super Fudida", font="fire_font-s\n")
        print("--OPÇÕES--")
        print("1. Calculadora")
        print("2. Função Quadratica")
        print("3, Função Afim")
        print("4. exit")
        escolha = int(input())
        if escolha == 1:
            calculadora()
        elif escolha == 2:
            funcqrdt()
        elif escolha == 4:
            print("Tchau!")
            break


main()
