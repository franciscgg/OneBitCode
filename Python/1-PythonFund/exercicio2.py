# Substituindo caractere repetido
gameName = "Fifa 24"

character = gameName[0].lower() # para retornar todo o nome em minúsculo
new = gameName.replace("f" , "$") # faz a troca da letra 'f' por '$'
new = character + new[1:]  # Junta o primeiro caractere original em minúsculo com o restante modificado, a partir do índice 1
print(new) # Exibe o resultado final

# Invertendo a ordem dos caracteres

# definindo o valor das strings
str1 = "abc" 
str2 = "xyz"

new_str1 = str1[:2] + str2[2:]  # Pega os caracteres de índice 0 e 1 de 'abc' e junta com o último caractere de 'xyz' (índice 2)
new_str2 = str2[:2] + str1[2:]  # Pega os caracteres de índice 0 e 1 de 'xyz' e junta com o último caractere de 'abc' (índice 2)

print(new_str1) # Exibe o resultado final
print(new_str2) # Exibe o resultado final