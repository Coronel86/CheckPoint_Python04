# CheckPoint_Python04

# 🚀 Sistema de Gestão de Inventário (ERP)
**Desenvolvedor:** Heberton Henrique Coronel da Silva  
**Status do Projeto:** ✅ Concluído

---

## 📝 Descrição do Projeto
O **Sistema de Gestão de Inventário** é uma solução baseada no conceito de ERP (Planejamento de Recursos Empresariais) desenvolvida em Python. O software foi projetado para atender às necessidades de comércios locais (como uma Fruteira de exemplo), permitindo o cadastramento de produtos, controle rigoroso de estoque e acompanhamento de dados financeiros de forma automatizada e segura.

O projeto utiliza o padrão de arquitetura **MVC (Model-View-Controller)** para garantir a modularização, organização e fácil manutenção do código.

---

## ✨ Funcionalidades Principais
* ⚙️ **Criação e Leitura:** Controle de estoque com rotinas para Adicionar, Listar os produtos.
* 🛡️ **Segurança Avançada:** Proteção contra ataques de *SQL Injection* utilizando marcadores seguros (`?, ?`) nas consultas ao banco de dados.
* 📊 **Dashboard Integrado:** Relatórios visuais gerados em tempo real com gráficos de barras exibindo a quantidade e os nomes dos produtos em estoque.
* 🔍 **Interface Moderna:** Janela gráfica responsiva, intuitiva e de alto padrão visual desenvolvida com CustomTkinter.
* 📦 **Portabilidade:** Sistema compilado e pronto para execução direta no Windows (`.exe`).

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Categoria / Utilidade |
| :--- | :--- |
| **Python 3.10** | Linguagem principal de desenvolvimento |
| **SQLite3** | Banco de dados relacional embutido para persistência permanente |
| **CustomTkinter** | Biblioteca de interface gráfica moderna (GUI) |
| **Matplotlib** | Geração e plotagem de gráficos de barras do Dashboard |
| **Git & GitHub** | Ferramentas de controle de versão e hospedagem do código |

---

## 📐 Arquitetura do Projeto (MVC)

O código foi rigorosamente dividido para respeitar a separação de responsabilidades (Regra: código não unificado em arquivo único) e está distribuído na seguinte estrutura de arquivos:

* **`config/init_banco.py`:** Script responsável por preparar o ambiente local, garantindo a inicialização automatizada e a criação da estrutura de tabelas corretas dentro do arquivo `banco.db`.

* **`Modelos/modelo.py` (Model):** O banco de dados. Contém toda a lógica de comunicação direta com o `sqlite3`. Responsável por conectar, criar tabelas e executar comandos SQL (`INSERT`, `SELECT`, `UPDATE`) de forma segura utilizando *Prepared Statements* com marcadores seguros (`?, ?`) para prevenir ataques de Injeção SQL.

* **`controladores/controlador.py` (Controller):** O cérebro do sistema. Faz a ponte segura entre a Interface (`Visualizar/tela.py`) e o Modelo (`Modelos/modelo.py`). Realiza validações críticas: se os campos estiverem vazios, retorna `False`, "Campos vazios". Utiliza blocos `try/except` para converter preço para `float`. Se tudo estiver correto, chama o Modelo e retorna `True`.

* **`Visualizar/tela.py` (View):** A interface de usuário. Importa o `customtkinter` e as funções do controlador para desenhar o formulário de entrada (Nome, Preço, Qtd). Possui o botão "Gravar Produto", cuja função envia os dados capturados via `.get()` e exibe um `messagebox` baseado na resposta. Organiza a janela de forma profissional com `CTkFrame`, gerencia uma listagem atualizável de produtos e renderiza o Dashboard do `Matplotlib` através da biblioteca `FigureCanvasTkAgg` com a lógica de separar os dados buscados do modelo em duas listas usando um laço `for`.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Antes de começar, certifique-se de ter instalado em sua máquina:
* [Python 3.10 ou superior](https://www.python.org/)
* [Git](https://git-scm.com/)

### Passos para Instalação e Execução

1. Clone este repositório para a sua máquina local:
   ```bash
   git clone [https://github.com/Coronel86/CheckPoint_Python04.git](https://github.com/Coronel86/CheckPoint_Python04.git)