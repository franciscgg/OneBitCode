# 1 - Função para imprimir Hello World
def wellcome():
    print("Hello World")
    
    
wellcome()

# 2 - Função para somar dois números
def sum():
    #print(5 + 4)
    return 5 + 4 # quando se return precisa usar o print para mostrar
    
    
print(sum())

# 3 - Função para cadastrar um jogo
def create_game(): # funções são utilizadas para não duplicar códigos
    name = input("Digite o nome do jogo: ")
    yearLaunch = int(input("Digite o ano de lançamento do jogo: "))
    gamePrice = float(input("Digite o preço do jogo: "))
    noteRating = float(input("Digite a nota de avaliação do jogo: "))
    
    print(f"{name} - R${gamePrice:.2f}")
    
create_game()