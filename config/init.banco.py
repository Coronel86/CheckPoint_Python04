import sqlite3

def conectar():
    return sqlite3.connect("banco.db")

def criar_tabela():
    
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL,
                    quantidade INTEGER NOT NULL
                )
            """)

        
        print("Banco de dados e tabela 'produtos' criados com sucesso!")
    except sqlite3.Error as erro:
        print(f"OCORREU UM ERRO NO BANCO: {erro}")
    
    

if __name__ == "__main__":
    criar_tabela()