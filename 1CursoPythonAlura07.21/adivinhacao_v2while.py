print("Bem vindo ao jogo de adivinhação!!")
print("#################################")
numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite seu numero: ")
    chute = int(chute_str) # convertendo de string para inteiro
    print("Voce digitou ", chute)
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print("Voce acertou!")
    else:
        if maior:
            print("Seu chute foi maior que o numero secreto.")
        elif menor:
            print("Seu chute foi menor que o numero secreto.")
        print("Voce errou!")

    print("Fim do jogo!")
    rodada = rodada +1