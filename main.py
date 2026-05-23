from visualizar.tela import iniciar_janela_principal

from config.init_banco import criar_tabela


if __name__ == "__main__":
    criar_tabela()
    iniciar_janela_principal()