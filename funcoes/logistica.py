import os
import funcoes.motoristas as motoristas
from funcoes.config import superuser, superuser_password

# Arquivo com a parte inicial do programa
log_status = False


def tela_inicial():

    global tipo_usuario

    os.system("cls" if os.name == "nt" else "clear")
    print("------------------------")
    print("1 - Aluno")
    print("2 - Motorista")
    print("3 - Administrador")
    print("0 - Sair")
    print("------------------------\n")
    tipo_usuario = int(input("Qual o tipo de usuário? "))


def tela_aluno():

    global op_principal

    os.system("cls" if os.name == "nt" else "clear")
    print("------------------------------------------------")
    print("1 - Marcar Viagem")
    print("2 - Desmarcar Viagem")
    print("3 - Consultar status de Passageiro(por nome)")
    print("4 - Modificar status de Passageiro(por nome)")
    print("5 - Consultar Horários")
    print("6 - Consultar Paradas")
    print("7 - Consultar Motoristas")
    print("0 - Sair")
    print("------------------------------------------------\n")
    op_principal = int(input("Selecione uma opção:"))


def tela_motorista():

    global op_principal

    os.system("cls" if os.name == "nt" else "clear")
    print("------------------------------------------------")
    print("1 - Consultar Quantidade de Passageiros(Total)")
    print("2 - Consultar Quantidade de Passageiros(por Instituição)")
    print("3 - Consultar Horários")
    print("4 - Consultar Paradas")
    print("0 - Sair")
    print("------------------------------------------------\n")
    op_principal = int(input("Selecione uma opção:"))


def tela_adm():

    global op_principal

    os.system("cls" if os.name == "nt" else "clear")
    print("------------------------------------------------")
    print("------ Pontos ------")
    print("1 - Cadastrar Ponto")
    print("2 - Deletar Ponto")
    print("3 - Modificar Ponto")
    print("4 - Consultar Pontos")
    print("--------------------")
    print("------ Horários ------")
    print("5 - Cadastrar Horário")
    print("6 - Deletar Horário")
    print("7 - Consultar Horários")
    print("----------------------")
    print("------- Motoristas -------")
    print("8 - Cadastrar Motorista")
    print("9 - Deletar Motorista")
    print("10 - Modificar Motorista")
    print("11 - Consultar Motoristas")
    print("--------------------------")
    print("0 - Sair")
    print("------------------------------------------------\n")
    op_principal = int(input("Selecione uma opção:"))


def login(login, senha):

    global log_status

    if tipo_usuario == 2:
        if motoristas.login_check(login) and motoristas.senha_check(senha):
            log_status = True
            return True

        return False
    if tipo_usuario == 3:
        if login == superuser and senha == superuser_password:
            log_status = True
            return True

        return False


def logout():

    global log_status

    log_status = False


def is_logged():

    if log_status:
        return True
    else:
        return False
