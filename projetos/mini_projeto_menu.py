opcao = 1

while opcao != 0:
    print("\n===== MENU =====")
    print("1 - Somar dois números")
    print("2 - Contar números positivos")
    print("3 - Contar números pares")
    print("4 - Contar números ímpares")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite seu segundo número: "))
        print("Soma", a + b)

    elif opcao == 2:
        contador = 0
        numero = -1

        while numero != 0:
            numero = int(input("Digite seu número (0 para sair) "))
            if numero > 0:
                contador += 1

    elif opcao == 3:
        contador = 0
        numero = -1

        while numero != 0:
            numero = int(input("Digite um número (0 para sair): "))
            if numero > 0 and numero % 2 == 0:
                contador += 1
        print("Quantiedade de números pares", contador)

    elif opcao == 4:
        contador = 0
        numero = -1

        while numero != 0:
            numero = int(input("Digite um número (0 para sair): "))
            if numero > 0 and numero % 2 != 0:
                contador += 1
        print("Quantiedade de números ímpares", contador)

        
    elif opcao == 0:
        print("Programa encerado.")
    
    else:
        print("Opção inválida. Tente novamente.")


