# 1 - Crie uma função que receba dois argumentos: o primeiro e o segundo nome
def full_name(fname, lname):
    print(f"Nome completo: {fname} {lname}")
    
full_name("Francisco", "Hélio") # deve se passar os parametros na ordem

# 2 - Crie uma função que some dois números via parâmetros
def sum(a,b):
    return a + b # return para retornar a soma de a + b

print(sum(5,7)) # paramentros passado para a soma

# 3 - Argumento defalt numa função

def address(country="Brasil"): # definindo o argumento direto
    print(f"Eu moro no {country}")
    
address() # retorna o argumento definido
address("Espanha") # retorna o argumento passado na função aqui

# 4 - Avaliação do jogo
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo:")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo: "))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum / qtdRating:.2f}")
    
rating = int(input("Digite quantas avaliações deseja fazer no jogo: "))
rating_game(rating) # retorna quantas vezes você digitar
rating_game(2) # retorna duas vezes para digitar a nota passado o parametro aqui