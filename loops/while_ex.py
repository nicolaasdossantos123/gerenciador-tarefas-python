contador = 0
numero = -1


while numero != 0:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        print("Programa encerrado")

    if numero > 0:
        contador = contador + 1
        

print("Quantiedade de numeros positivos", contador)
    