def simular_banco():
    nome = input("Digite seu nome: ")
    print(f"Bem-vindo ao banco da Rayane, {nome}")
    
    deposito = float(input("Digite o valor que você deseja depositar: "))
    saldo = 0.0
    saldo += deposito
    print(f"Seu saldo atual é de: R${saldo:.2f}")
    
    saque = float(input("Digite o valor que você deseja sacar: "))
    if saque > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= saque
        print(f"Seu saldo atual é de: R${saldo:.2f}")
    
    print(f"Obrigado por usar o banco da Rayane, {nome}, volte logo para o banco ficar mais rico")

simular_banco()
