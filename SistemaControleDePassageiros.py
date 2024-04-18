passageiros = []
motoristas = []
horarios = ["06h", "12h", "18h", "21h30"]
instituicoes = ["IFPB", "UEPB", "UFCG", "ITEC", "UNIPLAN", "FIP"]
opc = 0

while opc >= 0:
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

        horario_ida = input("Digite o horário de ida do aluno:")
        horario_volta = input("Digite o horario de volta do aluno")

        passageiros.append(
            [
                nome,
                instituicao,
                horario_ida,
                horario_volta,
            ]
        )

    if opc == 2:
        instituicoes = []
        qnt = []
        for pessoa in passageiros:
            if pessoa[1] not in instituicoes:
                instituicoes.append(pessoa[1])
                qnt.append(1)
            else:
                qnt[instituicoes.index(pessoa[1])][0] += 1
        print(instituicoes, qnt)

    elif opc == 7:
        print(f"A quantidade total de passageiros eh: {len(passageiros)}")

print("Programa encerrado")
