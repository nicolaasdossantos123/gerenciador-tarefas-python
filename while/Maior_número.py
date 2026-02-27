maior= None #Em vez de usar -999999, use None (mais elegante e seguro)

print("Digite números inteiros (digite 0 para parar):")

while True:
    try:
        numero = int(input())

        if numero == 0:
            break

        if numero > maior: #Comparação para achar o maior
            maior = numero
    except ValueError:
        print("Por favor, digite apenas números inteiros")

if maior == None:
    print("\nNenhum número foi digitado, Tente novamente")
else:
    print(f"\nO maior número digitado foi {maior}")

