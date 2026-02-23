usuario_cadastrado = "ithalo"
senha_cadastrada = "4444"

tentativas = 0
logado =False

saldo = 0
limite_saque_diario = 1000
total_depositado = 0
total_sacado = 0
qtd_operacoes = 0


while tentativas <3:
    usuario = input("Digite seu usuário:")
    senha = input("Digite sua senha:")

    if usuario == usuario_cadastrado and senha == senha_cadastrada:
        print("Login realizado com sucesso!")
        logado = True
        break
    else:
        tentativas += 1
        print(f"Usuário ou senha incorretos! Tentativa {tentativas}/3")
    if not logado:
        print("Muitas tentativas inválidas.Sistema bloqueado!")
    
while True:
    print("\n=== Banco Python ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Resumo da conta")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        print(f"Seu saldo é: R$ {saldo:.2f}")

    elif opcao == "2":
        deposito = float(input("Digite o valor do depósito: R$ "))
        if deposito > 0:
            if deposito > 500:
                print("Atenção: valor de depósito muito alto!") 
            saldo += deposito
            total_depositado += deposito
            qtd_operacoes += 1
            print(f"Depósito realizado! Novo saldo: R$ {saldo:.2f}")
        else:
            print("Valor inválido! Informe um valor positivo. ")

    elif opcao =="3":
        saque = float(input("Digite o valor do saque: R$ "))
        if saque > 0:
            if saque > limite_saque_diario:
                print(f"Atenção: o valor ultrapassa o limite diário de R$ {limite_saque_diario:.2f}!")
            if saque >500:
                print("Atenção: valor de saque muito alto")
            elif saque <=saldo:
                saldo -= saque
                total_sacado += saque
                qtd_operacoes += 1
                print(f"Saque realizado! Novo saldo : R$ {saldo:.2f}")
            else:
                print("Saldo insuficiente!")
        else:
            print("Valor inválido! Informe um valor positivo.")

    elif opcao =="4":
        print("\n=== Resumo da Conta===")
        print(f"Saldo atual; R$ {saldo:.2f}")
        print(f"Total depositado: R$ {total_depositado:.2f}")
        print(f"Total sacado : R$ {total_sacado:.2f}")
        print(f"Quantidades de operações: {qtd_operacoes}")
    
    elif opcao =="5":
        print("Obrigado por usar Bando Phython. Até logo!")
        break
    else:
        print("Opção inválida! Escolha novamente.")

