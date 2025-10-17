import os
import shutil

PASTA_PARA_ORGANIZAR = "C:/Users/Ronan/Downloads" 

#Acho que foi todas extensoes
MAPA_EXTENSOES = {
    "Imagens": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Musicas": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z", ".gz"],
    "Executaveis": [".exe", ".msi"]
}

def organizar_pasta(caminho):
    print(f"Iniciando organização da pasta: {caminho}")
    
    for nome_arquivo in os.listdir(caminho):
        caminho_original_arquivo = os.path.join(caminho, nome_arquivo)

        if os.path.isdir(caminho_original_arquivo):
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
            print(f"Pasta '{pasta_destino}' criada.")
        
        caminho_novo_arquivo = os.path.join(caminho_pasta_destino, nome_arquivo)
        
        try:
            shutil.move(caminho_original_arquivo, caminho_novo_arquivo)
            print(f"Moveu: '{nome_arquivo}' -> para a pasta '{pasta_destino}'")
        except Exception as e:
            print(f"ERRO ao mover '{nome_arquivo}': {e}")

    print("\nOrganização concluída!")

if __name__ == "__main__":
    organizar_pasta(PASTA_PARA_ORGANIZAR)