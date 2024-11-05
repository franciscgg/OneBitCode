num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operation = input("Digite a operação a realizar: (+ - * /): ")


if operation == "+":
    soma = num1 + num2
elif operation == "-":
    soma = num1 - num2
elif operation == "*":
    soma = num1 * num2
elif operation == "/":
    soma = num1 / num2
else:
    print("Digite uma operação válida!")
    soma = 0
print(f"Resultado é: {soma:.2f}")    

