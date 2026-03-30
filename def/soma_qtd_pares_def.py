def soma_quantidade_pares():
    soma = 0
    quantidade = 0
    pares = 0

    while True:
        try:
            n = int(input("Digite um número (0 para sair): "))

            if n == 0:
                break

            soma += n
            quantidade += 1

            if n % 2 == 0:
                pares += 1

        except ValueError:
            print("Digite apenas números, tente novamente.")

    return soma, quantidade, pares

soma, qtd, pares = soma_quantidade_pares()

print("Soma total:", soma)
print("Quantidade de números:", qtd)
print("Quantidade de números pares:", pares)