gameName = "Black Ops 6"
gameDescription = """
Black Ops 6 é um jogo de tiro em primeira pessoa (FPS),
desenvolvido pela Activision,
que possibilita jogar no modo multiplayer e campanha.
"""

# O ÍNDICE FINAL NAO INCLUI ENTAO SE É 10 CARACTERE TEM QUE SER 11 

# string [incío:fim] - índice começa na posição 0 | índice final -1

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])

# 2 - Busque toda string até a última posição
print(gameName[:11])

# 3 - Busque toda string da terceira até a última posição
print(gameName[2:])

"""
string [incío:fim] - índice começa na posição 0 | índice final -1
passo - determina o incremento. Por padrão esse número é o 1.
"""

# 4 - Busque toda a string de 2 em 2 caractares
print(gameName[::2])

# 5 - Busque toda a string nos índices ímpares
print(gameName[1::2])

# 6 - Inverter uma string de trás pra frente
print(gameName[::-1])