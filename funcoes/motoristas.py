import os, time
import funcoes.passageiros as passageiros

# Funções da parte dos motoristas

global motoristas

motoristas = [["jose", "123", "8399999999"], ["pedro", "456", "8399999999"]]
#                   Funciona como uma matriz
#                   [0] -> Nome do motorista
#                   [1] -> Senha do motorista
#                   [2] -> Telefone/WhatsApp do motorista


def login_check(login):
    for i in motoristas:
        if login == i[0]:
            return True

    return False


def senha_check(senha):
    for i in motoristas:
        if senha == i[1]:
            return True

    return False


def check_quantidade_passageiros():

    os.system("cls" if os.name == "nt" else "clear")

    print(f"Segue a quantidade total de passageiros: \n {len(passageiros.passageiros)}")


def check_quantidade_passageiros_instituicao():

    os.system("cls" if os.name == "nt" else "clear")

    print(f"Segue a Quantidade de Passageiros por Instituição: \n")

    for instituicao in passageiros.passageiros_por_instituicao.items():
        print(f"{instituicao[0]} - {instituicao[1]}")


def cadastro():

    os.system("cls" if os.name == "nt" else "clear")

    print("Digite o nome:")
    nome = str(input("")).strip()
    for i in motoristas:
        if nome == i[0]:
            print("Motorista ja existe!")
            time.sleep(1.5)
            return
    print("Crie a sua senha:")
    senha = str(input(""))
    print("Digite seu telefone")
    telefone = int(input(""))
    motoristas.append([nome, senha, telefone])
    print("Cadastro realizado com sucesso!")


def consulta_motorista():

    os.system("cls" if os.name == "nt" else "clear")

    print(f"Segue os motoristas disponiveis e o contato dos respectivos")
    for motorista in motoristas:
        print(f"{motorista[0]} - {motorista[2]}")


def mod_cadastro_motoristas():

    os.system("cls" if os.name == "nt" else "clear")

    pin_loPas = input(
        "Você deseja modificar o login ou a senha?\n01 - login\n02 - Senha\n03 - Numero de Telefone\n"
    )
    if pin_loPas == "01" or pin_loPas == "1":
        login = input("Digite o nome do motorista (antigo): ").strip()
        for motorista in motoristas:
            if login == motorista[0]:
                motorista[0] = input("Novo Nome: ").strip()
    elif pin_loPas == "02" or pin_loPas == "2":
        login = input("Digite o nome do motorista: ")
        for motorista in motoristas:
            if login == motorista[0]:
                motorista[1] = input("Nova Senha: ").strip()
    elif pin_loPas == "03" or pin_loPas == "3":
        login = input("Digite o nome do motorista: ")
        for motorista in motoristas:
            if login == motorista[0]:
                motorista[2] = input("Novo Telefone: ").strip()


def excluir_motorista():

    os.system("cls" if os.name == "nt" else "clear")

    for index, motorista in enumerate(motoristas):
        print(f"{index+1} - {motorista[0]}")

    motorista = int(input("Qual o motorista que deseja excluir? ")) - 1
    motoristas.pop(motorista)
    print("Motorista excluído com sucesso!")
