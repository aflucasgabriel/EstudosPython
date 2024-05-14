lista = list(range(4))

print(lista)


for numero in range(0, 51, 5):
    print(numero, end= " ")

    

opcao = -1

while opcao != 0:
    opcao = int(input("\n[1] - Sacar \n[2] - Depositar \n[0] - Sair: \nOpcao: " ))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Depositando...")
