contador = 0

print("Digite números (digite -1 para sair): ")

while True:
    
        numero = int(input())
        
        if numero == -1:
            break
            
        if numero > 0 and numero % 2 == 1:
            contador += 1
            

print(f"\nForam digitados {contador} números positivos e ímpares.")