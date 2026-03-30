def contar_pares_impares():
    pares = 0
    impares = 0

    try:
        while True:
            numero = int(input("Digite um número (0 para sair): "))

            if numero == 0:
                break

            if numero % 2 == 0:
                pares += 1
            
            else:
                impares += 1

    except ValueError:
        print("Digite apenas números, por favor.")
    
    return pares, impares

pares, impares = contar_pares_impares()

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)