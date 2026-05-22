from modelos.modelo import inserir_produtos

def processar_cadastro(nome, preco, quantidade):
    if nome == "" or preco == "":
        return False, "Erro: Nome ou preço estão vazios!"
    try:
        preco = float(preco)
        quantidade = int(quantidade)
    except ValueError:
        return False, "Erro: quantidade deve ser um número inteiro!"

    inserir_produtos(nome, preco, quantidade)
    return True, "Cadastro realizado com sucesso!"