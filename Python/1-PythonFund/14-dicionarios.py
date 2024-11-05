gameCod = {
    "name": "Black Ops 6",
    "yearLaunch": 2024,
    "gamePrice": 350.00,
    "classification": 9.5,
    "genre": ["Ação", "Tiro"] # Dicionario com lista
}

print(gameCod)
print(len(gameCod))
print(type(gameCod))

# 1 - Recuperar um elemtno do dicionario
print(gameCod["genre"]) # [] pega o elemento do dicionario
print(gameCod.get("classification")) # .get pega o elemento do dicionario

# 2 - Buscar apenas as chaves no dicionario
print(gameCod.keys()) # .keys retorna apenas as chaves (dict_keys) que são 'name' 'yearLaunc' 'gamePrice' 'classification' 'genre'

# 3 - Buscar apenas os valores do dicionario

print(gameCod.values()) # .values retorna apenas os valores dentro das (dict_keys)

# 4 - Buscar itens do dicionario com chave e valor
print(gameCod.items()) # retona os itens com chave e valor retorando em formato de tupla

# 5 - Adicionar itens no dicionario 
gameCod["players"] = 100 # adicionar itens no dicionario 
print(gameCod)

# 6 - Atualizar itens no dicionario
gameCod.update({"players": 1}) # .update no dicionario mudou o valor de 100 para 1 usando o .update
print(gameCod)

# 7 - Remover item no dicionario
gameCod.pop("players") # .pop usado para remover um item do dicionario
print(gameCod)