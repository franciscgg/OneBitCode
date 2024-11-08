"""
Fatorial de um número:

3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1
"""

# 1 - Fatorial de um número
def factorial(num):
    if num == 1:
        return 1  # Retorna 1 porque o fatorial de 1 é 1, e esse é o caso base que interrompe a recursão.
    else:
        return num * factorial(num - 1)  # Multiplica num pelo fatorial do número anterior (num - 1), até chegar ao caso base.

number = int(input("Digite o número para o fatorial: "))
print(f"O fatorial de {number} é: {factorial(number)}")

# 2 - Soma total de um número
"""
Soma total de um número:

3 -> 3 + 2 + 1
5 -> 5 + 4 + 3 + 2 + 1
"""
def total_sum(num):
    if num == 1:  # Retorna 1 porque a soma de 1 é 1, e esse é o caso base que interrompe a recursão.
        return 1
    else:
        return num + total_sum(num - 1)  # Soma num com a soma dos números anteriores (num - 1), até chegar ao caso base.

num = int(input("Digite um número para soma: "))
print(f"A soma total de {num} é: {total_sum(num)}")
