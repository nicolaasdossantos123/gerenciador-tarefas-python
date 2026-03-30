soma = 0
impares = 0
pares = 0

print("Digite 5 números:")

for i in range(1, 6):
    while True:
        try:
            numero = int(input(f"{i}º número: "))
            break   
        except ValueError:
            print("Erro: digite apenas números inteiros.")

    soma += numero

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\n===== RESULTADO =====")
print("Quantidade de números ímpares:", impares)
print("Quantidade de números pares:", pares)
print("Soma total:", soma)