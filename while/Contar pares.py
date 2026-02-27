contador = 0

print("Digite seu número (0 para sair): ")

while True:

        numero = int(input())

        if numero == 0:
            break

        if numero > 0 and numero % 2 == 0:
            contador += 1
    
        
print(f"\nForam digitados {contador} números ímpares e positivos.")