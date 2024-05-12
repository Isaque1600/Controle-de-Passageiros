import os
import time
import funcoes.logistica as log
import funcoes.passageiros as p
import funcoes.paradas as pa
import funcoes.motoristas as m
import funcoes.horarios as h

log.tipo_usuario = -1
tentativas = 0

while log.tipo_usuario != 0:

    if log.tipo_usuario == 1:
        log.tela_aluno()

        if log.op_principal == 0:
            log.tipo_usuario = -1

        elif log.op_principal == 1:
            p.marcar_viagem()

        elif log.op_principal == 2:
            p.desmarcar_viagem()

        elif log.op_principal == 3:
            p.consultar_passageiro()

            input("Pressione Enter para continuar...")

        elif log.op_principal == 4:
            p.alterar_passageiro()

        elif log.op_principal == 5:
            h.mostrar_horarios()

            input("Pressione Enter para continuar...")

        elif log.op_principal == 6:
            pa.mostrar_paradas()

            input("Pressione Enter para continuar...")

        elif log.op_principal == 7:
            m.consulta_motorista()

            input("Pressione Enter para continuar...")

    if log.tipo_usuario == 2:

        os.system("cls" if os.name == "nt" else "clear")

        if log.is_logged():
            log.tela_motorista()

            if log.op_principal == 0:
                log.logout()
                log.tipo_usuario = -1

            elif log.op_principal == 1:
                m.check_quantidade_passageiros()

                input("Pressione Enter para continuar...")

            elif log.op_principal == 2:
                m.check_quantidade_passageiros_instituicao()

                input("Pressione Enter para continuar...")

            elif log.op_principal == 3:
                h.mostrar_horarios()

                input("Pressione Enter para continuar...")

            elif log.op_principal == 4:
                pa.mostrar_paradas()

                input("Pressione Enter para continuar...")
        else:
            if tentativas == 3:
                print("Tentativas esgotadas, tente novamente mais tarde!")
                log.tipo_usuario = -1

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

    if log.tipo_usuario == 3:

        os.system("cls" if os.name == "nt" else "clear")
        if log.is_logged():
            log.tela_adm()

            if log.op_principal == 0:
                log.logout()
                log.tipo_usuario = -1

            elif log.op_principal == 1:
                pa.cadastrar_parada()

            elif log.op_principal == 2:
                pa.excluir_parada()

            elif log.op_principal == 3:
                pa.alterar_parada()

            elif log.op_principal == 4:
                pa.mostrar_paradas()

                input("Pressione Enter para continuar...")

            elif log.op_principal == 5:
                h.cad_horarios()

            elif log.op_principal == 6:
                h.del_horarios()

            elif log.op_principal == 7:
                h.mostrar_horarios()

                input("Pressione Enter para continuar...")

            elif log.op_principal == 8:
                m.cadastro()

            elif log.op_principal == 9:
                m.excluir_motorista()

            elif log.op_principal == 10:
                m.mod_cadastro_motoristas()

            elif log.op_principal == 11:
                m.consulta_motorista()

                input("Pressione Enter para continuar...")
        else:
            if tentativas == 3:
                print("Tentativas esgotadas, tente novamente mais tarde!")
                log.tipo_usuario = -1

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

    if log.tipo_usuario not in [1, 2, 3]:
        log.tela_inicial()


print("Saindo...")
time.sleep(2)
print("Programa encerrado")
