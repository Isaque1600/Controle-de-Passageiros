# Lista para guardar os passageiros, funciona como uma matriz, onde cada index do Lista é um outro Lista
# Contendo nome, instituição, horario de ida e horario de volta.
#           [0]       [1]           [2]                [3]
passageiros = []

# Lista para guardar o as informações dos motoristas, como nome e telefone
motoristas = []

# Lista com os horarios, de inicio será uma lista estatica, mais pra frente implementaremos
# a possibilidade de manipular dinamicamente a lista
horarios = ["06h", "12h", "18h", "21h30"]

# Lista com as paradas/intituições, novamente de inicio sera uma lista estatica.
# Depois implementaremos a possibilidade de manipular dinamicamente a lista
instituicoes = ["IFPB", "UEPB", "UFCG", "ITEC", "UNIPLAN", "FIP"]

# Variavel para a escola das opções
opc = 0

# Enquanto a variavel opc for maior que 0 o programa continua rodando
while opc >= 0:

    # Cada opção executa uma funcionalidade, essas são as funcionalidades iniciais
    # Por enquanto implementamos apenas a primeira e a setima, além da opção de sair
    print(
        "-" * 10 + "Opções" + "-" * 10,
        "\nMarcar viagem => 1",
        "\nDesmarcar viagem => 2",
        "\nConsultar Quantidade de Pessoas por Instituição => 3",
        "\nConsultar Horários => 4",
        "\nConsultar Paradas => 5",
        "\nConsultar Motoristas => 6",
        "\nConsultar Quantidade Total de Passageiros => 7",
        "\nSair => -1",
        "\n" + "-" * 26,
    )
    opc = int(input("Digite a operação que deseja realizar:"))

    if opc == 1:
        nome = input("Digite o nome do aluno:")
        for i in instituicoes:
            print(f"{i.upper()}")

        instituicao = input(
            "Digite a instituição do aluno (acima é possivel ver as opções):"
        )

        while instituicao not in instituicoes:
            print("Instituição inválida. Por favor, tente novamente.")
            instituicao = input(
                "Digite a instituição do aluno (acima é possivel ver as opções):"
            )

        for i in horarios:
            print(f"{i.upper()}")

        print("Selecione um dos horarios a cima")
        horario_ida = input("Digite o horário de ida do aluno:")

        while horario_ida not in horarios:
            print("Horario invalido, selecione um dos horarios acima para a Ida!")
            horario_ida = input("Digite o horário de ida do aluno:")


        for i in horarios:
            print(f"{i.upper()}")

        print("Selecione um dos horarios a cima")
        horario_volta = input("Digite o horario de volta do aluno")

        while horario_volta not in horarios:
            print("Horario invalido, selecione um dos horarios acima para a Ida!")
            horario_volta = input("Digite o horario de volta do aluno")

        passageiros.append(
            [
                nome,
                instituicao,
                horario_ida,
                horario_volta,
            ]
        )

    # if opc == 2:
    #     instituicoes = []
    #     qnt = []
    #     for pessoa in passageiros:
    #         if pessoa[1] not in instituicoes:
    #             instituicoes.append(pessoa[1])
    #             qnt.append(1)
    #         else:
    #             qnt[instituicoes.index(pessoa[1])][0] += 1
    #     print(instituicoes, qnt)

    elif opc == 7:
        print(f"A quantidade total de passageiros eh: {len(passageiros)}")

print("Programa encerrado")