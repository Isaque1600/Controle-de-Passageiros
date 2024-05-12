import os

global horarios

horarios_ida = ["06:00", "12:00", "18:00"]
horarios_volta = ["12:00", "18:00", "21:30"]


def mostrar_horarios():
    os.system("cls" if os.name == "nt" else "clear")

    while True:
        tipo = int(input("Horario de ida(0) ou volta(1)? "))
        if tipo == 0 or tipo == 1:
            break
        print("Insira uma opção válida")

    if tipo == 0:
        for horario in horarios_ida:
            print(f"{horario}")
    elif tipo == 1:
        for horario in horarios_volta:
            print(f"{horario}")


def cad_horarios():
    os.system("cls" if os.name == "nt" else "clear")

    while True:
        tipo = int(input("Horario de ida(0) ou volta(1)? "))
        if tipo == 0 or tipo == 1:
            break
        print("Insira uma opção válida")

    os.system("cls" if os.name == "nt" else "clear")

    if tipo == 0:
        horarios_ida.append(input("Horario (HH:MM): "))
        print("Horario adicionado com sucesso!")
    elif tipo == 1:
        horarios_volta.append(input("Horario (HH:MM): "))
        print("Horario adicionado com sucesso!")


def alt_horarios():

    os.system("cls" if os.name == "nt" else "clear")

    while True:
        tipo = int(input("Modificar horario de ida(0) ou volta(1)? "))
        if tipo == 0 or tipo == 1:
            break
        print("Insira uma opção válida")

    os.system("cls" if os.name == "nt" else "clear")

    if tipo == 0:
        print("Lista de Horários(ida): ")
        for i, horario in enumerate(horarios_ida):
            print(f"{i + 1} - {horario}")

        while True:
            indice = (
                int(input("Digite o número do horário a ser alterado (0 para sair): "))
                - 1
            )
            if indice == -1:
                return
            if 0 <= indice < len(horarios):
                break
            print("Insira um índice válido")

        novo_horario = input("Digite o novo horário: ")
        horarios_ida[indice] = novo_horario
        print("Horário alterado com sucesso!")

        os.system("cls" if os.name == "nt" else "clear")

        print("Lista atualizada:")
        for i, horario in enumerate(horarios_ida):
            print(f"{i + 1} - {horario}")

    elif tipo == 1:
        print("Lista de Horários(volta): ")
        for i, horario in enumerate(horarios_volta):
            print(f"{i + 1} - {horario}")

        while True:
            indice = (
                int(input("Digite o número do horário a ser alterado (0 para sair): "))
                - 1
            )
            if indice == -1:
                return
            if 0 <= indice < len(horarios):
                break
            print("Insira um índice válido")

        novo_horario = input("Digite o novo horário: ")
        horarios_volta[indice] = novo_horario
        print("Horário de volta alterado com sucesso!")

        print("Lista atualizada:")
        for i, horario in enumerate(horarios_volta):
            print(f"{i + 1} - {horario}")

        input("Pressione Enter para continuar...")


def del_horarios():

    os.system("cls" if os.name == "nt" else "clear")

    while True:
        tipo = int(input("Excluir horario de ida(0) ou volta(1)? "))
        if tipo == 0 or tipo == 1:
            break
        print("Insira uma opção válida")

    os.system("cls" if os.name == "nt" else "clear")

    if tipo == 0:
        print("Horários de ida disponíveis:")
        for i, horario in enumerate(horarios_ida):
            print(f"{i+1} - {horario}")

        while True:
            op = int(
                input("Digite o número do horário que quer deletar (0 para sair): ")
            )
            if op <= len(horarios_ida):
                break
            print("Insira uma opção válida")

        if op == 0:
            return
        else:
            del horarios_ida[op - 1]
            print("Horário deletado com sucesso")

            os.system("cls" if os.name == "nt" else "clear")

            print("Lista atualizada:")
            for i, horario in enumerate(horarios_ida):
                print(f"{i+1} - {horario}")

            input("Pressione Enter para continuar...")
    elif tipo == 1:
        print("Horários de volta disponíveis:")
        for i, horario in enumerate(horarios_volta):
            print(f"{i+1} - {horario}")

        while True:
            op = int(
                input("Digite o número do horário que quer deletar (0 para sair): ")
            )
            if op <= len(horarios_volta):
                break
            print("Insira uma opção válida")

        if op == 0:
            return
        else:
            del horarios_volta[op - 1]
            print("Horário deletado com sucesso")

            os.system("cls" if os.name == "nt" else "clear")

            print("Lista atualizada:")
            for i, horario in enumerate(horarios_volta):
                print(f"{i+1} - {horario}")

            input("Pressione Enter para continuar...")
