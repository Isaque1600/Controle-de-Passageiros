from funcoes.JSONify import JSONDatabase


def pegar_pontos():
    db = JSONDatabase("database/data.json")

    pontos = db.select("pontos")
    pontos = [i[1].get("nome") for i in pontos.items()]
    return pontos


def cadastrar_ponto():
    db = JSONDatabase("database/data.json")

    nome = input("Qual o nome do ponto?")

    try:
        db.set("pontos", {len(db.select("pontos")) + 1: {"nome": nome}})

        return "ponto inserido"
    except Exception:
        print("Erro ao inserir o ponto")


def deletar_ponto(nome):
    db = JSONDatabase("database/data.json")

    try:
        db.delete("pontos", db.get_id("pontos", nome)[0])
        print("Ponto deletado")
    except Exception as e:
        print(e)
