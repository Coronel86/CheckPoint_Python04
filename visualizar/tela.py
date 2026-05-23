import customtkinter as ctk
from tkinter import messagebox
from controladores.controlador import processar_cadastro
import main



def botao_gravar_produto():
    produto_digitado = cx_produto.get()
    preco_digitado = cx_preco.get()
    quantidade_digitada = cx_quantidade.get()

    if processar_cadastro(produto_digitado, preco_digitado, quantidade_digitada):
        lbl_aviso.configure(text="Produto criado com sucesso!", text_color="green")
    else:
        lbl_aviso.configure(text="O produto, preço ou quantidade não pode ser vazio!", text_color="red")
    janela.after(3000, lambda: lbl_aviso.configure(text=""))


def iniciar_janela_principal():
    global janela, cx_produto, cx_preco, cx_quantidade, lbl_aviso

    janela = ctk.CTk()
    janela.title("Exemplo Padrão MVC")
    janela.geometry("800x500")

    lbl_titulo = ctk.CTkLabel(janela, text="**** Cadastrar Produtos ****")
    lbl_titulo.pack(pady=20)

    cx_produto = ctk.CTkEntry(janela, placeholder_text="Digite o nome do produto...")
    cx_produto.pack(pady=10)

    cx_preco = ctk.CTkEntry(janela, placeholder_text="Digite o preço do produto...")
    cx_preco.pack(pady=10)

    cx_quantidade = ctk.CTkEntry(janela, placeholder_text="Digite a quantidade do produto...")
    cx_quantidade.pack(pady=10)

    lbl_aviso = ctk.CTkLabel(janela, text="")
    lbl_aviso.pack(pady=5)

    btn_salvar = ctk.CTkButton(
        janela,
        text="Gravar Produto",
        command=botao_gravar_produto
    )
    btn_salvar.pack(pady=10)

    janela.mainloop()


       