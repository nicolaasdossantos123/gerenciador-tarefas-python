def soma_total():
    soma = 0

    while True:
        try:
            n = int(input("Digite um número (0 para sair): "))

            if n == 0:
                break

            soma += n

        except ValueError:
            print("Digite apenas números.")

    return soma

total = soma_total()
print("Soma total", total)