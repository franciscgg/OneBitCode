"""
*args - Utilizamos ele quando não temos certeza de quantos argumentos queremos passar para uma função.
- Os argumentos são passados como uma tupla, o que permite que a função receba um número variável de argumentos.

**kwargs - Além dos valores, podemos passar também as respectivas chaves (nomes dos parâmetros) para cada argumento.
- Os argumentos são passados como um dicionário, onde as chaves são os nomes dos parâmetros e os valores são os valores atribuídos a esses parâmetros.
"""

# 1 - Soma de números
def sum(*num):  # Usa o * quando você não sabe quantos parâmetros vão ser passados!
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é {sum_total}")

sum(7, 7, 7)  # Aqui pode ser passado quantos parâmetros quiser, e são tratados como uma tupla.

# 2 - Apresentação de cursos
def presentation(**data): # O uso de **data é para capturar argumentos nomeados como um dicionário
    for key, value in data.items():
        print(f"{key} - {value}")  # Passado como um dicionário, onde key é o nome e value é o conteúdo.

print("#####Cursos#####")
presentation(name="Python", category="Backend", level="Iniciante")
presentation(name="Visão Computacional", category="IA", level="Avançado")
presentation(name="Dashboards com Dash", category="Data Science", level="Intermediário")
