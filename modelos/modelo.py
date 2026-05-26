import sqlite3

def conectar():
    return sqlite3.connect("banco.db")


def inserir_produtos(produto, preco, quantidade):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO produtos (produto, preco, quantidade) VALUES (?, ?, ?)", (produto, preco, quantidade))
        conexao.commit()

def buscar_produtos():
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM produtos")
            return cursor.fetchall()
    except sqlite3.Error:
        return []

def atualizar_preco(id_produto, novo_preco):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute("UPDATE produtos SET preco = ? WHERE id = ?", (novo_preco, id_produto))
        conexao.commit()



