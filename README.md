# Organizador-Automatico

#  Organizador de Arquivos Inteligente em Python

Este projeto é um script de automação que organiza arquivos em uma pasta com base em suas extensões, movendo-os para subpastas categorizadas. O projeto foi desenvolvido em etapas, evoluindo de um script manual para uma ferramenta com interface gráfica e monitoramento em tempo real.

##  Funcionalidades

O projeto foi construído nas seguintes versões:
* **v1 (Manual):** Um script simples que organiza a pasta quando executado.
* **v2 (Tempo Real):** Utiliza a biblioteca `watchdog` para monitorar a pasta e organizar novos arquivos automaticamente.
* **v3 (Interface Gráfica):** Uma GUI feita com `PySimpleGUI` que permite ao usuário escolher a pasta e iniciar a organização.
* **v4 (Logs):** Adiciona um sistema de logs para registrar todas as ações de movimentação de arquivos.
* **v5 (Histórico e Desfazer):** Salva um histórico das movimentações e permite reverter a última organização.

##  Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Bibliotecas:**
    * `watchdog` (para monitoramento de arquivos)
    * `PySimpleGUI` (para a interface gráfica)

##  Como Usar

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/SEU-USUARIO/nome-do-repositorio.git](https://github.com/SEU-USUARIO/nome-do-repositorio.git)
    ```

2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3.  Execute a versão desejada. Por exemplo, para a versão com interface gráfica:
    ```bash
    python organizador_v3_gui.py
    ```

4.  **Importante:** Lembre-se de alterar a variável `PASTA_PARA_ORGANIZAR` nos scripts que não possuem interface gráfica para o caminho da pasta que você deseja organizar.
