def jogar():

    import random

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = int(random.randrange(1,101))
    rodada = 1
    pontos = 1000

    print("\nNíveis de Dificculdade")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha o nível de dificuldade: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while(rodada <= total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("\nVocê deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("\nParabéns! Você acertou! Sua pontuação foi de {} pontos.".format(pontos))
            break
        else:
            if(maior):
                print("\nO seu chute foi maior do que o número secreto!")
            elif(menor):
                print("\nO seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        rodada = rodada + 1

    print("\nO número secreto é: {}".format(numero_secreto))
    print("\nFim do jogo")

if (__name__ == "__main__"):
    jogar()