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
