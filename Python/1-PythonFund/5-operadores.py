num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

#Aritméticos

sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"Soma:{sum}\nSubtração: {sub}\nDivisão: {div}\nMultiplicação: {mult}\nResto da divisão: {mod}\nPotência do número: {exp}")

#Comparação 

bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"Os números {num1} e {num2} são iguais? {equal}\nO número {num1} e {num2} é maior ou igual a {num2}? {bigger_equal}")

#Atribuição

num1 += 1 # num1 = num1 + 1
num1 -= 1 # num1 = num1 - 1
num1 *= 1 # num1 = num1 * 1
num1 /= 1 # num1 = num1 / 1
