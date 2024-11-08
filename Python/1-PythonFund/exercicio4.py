import winsound
# Lançamento Foguete

for i in range(10,0,-1):
    print(i)
winsound.Beep(2500, 500)


# Tabuada

num1 = int(input("Digite qual tabuada você quer exemplo(1,2,3...): "))
num2 = int(input("Digite até qual número você quer ver a tabuada exemplo(10,11,12...): "))
soma = 1


while soma <= num2:
    tabuada = num1 * soma
    print(f"{num1} x {soma} = {tabuada}")
    soma += 1


for i in range(1, num2 + 1):
    tabuada = num1 * i
    print(f"{num1} x {i} = {tabuada}")
