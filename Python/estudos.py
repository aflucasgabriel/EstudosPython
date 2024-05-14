MAIOR_IDADE = 85

if MAIOR_IDADE < 16:
    print("Nao pode votar!")
elif (MAIOR_IDADE >= 16) and (MAIOR_IDADE <= 60):
    print("Pode votar!")
else:
    print("Não é obrigado votar")        


texto = input("Digite um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
        print()

