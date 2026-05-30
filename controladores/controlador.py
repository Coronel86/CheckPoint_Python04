from modelos.modelo import inserir_produtos, buscar_produtos

def processar_cadastro(produto, preco, quantidade):
    if produto == "" or preco == "":
        return False, "Erro: Produto, preço ou quantidade estão vazios!"
    try:
        preco = float(preco)
        quantidade = int(quantidade)
    except ValueError:
        return False, "Erro: Preço ou quantidade deve ser um número inteiro e com (.) em vez de vírgulas!"

    inserir_produtos(produto, preco, quantidade)
    return True, "Cadastro realizado com sucesso!"

def obter_lista_produtos():
    return buscar_produtos()