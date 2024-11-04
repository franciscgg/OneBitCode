gameName = "Black Ops 6"
gameDescription = """
Black Ops 6 é um jogo de tiro em primeira pessoa (FPS),
desenvolvido pela Activision,
que possibilita jogar no modo multiplayer e campanha.
"""

print(gameName.upper()) # Retornar a string em maiúsculo
print(gameName.lower()) # Retornar a string em minúsculo
print(gameName.capitalize()) # Apenas a primeira letra em maiúsculo
print(gameName.title()) # Apenas a primeira letra em maiúsculo
print(gameName.center(15, "-")) # Retorna a string  centralizada com caractere de preenchimento
print(gameName.find("a")) # Retorna a posição do caractere
print(gameDescription.count("a")) # Conta os caracteres
print(gameDescription.replace("Black Ops 6", "CS:GO")) # Altera um elemento por outro
print(gameDescription.split(",")) # Pode quebrar em partes menores para ter um mapeamento melhor