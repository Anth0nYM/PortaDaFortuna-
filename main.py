import random

pontuacao = 0
repetir = "s"

print("\n"*100)
print('''
Porta da Fortuna
----------------------------------------
Escolha a porta correta e ganhe pontos!
Escolha a porta errada e perca tudo!

Sua pontuação será salva quando escolher
parar de abrir portas!

Vamos começar!
''')

nome = str(input("Primeiro de tudo! Qual seu nome? (Somente o primeiro nome)\n"))
nome = nome.replace(" ", "")

tabela = open("pontuacao.txt", "r").read()
tabela = tabela.splitlines()
for u in tabela:
    nomeSalvo, pontuacaoSalva = u.split("|")

    if(nomeSalvo == nome):
        print("Você tinha {} pontos salvos, vamos continuar daqui!".format(
            pontuacaoSalva))
        pontuacao = int(pontuacaoSalva)


while repetir == "s":
    print('''
     _______   _______   _______
    |       | |       | |       |
    |  [1]  | |  [2]  | |  [3]  |
    |       | |       | |       |
    |       | |       | |       |
     -------   -------   -------
    ''')

    resposta = int(input("Qual a sua escolha? 1, 2 ou 3?\n"))
    correto = random.randint(1, 3)

    print("\n"*100)
    if resposta == correto:
        print("Parabéns você escolheu a porta correta!\n")

        pontuacao += 1
        print("Sua pontuação é de {} acertos\n".format(pontuacao))
    else:
        print("Não foi dessa vez, a porta correta era a {}\n".format(correto))

        pontuacao = 0
        print("Sua pontuação foi resetada\n")

    repetir = str(input("Deseja jogar novamente? (s/n)\n"))

    if repetir != "s":

        tabela = open("pontuacao.txt", "r").read()
        tabela = tabela.splitlines()

        novaTabela = open("pontuacao.txt", "w")

        if len(tabela) > 0:
            tabelaModificada = str()
            jaSalvo = False

            for u in tabela:
                nomeSalvo, pontuacaoSalva = u.split("|")

                if(nomeSalvo == nome):
                    jaSalvo = True
                    tabelaModificada += "{}|{}\n".format(nome, pontuacao)
                else:
                    tabelaModificada += "{}|{}\n".format(nomeSalvo, pontuacaoSalva)

            if not jaSalvo:
                tabelaModificada += "{}|{}\n".format(nome, pontuacao)

            novaTabela.write(tabelaModificada)
            novaTabela.close()
        else:
            novaTabela.write("{}|{}".format(nome, pontuacao))  
            novaTabela.close()