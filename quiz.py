


import random


def menu():
    print("\n================================")
    print("   QUIZ DE CONHECIMENTOS GERAIS")
    print("================================")
    print("1 - Iniciar Quiz")
    print("2 - Ver regras do jogo")
    print("3 - Ver classificacao")
    print("4 - Sair")
    print("================================")



def regras():
    print("\n========== REGRAS DO QUIZ ==========")
    print("- O quiz possui perguntas de nivel intermediario.")
    print("- Cada pergunta possui quatro alternativas.")
    print("- Apenas uma alternativa esta correta.")
    print("- Cada resposta correta vale 1 ponto.")
    print("- Ao final, sera apresentada sua pontuacao.")
    print("====================================")



def verificar_resposta(resposta, correta):
    if resposta.upper() == correta:
        return 1
    else:
        return 0



def iniciar_quiz():
    perguntas = [
        {
            "pergunta": "Qual e o maior planeta do Sistema Solar?",
            "alternativas": ["A) Terra", "B) Jupiter",
                            "C) Saturno", "D) Netuno"],
            "correta": "B"
        },
        {
            "pergunta": "Em que ano ocorreu a Proclamacao da Republica no Brasil?",
            "alternativas": ["A) 1822", "B) 1888",
                            "C) 1889", "D) 1891"],
            "correta": "C"
        },
        {
            "pergunta": "Qual o último ano que o Brasil ganhou a copa do mundo?",
            "alternativas": ["A) 1958 ", "B) 2002",
                            "C) 2006 ", "D) 1970"],
            "correta": "B"
        },
        {
            "pergunta": "Qual e o maior oceano do planeta?",
            "alternativas": ["A) Atlantico", "B) Indico",
                            "C) Artico", "D) Pacifico"],
            "correta": "D"
        },
        {
            "pergunta": "Qual pais e conhecido como a terra do Sol nascente?",
            "alternativas": ["A) China", "B) Japao",
                            "C) Coreia do Sul", "D) Tailandia"],
            "correta": "B"
        },
        {
            "pergunta": "Quantas copas do mundo o Brasil ja ganhou?",
            "alternativas": ["A) 1", "B) 4",
                            "C) 5", "D) 6"],
            "correta": "C"
        },
        {
            "pergunta": "Quem escreveu o livro Sítio do Picapau Amarelo ?",
            "alternativas": ["A) Monteiro Lobato", "B) Jose de Alencar",
                            "C) Clarice Lispector", "D) Carlos Drummond"],
            "correta": "A"
        },
        {
            "pergunta": "Qual e a capital do Brasil?",
            "alternativas": ["A) Rio de Janeiro", "B) Salvador",
                            "C) Brasília", "D) Mananus"],
            "correta": "C"
        },
        {
            "pergunta": "Quantos ossos possui, aproximadamente, um adulto?",
            "alternativas": ["A) 106", "B) 206",
                            "C) 306", "D) 406"],
            "correta": "B"
        },
        {
            "pergunta": "Qual e o processo pelo qual as plantas produzem seu alimento?",
            "alternativas": ["A) Respiracao", "B) Fermentacao",
                            "C) Fotossintese", "D) Digestao"],
            "correta": "C"
        }
    ]

   
    random.shuffle(perguntas)

    pontos = 0

    print("\n========== INICIANDO O QUIZ ==========")

    for i, pergunta in enumerate(perguntas, start=1):
        print(f"\nPergunta {i}: {pergunta['pergunta']}")

        for alternativa in pergunta["alternativas"]:
            print(alternativa)

        resposta = input("Digite sua resposta (A, B, C ou D): ").strip().upper()

        while resposta not in ["A", "B", "C", "D"]:
            print("Opcao invalida! Digite A, B, C ou D.")
            resposta = input("Sua resposta: ").strip().upper()

        pontos += verificar_resposta(resposta, pergunta["correta"])

        if resposta == pergunta["correta"]:
            print("Parabens! Resposta correta!")
        else:
            print("Resposta incorreta!")
            print("A resposta correta era:", pergunta["correta"])

    print("\n========== RESULTADO FINAL ==========")
    print("Pontuacao:", pontos, "de 10 pontos")

    mostrar_classificacao(pontos)



def mostrar_classificacao(pontos):
    if pontos >= 8:
        print("Classificacao: parabéns! você conhece o básico! :)")
    elif pontos >= 5:
        print("Classificacao: mais ou menos! melhore! ;).")
    elif pontos >= 3:
        print("Classificacao: vamos estudar? isso é só o básico.")
    else:
        print("Classificacao: vixi! desista :(!")
        
        print("\n Feito por Kaio e Israellen :)")




def main():
    while True:
        menu()

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            iniciar_quiz()

        elif opcao == "2":
            regras()

        elif opcao == "3":
            print("\nConsulte a classificacao respondendo ao quiz!")

        elif opcao == "4":
            print("\nObrigado por jogar! Ate a proxima!")
            break

        else:
            print("\nOpcao invalida! Tente novamente.")



main()
