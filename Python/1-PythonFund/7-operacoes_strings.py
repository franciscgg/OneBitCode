gameDescription = """
Black Ops 6 é um jogo de tiro em primeira pessoa (FPS),
desenvolvido pela Activision,
que possibilita jogar no modo multiplayer e campanha.
"""

gameName = "Black Ops"
gameVersion = "6"
line = "="

# 1- Operação de Concatenação de Strings
print(line * 20)
gameFullName = gameName + gameVersion
print(gameFullName)

# 2 - Operação de multiplicação de Strings
print(line * 20)

# 3 - Procura palavra dentro de um texto
print("Black Ops 6" in gameDescription)
print("tiro" in gameDescription)