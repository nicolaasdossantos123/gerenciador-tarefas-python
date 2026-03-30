def soma_total():
    soma = 0
    quantidade = 0

    while True:
        try:
            numero = int(input("Digite um número (0 para sair): "))

            if numero == 0:
                break

            soma += numero
            quantidade += 1

        except ValueError:
            print("Digite apenas números, tente novamente.")

    return soma, quantidade

total, qtd = soma_total()

print("Soma total dos números:", total)
print("Quantidade de números digitados:", qtd)