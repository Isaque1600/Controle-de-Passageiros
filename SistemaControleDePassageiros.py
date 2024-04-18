passageiros = []
motoristas = []
horarios = []

while True:
    print(
        "-" * 10 + "Opções" + "-" * 10,
        "\nPassageiros -------------",
        "\nMarcar viagem => 1",
        "\nDesmarcar viagem => 2",
        "\nConsultar Quantidade de Pessoas por Instituição => 3",
        "\nConsultar Horários => 4",
        "\nConsultar Paradas => 5",
        "\nMotoristas --------------",
        "\nConsultar Motoristas => 6",
        "\nConsultar Quantidade Total de Passageiros => 7",
        "\nCadastrar Motorista => 8",
        "\nModificar Cadastro => 9",
        "\nExcluir Motorista => 10",
        "\nConfigurações -----------",
        "\nCadastrar Horários => 11",
        "\nAlterar Horários => 12",
        "\nExcluir Horário => 13",
        "\nCadastrar Ponto => 14",
        "\nAlterar Ponto => 15",
        "\nExcluir Ponto => 16",
        "\nSair => -1",
        "\n" + "-" * 26,
    )
    opc = int(input("Digite a operação que deseja realizar:"))

    if opc == -1:
        break

    if opc == 1:
        passageiros.append(
            [
                input("Digite o nome do passageiro:"),
                input("Digite a instituição do passageiro:"),
                input("Digite o horario de ida do passageiro:"),
                input("Digite o horario de retorno do passageiro:"),
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

    elif opc == 8:
        print(passageiros)
