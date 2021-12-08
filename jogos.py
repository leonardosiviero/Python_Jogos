def escolhe_jogo():

    import forca
    import adivinhacao

    print("*********************************")
    print("********* Menu de Jogos *********")
    print("*********************************")

    print("Lista de jogos disponíveis: \n")
    print("(1) Jogo da Forca")
    print("(2) Jogo da Adivinhação")

    jogo = int(input("\nDigite o número da opção desejada: \n"))

    if jogo == 1:
        print("Jogando jogo da forca!\n")
        forca.jogar()
    elif jogo == 2:
        print("Jogando jogo da adivinhação!\n")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()
