import customtkinter as ctk
from controladores.controlador import processar_cadastro

def botao_verificar_e_salvar():
    nome_digitado = cx_nome.get()
    preco_digitado = cx_preco.get()
    quantidade_digitada = cx_quantidade.get()

    sucesso, mensagem = processar_cadastro(nome_digitado, preco_digitado, quantidade_digitada)

    lbl_aviso.configure(text=mensagem, text_color="green" if sucesso else "red")
    janela.after(3000, lambda: lbl_aviso.configure(text=""))

       