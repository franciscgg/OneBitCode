gameList = ["Resident Evil 4" , "God Of War", "Black Ops 6" , "Dayz"]

# 1 - Quando a condição for atendida, o loop será encerrado
for game in gameList: # foi passado para game a gameList 
    print(game)
    
# 2 - Quando a condição for atendida, o loop vai para a próxima iteração
for game in gameList:
    if game == "Black Ops 6":
        break # encerra o loop 
    print(game)
    
# 3 - Avaliação Jogo
for game in gameList:
    if game == "Black Ops 6":
        continue # quando for acionado ele pula para próxima interação sendo assim ecluindo o qual foi passado no parametro
    print(game)
    
gameName = input("Digite o nome do jogo: ")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo: "))

soma = 0 # para iniciar em 0
for i in range(gameRating): #parametro foi o gameRating o valor digitado dentro dele será o limite do for
    note = float(input("Digite a nota para o jogo: ")) #input para digitar as notas na quantidades de vezes que foi digitada no 'gameRating'
    soma += note
print(f"Média de avaliação do jogo {gameName} é {soma/gameRating}:.2f")

# Exemplo de for
'''for i in range(5): # passado para ter o limite
    print("Hello World")'''