import os, time
import funcoes.horarios as horarios, funcoes.paradas as paradas

global passageiros, passageiros_por_instituicao

passageiros = []
passageiros_por_instituicao = {instituicao: 0 for instituicao in paradas.paradas}


def marcar_viagem():

    os.system("cls" if os.name == "nt" else "clear")

    print("\nMarcar Viagem: ")
    nome = input("Digite o seu nome completo:").strip()

    for i in passageiros:
        if i[0] == nome:
            print("Usuario ja existe!")
            time.sleep(1.5)
            return

    print("Opções de instituição:")
    for i in paradas.paradas:
        print(f"{i}")

    instituicao = ""
    while instituicao not in paradas.paradas:
        instituicao = input("Digite a intituicao que deseja ir: ").upper().strip()

    passageiros_por_instituicao[instituicao] += 1

    print("Opções de horário (ida):")
    for horario in horarios.horarios_ida:
        print(f"{horario}")

    opcao_hora_ida = ""
    while opcao_hora_ida not in horarios.horarios_ida:
        opcao_hora_ida = input("Selecione o horário de ida: ")

    print("Opções de horário (volta):")
    for horario in horarios.horarios_volta:
        print(f"{horario}")

    opcao_hora_volta = ""
    while opcao_hora_volta not in horarios.horarios_volta:
        opcao_hora_volta = input("Selecione o horário de volta: ")

    passageiros.append([nome, instituicao, opcao_hora_ida, opcao_hora_volta])
    print("Viagem marcada com sucesso!")


def desmarcar_viagem():

    os.system("cls" if os.name == "nt" else "clear")

    print("\nDesmarcar Viagem:")
    nome = input("Digite o nome colocado no momento de cadastro:")

    for i in passageiros:
        if i[0] == nome:
            passageiros.remove(i)
            print(f"Viagem do usuário {nome} desmarcada com sucesso!")

    print("Usuario não encontrado!")


def alterar_passageiro():

    os.system("cls" if os.name == "nt" else "clear")

    print("\nAlterar Passageiro:")
    nome = input("Digite o nome colocado no momento de cadastro:").strip()

    for i in passageiros:
        if i[0] == nome:
            print("Opções de instituição:")
            for parada in paradas.paradas:
                print(f"{parada}")

            passageiros_por_instituicao[i[1]] -= 1

            instituicao = ""
            while instituicao not in paradas.paradas:
                instituicao = input("Nova instituição: ")
                i[1] = instituicao

            passageiros_por_instituicao[i[1]] += 1

            print("Opções de horário (ida):")
            for horario in horarios.horarios_ida:
                print(f"{horario}")

            opcao_hora_ida = ""
            while opcao_hora_ida not in horarios.horarios_ida:
                opcao_hora_ida = input("Selecione o horário de ida: ")
                i[2] = opcao_hora_ida

            print("Opções de horário (volta):")
            for horario in horarios.horarios_volta:
                print(f"{horario}")

            opcao_hora_volta = ""
            while opcao_hora_volta not in horarios.horarios_volta:
                opcao_hora_volta = input("Selecione o horário de volta: ")
                i[3] = opcao_hora_volta

            print("Viagem alterada com sucesso!")
            return
        else:
            print("Usuario não encontrado!")

    print("Viagem alterada com sucesso!")


def consultar_passageiro():

    os.system("cls" if os.name == "nt" else "clear")

    print("\nConsultar Passageiro:")
    nome = input("Digite o nome colocado no momento de cadastro:")

    for i in passageiros:
        if i[0] == nome:
            print(f"Nome: {i[0]}")
            print(f"Instituição: {i[1]}")
            print(f"Horário de ida: {i[2]}")
            print(f"Horário de volta: {i[3]}")
            return
        else:
            print("Usuario não encontrado!")
