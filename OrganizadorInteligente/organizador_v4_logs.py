import os
import shutil
import logging

PASTA_PARA_ORGANIZAR = "C:/Users/Ronan/Downloads"
ARQUIVO_DE_LOG = os.path.join(PASTA_PARA_ORGANIZAR, "organizador.log")
MAPA_EXTENSOES = {
    "Imagens": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Musicas": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z", ".gz"],
    "Executaveis": [".exe", ".msi"]
}

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(ARQUIVO_DE_LOG),
        logging.StreamHandler()
    ]
)

def organizar_pasta_com_log(caminho):
    logging.info(f"Iniciando organização da pasta: {caminho}")
    
    for nome_arquivo in os.listdir(caminho):
        caminho_original_arquivo = os.path.join(caminho, nome_arquivo)
        
        if os.path.isdir(caminho_original_arquivo) or nome_arquivo == "organizador.log":
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
            logging.info(f"Pasta '{pasta_destino}' criada.")
        
        caminho_novo_arquivo = os.path.join(caminho_pasta_destino, nome_arquivo)
        
        try:
            shutil.move(caminho_original_arquivo, caminho_novo_arquivo)
            logging.info(f"Moveu: '{nome_arquivo}' -> para a pasta '{pasta_destino}'")
        except Exception as e:
            logging.error(f"ERRO ao mover '{nome_arquivo}': {e}")

    logging.info("Organização concluída!")

if __name__ == "__main__":
    organizar_pasta_com_log(PASTA_PARA_ORGANIZAR)