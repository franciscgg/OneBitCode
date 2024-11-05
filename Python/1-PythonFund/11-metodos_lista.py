gameList = ["Resident Evil 4", "Black Ops 6", "Red Dead Redemption 2", "Dayz", "God Of War", "The Last Of Us"]

# 1 - Tamanho da lista
print(len(gameList))

# 2 - Recuperar um item da lista pelo índice
print(gameList.index("Dayz")) # .index mostra o índice na lista que é 3

# 3 - Adicionar item ao final da lista
gameList.append("GTA V") # .append para incluir item ao final da lista
print(gameList)

# 4 - Ordernar a lista
gameList.sort() # .sort serve para ordenar a lista 
print(gameList) 

# 5 - Copiar os itens de uma lista para outra

gameReset = gameList.copy()
gameReset.remove("God Of War") # .remove \ remove o item da lista passando o nome
print(gameReset)

# 6 - Remove todos os itens da lista
gameList.clear()
print(gameList)

