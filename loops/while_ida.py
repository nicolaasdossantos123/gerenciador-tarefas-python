idade = 0

while idade != 0:
    idade = int(input("Digite sua idade (0 para sair): "))

    if idade == 0:
        print("Programa encerrado")
        if idade < 18:
            print("Menor de idade")
        elif idade > 18:
         print("Maior de idade")
        else:
           print("Idoso")