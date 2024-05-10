import passageiros
import horarios
import paradas

# Funções da parte dos motoristas

global motoristas

motoristas = []
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


def check_horarios():
    print(f"Segue os Horários: \n {horarios}")


def check_paradas():
    print(f"Segue as Paradas: \n {paradas} ")


def check_quantidade_passageiros():
    print(f"Segue a quantidade total de passageiros: \n {len(passageiros.passageiros)}")


def check_quantidade_passageiros_instituicao():
    print(
        f"Segue a Quantidade de Passageiros por Instituição: \n {passageiros.passageiros_por_instituicao}"
    )
