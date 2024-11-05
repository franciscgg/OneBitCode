import pprint # uma maneira mais organizada e legível de imprimir estruturas de dados complexas

gamesDict = {
    "Resident Evil 4":{
        "yearLaunch": 2024,
        "classification": 9.9,
        "genre": ["Ação", "Aventura"] # lista
    },
    "Black Ops 6":{
        "yearLaunch": 2024,
        "gamePrice": 350.00,
        "classification": 9.5,
        "genre": ["Ação", "Tiro"] # lista
    },
    "Red Dead Redemption 2":{
        "yearLaunch": 2018,
        "gamePrice": 300.00,
        "classification": 10.0,
        "genre": ["Ação", "Tiro"] # lista
    }
}

pp = pprint.PrettyPrinter(depth=4) # formatação do pprint
pp.pprint(gamesDict)

# 1 - Buscando informação dentro de um dicionário
print(gamesDict["Black Ops 6"]["genre"]) # buscou a informação passando o parametro do nome da 'dict' que foi o 'Black Ops 6'

# 2 - Adicionando novo item
gamesDict["Red Dead Redemption 2"]["players"] = 1 # passa o primeiro parameto do dict que foi o nome do jogo depois passa o parametro a ser incluir naquele dicionario
print(gamesDict["Red Dead Redemption 2"])

# 3 - Excluir um dicionario
del gamesDict["Resident Evil 4"] # del para exluir um dicionario
pp.pprint(gamesDict)