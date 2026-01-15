print("Olá! Você pode me fazer perguntas.")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ").lower()

    if pergunta == "sair":
        print("Computador: Até logo!")
        break

    elif "seu nome" in pergunta:
        print("Computador: Meu nome é Computador.")

    elif "como você está" in pergunta:
        print("Computador: Estou funcionando perfeitamente!")

    elif "hora" in pergunta:
        print("Computador: A hora eu ainda  não sei mas podemos conversar")

    elif "python" in pergunta:
        print("Computador: Python é uma linguagem de programação simples e poderosa.")

    else:
        print("Computador: Desculpa, ainda não sei responder isso.")
