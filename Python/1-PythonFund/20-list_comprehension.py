# 1- Liste valores de 0 a 10 que sejam menor do que 4.
"""for i in range(10):
    if i < 4:
        print(i)"""


"""
Em uma única expressão aplicamos o for e o 
if para selecionar jogos que tenham a letra a

Sintaxe: novalista = 
[expression for item in iterable if condition == True]

"""

listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)


gameList = ["Resident Evil 4", "Black Ops 6", "Red Dead Redemption 2", "Dayz", "God Of War"]

# 2 -  Jogos que possuam a letra a

newList = [x for x in gameList if "a" in x]
print(newList)

# 3 - Jogos que eu zerei
gamesFinished = [x for x in gameList if x != "Dayz"]
print(gamesFinished)