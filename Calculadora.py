# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação
# e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(a, b, op):
    if (op == 1):
        res = a+b

    elif (op == 2):
        res = a-b

    elif (op == 3):
        res = a*b

    else:
        res = a/b
    return res


op = int(input(
    "Qual a operacao desejada? 1. Soma, 2. Subtração, 3. Multiplicação, 4. Divisão"))
a = int(input("Qual o primeiro numero ?"))
b = int(input("Qual o segundo numero?"))

c = calculadora(a, b, op)
print("resposta = ", c)
