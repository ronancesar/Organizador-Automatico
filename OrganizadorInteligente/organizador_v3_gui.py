import os
import shutil
import PySimpleGUI as sg

def organizar_pasta(caminho, window):
    MAPA_EXTENSOES = {
        "Imagens": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".svg"],
        "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Musicas": [".mp3", ".wav", ".flac"],
        "Compactados": [".zip", ".rar", ".7z", ".gz"],
        "Executaveis": [".exe", ".msi"]
    }
    
    try:
        arquivos_movidos = 0
        for nome_arquivo in os.listdir(caminho):
            caminho_completo = os.path.join(caminho, nome_arquivo)
            if os.path.isdir(caminho_completo):
                continue

            _, extensao = os.path.splitext(nome_arquivo)
            extensao = extensao.lower()

            if not extensao:
                continue

            pasta_destino = "Outros"
            for nome_pasta, extensoes in MAPA_EXTENSOES.items():
                if extensao in extensoes:
                    pasta_destino = nome_pasta
                    break
            
            caminho_pasta_destino = os.path.join(caminho, pasta_destino)
            if not os.path.exists(caminho_pasta_destino):
                os.makedirs(caminho_pasta_destino)
            
            shutil.move(caminho_completo, os.path.join(caminho_pasta_destino, nome_arquivo))
            window['-LOG-'].print(f"Moveu: '{nome_arquivo}' -> para a pasta '{pasta_destino}'")
            arquivos_movidos += 1
        
        sg.popup('Sucesso!', f'{arquivos_movidos} arquivos foram organizados.')
    except Exception as e:
        sg.popup('Erro!', f'Ocorreu um erro durante a organização: {e}')

sg.theme('DarkAmber')

layout = [
    [sg.Text('Selecione a pasta que deseja organizar')],
    [sg.Input(key='-PASTA-'), sg.FolderBrowse('Procurar')],
    [sg.Button('Organizar', key='-ORGANIZAR-'), sg.Button('Sair')],
    [sg.Text('Log de Atividade:')],
    [sg.Multiline(size=(60, 15), key='-LOG-', disabled=True, autoscroll=True)]
]

window = sg.Window('Organizador de Arquivos Inteligente', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    
    if event == '-ORGANIZAR-':
        pasta_selecionada = values['-PASTA-']
        if pasta_selecionada and os.path.isdir(pasta_selecionada):
            window['-LOG-'].update('')
            organizar_pasta(pasta_selecionada, window)
        else:
            sg.popup('Erro!', 'Por favor, selecione uma pasta válida antes de organizar.')

window.close()