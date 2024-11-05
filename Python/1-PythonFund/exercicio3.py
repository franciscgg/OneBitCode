# Cálculo da Distância
distancia = float(input("Digite a distância que irá percorrer em KM: "))

if distancia <= 200:
    calculo_distancia = distancia * 0.50
else:
    calculo_distancia = distancia * 0.35
    
print(f"Será cobrado pela sua viagem de {distancia:.0f} KM, o valor de R${calculo_distancia:.2f}")

# Aumento salário funcionário
salario = float(input("Digite o seu sálario: "))
salarioFixo = 1250.00

if salario > salarioFixo:
    salario_aumento = (salario * 0.10) + salario
else:
    salario_aumento = (salario * 0.15) + salario
    
print(f"O seu sálario atual era de R${salario:.2f} e com aumento ficou R${salario_aumento:.2f}")