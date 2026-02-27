contador = 1
par = 0
impar = 0
soma = 0

while True:
    try:
        print("Digite um número (0 para sair): ")

        contador = int(input())

        if contador == 0:
            break

        elif contador % 2 == 0:
            par += 1

        elif contador % 2 != 0:
            impar += 1
        
        else:
            soma += contador

    except ValueError:
        print("Digite apenas números, tente denovo.")
        print()

print(f"\nQuantiedade de {par} números pares digitados")
print(f"\nQuantiedade de {impar} números ímpares digitados")
print(f"\nSoma total de {soma} números digitados")