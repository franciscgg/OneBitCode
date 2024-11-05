gameSet = {"Resident Evil 4", "Black Ops 6", "Red Dead Redemption 2", "Dayz"}

print(gameSet)

# 1 - Buscar o tamanho do set
print(len(gameSet))

# 2 -
exampleSet = {"Resident Evil 4", True, 1, 350.00} # no set o True e o 1 são o mesmo valor então não vai aparecer
print(exampleSet) # não pode repetir valores no set nem na tupla ele não deixa repetir valores

# 3 - Adicionar item de outro set
gameSet.update(exampleSet) # adiciona as informações de um set em outro set
print(gameSet)

# 4 -
gameSet.remove(True)
gameSet.remove(350.00)
print(gameSet)


# Não possibilita recuperar valores via fatiamento ou slice
