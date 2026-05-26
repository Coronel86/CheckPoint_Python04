import customtkinter as ctk
from tkinter import messagebox
from controladores.controlador import processar_cadastro, obter_lista_produtos


import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Variável global para controlar o canvas do gráfico e não duplicar
canvas_grafico = None

def botao_gravar_produto():
    produto_digitado = cx_produto.get()
    preco_digitado = cx_preco.get()
    quantidade_digitada = cx_quantidade.get()

    sucesso, mensagem = processar_cadastro(produto_digitado, preco_digitado, quantidade_digitada)

    if sucesso:
        messagebox.showinfo("Sucesso", mensagem) # Usando messagebox
        cx_produto.delete(0, 'end')
        cx_preco.delete(0, 'end')
        cx_quantidade.delete(0, 'end')
        atualizar_listagem() # Atualiza a lista automaticamente ao salvar
    else:
        messagebox.showerror("Erro de Validação", mensagem)

def atualizar_listagem():
    """Fase 3: Criar uma listagem atualizável"""
    txt_listagem.configure(state="normal") # Libera para escrita
    txt_listagem.delete("1.0", "end") # Limpa o texto antigo
    
    produtos = obter_lista_produtos()
    
    txt_listagem.insert("end", f"{'ID':<5} | {'Produto':<20} | {'Preço':<10} | {'Qtd':<5}\n")
    txt_listagem.insert("end", "-"*50 + "\n")
    
    for p in produtos:
        # p[0]=id, p[1]=produto, p[2]=preco, p[3]=quantidade
        txt_listagem.insert("end", f"{p[0]:<5} | {p[1]:<20} | R$ {p[2]:<8.2f} | {p[3]:<5}\n")
        
    txt_listagem.configure(state="disabled") # Bloqueia para o usuário não editar

def gerar_dashboard():
    """Fase 4: O Dashboard com Matplotlib"""
    global canvas_grafico
    
    produtos = obter_lista_produtos()
    if not produtos:
        messagebox.showwarning("Aviso", "Cadastre produtos primeiro para gerar o gráfico!")
        return
        
    # Separando em duas listas usando o laço for 
    nomes_produtos = []
    quantidades = []
    for p in produtos:
        nomes_produtos.append(p[1])
        quantidades.append(p[3]) # Gráfico baseado na quantidade em estoque
        
    # Criando a figura do Matplotlib
    fig, ax = plt.subplots(figsize=(4, 3), dpi=100)
    fig.patch.set_facecolor('#2b2b2b') # Cor de fundo combinando com o CustomTkinter Dark
    ax.set_facecolor('#2b2b2b')
    
    # Desenhando as barras
    ax.bar(nomes_produtos, quantidades, color='#1f6aa5')
    ax.set_title("Quantidade em Estoque", color='white', fontsize=12)
    ax.tick_params(colors='white')
    
    # Se já existir um gráfico na tela, remove ele antes de desenhar o novo
    if canvas_grafico:
        canvas_grafico.get_tk_widget().destroy()
        
    #  FigureCanvasTkAgg
    canvas_grafico = FigureCanvasTkAgg(fig, master=frame_direita)
    canvas_grafico.draw()
    canvas_grafico.get_tk_widget().pack(pady=10, fill="both", expand=True)
    plt.close(fig) # Fecha a figura para liberar memória

def iniciar_janela_principal():
    global cx_produto, cx_preco, cx_quantidade, txt_listagem, frame_direita

    ctk.set_appearance_mode("dark")
    janela = ctk.CTk()
    janela.title("Sistema - Gestão de Inventário")
    janela.geometry("900x550")

    
    frame_esquerda = ctk.CTkFrame(janela, width=400)
    frame_esquerda.pack(side="left", padx=10, pady=10, fill="both", expand=True)

    frame_direita = ctk.CTkFrame(janela, width=450)
    frame_direita.pack(side="right", padx=10, pady=10, fill="both", expand=True)

    # --- CONTEÚDO DA ESQUERDA: Formulário e Cadastro ---
    lbl_titulo = ctk.CTkLabel(frame_esquerda, text="Cadastrar Produtos", font=("Arial", 16, "bold"))
    lbl_titulo.pack(pady=15)

    cx_produto = ctk.CTkEntry(frame_esquerda, placeholder_text="Nome do produto...", width=250)
    cx_produto.pack(pady=8)

    cx_preco = ctk.CTkEntry(frame_esquerda, placeholder_text="Preço do produto...", width=250)
    cx_preco.pack(pady=8)

    cx_quantidade = ctk.CTkEntry(frame_esquerda, placeholder_text="Quantidade...", width=250)
    cx_quantidade.pack(pady=8)

    btn_salvar = ctk.CTkButton(frame_esquerda, text="Gravar Produto", command=botao_gravar_produto)
    btn_salvar.pack(pady=15)

    # Listagem de produtos 
    lbl_lista = ctk.CTkLabel(frame_esquerda, text="Produtos Cadastrados:", font=("Arial", 12, "bold"))
    lbl_lista.pack(pady=5)
    
    txt_listagem = ctk.CTkTextbox(frame_esquerda, width=350, height=180)
    txt_listagem.pack(pady=5)
    
    # --- CONTEÚDO DA DIREITA: Dashboard ---
    lbl_dash = ctk.CTkLabel(frame_direita, text="Dashboard", font=("Arial", 16, "bold"))
    lbl_dash.pack(pady=15)
    
    btn_grafico = ctk.CTkButton(frame_direita, text="Gerar e Atualizar Gráfico", command=gerar_dashboard, fg_color="green", hover_color="darkgreen")
    btn_grafico.pack(pady=10)

    # Carrega a lista logo ao abrir o programa
    atualizar_listagem()

    janela.mainloop()