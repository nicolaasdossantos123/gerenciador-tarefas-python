while True:
    try: #Se a pessoa digitar letra, o programa quebra.
        numero = int(input("Digite um número (0 para sair): "))
    except ValueError: #except ValueError funciona com try
        print("Digite apenas números!")
        continue

    if numero == 0:
        break

    contador += 1