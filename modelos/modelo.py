import sqlite3

def conectar():
    return sqlite3.connect("banco.db")


def inserir_produtos(nome, preco, quantidade):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))
        conexao.commit()

def buscar_produtos():
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        return cursor.fetchall()

def atualizar_preco(id_produto, novo_preco):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("UPDATE produtos SET preco = ? WHERE id = ?", (novo_preco, id_produto))
        conexao.commit()

def deletar_produto(id_produto):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        conexao.commit()