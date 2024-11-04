name = input("Digite o nome do jogo: ")
yearLaunch = int(input("Digite o ano de lançamento do jogo: "))
gamePrice = float(input("Digite o preço do jogo: "))
planIncluded = bool(input("Está incluso no serviço mensal? "))


print(f"###Dados do Jogo###\n====================\nNome do jogo: {name}\nAno de lançamento: {yearLaunch}\nPreço do Jogo: {gamePrice}\nEstá incluso no serviço? {planIncluded}")