print("Bem vindo ao jogo de adivinhação!!")
print("#################################")
#Função range  range(start, stop, [step])
numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um numero entre 1 e 100: ")
    chute = int(chute_str) # convertendo de string para inteiro

    if (chute < 1 or chute > 100):
        print ('Voce deve digitar um numero entre 1 e 100!')
        continue #continua para prox iteração

    print("Voce digitou ", chute)
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print("Voce acertou!")
        break #para o for
    else:
        if maior:
            print("Seu chute foi maior que o numero secreto.")
        elif menor:
            print("Seu chute foi menor que o numero secreto.")
        print("Voce errou!")

    print("Fim do jogo!")
    rodada = rodada +1