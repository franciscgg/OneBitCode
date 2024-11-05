gamesTuple = ("Resident Evil 4", "Black Ops 6", "Red Dead Redemption 2", "Dayz")

#name = ("Francisco",) # continua sendo string se não tiver a , a partir do momento que coloca a virgula se torna uma tupla
#print(type(name))
print(gamesTuple)
print(type(gamesTuple))

# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuple[:2])

# 2 - Buscar o último item da lista
print(gamesTuple[-1])

# 3 - Buscar jogos até uma determinada posição
print(gamesTuple[:3])

# 4 - Buscar jogos de uma posição em diante
print(gamesTuple[2:])

# 5 - Recuperar um item da tupla pelo índice
print(gamesTuple.index("Black Ops 6"))



# Não possibilita adicionar valores na tupla
# Não possibilita remover valores na tupla
# Não possibilita ordenar valores na tupla
# não pode repetir valores no set nem na tupla ele não deixa repetir valores