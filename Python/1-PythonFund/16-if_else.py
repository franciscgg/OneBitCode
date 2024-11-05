gameName = input("Digite o nome do jogo: ")
yearLaunch = int(input("Digite o ano de lançamento do jogo: "))
classification = float(input("Digite a nota de classificação do jogo: "))

if classification > 8.0 and yearLaunch > 2015:
    print(f"O jogo {gameName} é bom. Rcomendo jogá-lo")
else:
    print(f"O jogo {gameName} não antingiu uma boa nota. Por isso não recomendo")