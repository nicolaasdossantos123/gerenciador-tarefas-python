contador = 0
numero = -1  

while numero != 0:
    numero = int(input("Digite um número (0 para sair): "))
    
    if numero != 0:
        contador += 1

print("Quantidade de números ímpares:", contador)