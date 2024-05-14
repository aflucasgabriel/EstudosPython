menu = """
================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
================

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input("Digite um valor para depositar:\n=> "))

        if valor_deposito > 0:
            saldo += valor_deposito

            print(f"\nDeposito de R$ {valor_deposito:.2f} realizado com sucesso!")
            extrato += f"Deposito de R$ {valor_deposito:.2f}\n" 

        elif valor_deposito < 0:
            print("Valor precisa ser positivo!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 's':
        if LIMITE_SAQUES > 0:
            valor_saque = float(input("Digite um valor para sacar: \n=> "))

            if valor_saque <= limite and valor_saque <= saldo:
                saldo -= valor_saque
                LIMITE_SAQUES -= 1
                numero_saques += 1
                extrato += f"Saque de R$ {valor_saque:.2f}" 
            else:
                print("Limite de saque ultrapassado ou saldo insuficiente!")


        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 'e':
        if extrato == "":
            print("Nao foram realizados depositos ou saques!")
            print(f"Saldo: R$ {saldo:.2f}")

        else: 
            extrato_final = f'''
        ================EXTRATO================
        {extrato}
        \nSaldo: R$ {saldo:.2f}
        =======================================
        '''
        print(extrato_final)        

    elif opcao == 'q':
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
