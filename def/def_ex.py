def contar_pares():
    contador = 0
    soma = 0
    
    while True:
        try:
            numero = int(input("Digite um número (0 para sair): "))

            if numero == 0:
                break

            soma += numero
            contador += 1

        except ValueError:
            print("Digite apenas números, tente novamente.")

    return soma, contador
    
    