import os

global paradas

paradas = ["UEPB", "IFPB", "FIP", "UNIPLAN"]


def mostrar_paradas():

    os.system("cls" if os.name == "nt" else "clear")

    print("Paradas:")
    for index, parada in enumerate(paradas):
        print(f"{index + 1} - {parada}")


def cadastrar_parada():

    os.system("cls" if os.name == "nt" else "clear")

    instituicoes = input("Digite o nome da instituição: ").upper()

    paradas.append(instituicoes)
    print("Ponto de ônibus cadastrado com sucesso!")

    # return pontos_onibus


def alterar_parada():

    os.system("cls" if os.name == "nt" else "clear")

    mostrar_paradas()

    indice = int(input("Digite o indice do ponto que vc quer alterar: "))

    if indice < 0 or indice > len(paradas):
        print("Erro: Indice inválido!")
    else:
        ponto_atualizado = input("Digite o nome da instituição atualizada: ")
        paradas[indice - 1] = ponto_atualizado

        print("Ponto atualizado com sucesso!")


def excluir_parada():

    os.system("cls" if os.name == "nt" else "clear")

    mostrar_paradas()

    indice = int(input("Digite o indice do ponto que vc quer excluir: "))

    if indice < 0 or indice > len(paradas):
        print("Erro: Indice inválido!")
    else:
        del paradas[indice]

        print("Ponto excluído com sucesso!")
