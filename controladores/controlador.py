from modelos.modelo import inserir_produtos

def processar_cadastro(produto, preco, quantidade):
    if produto == "" or preco == "":
        return False, "Erro: Produto ou preço estão vazios!"
    try:
        preco = float(preco)
        quantidade = int(quantidade)
    except ValueError:
        return False, "Erro: quantidade deve ser um número inteiro!"

    inserir_produtos(produto, preco, quantidade)
    return True, "Cadastro realizado com sucesso!"