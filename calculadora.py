numero1 = float(input("Primeiro número: "))
numero2 = float(input("Segundo número: "))
operacao = input("Qual a operação? (+, -, *, /): ")
if operacao == "+":
    print(numero1 + numero2)
elif operacao == "-":
    print(numero1 - numero2)
elif operacao == "*":
    print(numero1 * numero2)
elif operacao == "/":
    print(numero1 / numero2)
else:
    print("Operação inválida")