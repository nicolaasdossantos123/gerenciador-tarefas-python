compras = []

while True:
    print("\n===== COMPRAS =====")
    print("1 - Adicionar item")
    print("2 - Ver lista")
    print("3 - Remover item")
    print("4 - Sair")

    try:
        opcao = int(input("Digite uma opção: "))
    
        if opcao == 1:
            item = input("Digite seu item: ")
            compras.append(item)

        elif opcao == 2:
            if not compras:
                print("Lista vazia")

            else:
                for numero, item in enumerate(compras):
                    print(numero + 1,"-", item)

        elif opcao == 3:
            numero = int(input("Digite um número da lista para remover:" ))
            
            indice = numero - 1

            if 0 <= indice < len(compras):
                compras.pop(indice)
                print("Item removido com sucesso:", indice)
            else:
                print("Esse item não existe")

        elif opcao >= 5:
            print("Opcão inválida")
            

        elif opcao == 4:
            break 

    except ValueError:
        print("Digite apenas números, tente novamente")       