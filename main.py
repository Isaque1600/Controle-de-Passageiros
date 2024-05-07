import os
import time
import funcoes.logistica as log
import funcoes.passageiros as p
import funcoes.paradas as pa
import funcoes.motoristas as m
import funcoes.superuser as su

log.tipo_usuario = -1

while log.tipo_usuario != 0:

    log.tela_inicial()

    if log.tipo_usuario == 1:
        log.tela_aluno()

        if log.op_principal == 0:
            p.tipo_usuario = -1

        elif log.op_principal == 1:
            p.marcar_viagem()

        elif log.op_principal == 2:
            p.desmarcar_viagem()

        elif log.op_principal == 3:
            p.consultar_status_passageiro()

        elif log.op_principal == 4:
            p.modificar_status_passageiro()

        elif log.op_principal == 5:
            h.consultar_horarios()

        elif log.op_principal == 6:
            pa.consultar_paradas()

        elif log.op_principal == 7:
            p.consultar_motoristas()

    if log.tipo_usuario == 2:

        os.system("cls" if os.name == "nt" else "clear")
        login = input("Login: ")
        senha = input("Senha: ")

        if log.login(login, senha):
            print("Logging...")
            time.sleep(2)
            print(f"Seja bem vindo {login}!")
            time.sleep(1)
        else:
            print("Login ou senha incorretos, tente novamente!")
            time.sleep(2)

        if log.is_logged():
            log.tela_motorista()

            if log.op_principal == 0:
                log.logout()
                log.tipo_usuario = -1

            elif log.op_principal == 1:
                m.consultar_quantidade_passageiros()

            elif log.op_principal == 2:
                m.consultar_quantidade_passageiros_instituicao()

            elif log.op_principal == 3:
                m.consultar_horarios()

            elif log.op_principal == 4:
                m.consultar_paradas()

    if log.tipo_usuario == 3:

        os.system("cls" if os.name == "nt" else "clear")
        login = input("Login: ")
        senha = input("Senha: ")

        if log.login(login, senha):
            print("Logging...")
            time.sleep(2)
            print(f"Seja bem vindo {login}!")
            time.sleep(1)
        else:
            print("Login ou senha incorretos, tente novamente!")
            time.sleep(2)

        if log.is_logged():
            log.tela_adm()

            if log.op_principal == 0:
                log.logout()
                log.tipo_usuario = -1

            elif log.op_principal == 1:
                pa.criar_ponto()

            elif log.op_principal == 2:
                pa.deletar_ponto()

            elif log.op_principal == 3:
                pa.modificar_ponto()

            elif log.op_principal == 4:
                pa.consultar_pontos()

            elif log.op_principal == 5:
                h.criar_horario()

            elif log.op_principal == 6:
                h.deletar_horario()

            elif log.op_principal == 7:
                h.consultar_horarios()

            elif log.op_principal == 8:
                m.criar_motorista()

            elif log.op_principal == 9:
                m.deletar_motorista()

            elif log.op_principal == 10:
                m.modificar_motorista()

            elif log.op_principal == 11:
                m.consultar_motoristas()


print("Saindo...")
time.sleep(2)
print("Programa encerrado")
