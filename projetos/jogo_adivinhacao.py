import random

print("Bem-vindo ao jogo de adivinhar o número secreto!\n")

pontuacao = 0

def escolher_dificuldade():
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 50)")
    print("3 - Difícil (1 a 100)\n")

    try:
        dificuldade = int(input("Escolha uma dificuldade: "))
    except ValueError:
        print("Digite apenas números.\n")
        return None

    if dificuldade == 1:
        return 10, 4
    elif dificuldade == 2:
        return 50, 6
    elif dificuldade == 3:
        return 100, 8
    else:
        print("Opção inválida!\n")
        return None
    
def jogar_partida(limite, tentativas_max):
    numero_secreto = random.randint(1, limite)
    tentativas = 0

    while tentativas < tentativas_max:
        try:
            chute = int(input(f"Escolha um número de 1 a {limite}: "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if not (1 <= chute <= limite):
            print("Número inválido!\n")
            continue

        if chute == numero_secreto:
            print("Parabéns, você acertou!\n")
            return True  

        elif chute < numero_secreto:
            print("Maior")
        else:
            print("Menor")

        tentativas += 1
        print(f"Tentativa {tentativas + 1} de {tentativas_max}\n")

    print(f"Você perdeu! O número era {numero_secreto}\n")
    return False

def menu_final():
    print("1 - Jogar novamente")
    print("2 - Sair")

    try:
        return int(input("Escolha: "))
    except ValueError:
        return 2

while True:
    config = escolher_dificuldade()

    if config is None:
        continue

    limite, tentativas_max = config

    ganhou = jogar_partida(limite, tentativas_max)

    if ganhou:
        pontuacao += 10

    print(f"Pontuação atual: {pontuacao}\n")

    opcao = menu_final()

    if opcao == 2:
        print("Encerrando o jogo...")
        break