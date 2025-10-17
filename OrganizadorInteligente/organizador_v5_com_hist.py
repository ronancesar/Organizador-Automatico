import os
import shutil
import logging
import json

PASTA_PARA_ORGANIZAR = "C:/Users/SEU_USUARIO/Downloads"
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
    handlers=[logging.FileHandler(ARQUIVO_DE_LOG), logging.StreamHandler()]
)

def organizar_e_salvar_historico(caminho):
    logging.info("Iniciando organização e salvando histórico...")
    historico_movimentacoes = []
    
    for nome_arquivo in os.listdir(caminho):
        caminho_original = os.path.join(caminho, nome_arquivo)

        if os.path.isdir(caminho_original) or nome_arquivo in ["organizador.log", "historico.json", "desfazer.py"]:
            continue
        
        _, extensao = os.path.splitext(nome_arquivo)
        pasta_destino = "Outros"
        for nome_pasta, extensoes in MAPA_EXTENSOES.items():
            if extensao.lower() in extensoes:
                pasta_destino = nome_pasta
                break

        caminho_destino_pasta = os.path.join(caminho, pasta_destino)
        caminho_novo = os.path.join(caminho_destino_pasta, nome_arquivo)

        if not os.path.exists(caminho_destino_pasta):
            os.makedirs(caminho_destino_pasta)
        
        shutil.move(caminho_original, caminho_novo)
        logging.info(f"Moveu: '{nome_arquivo}' -> '{pasta_destino}'")
        
        historico_movimentacoes.append({
            "de": caminho_novo,
            "para": caminho_original
        })

    with open(os.path.join(caminho, "historico.json"), "w") as f:
        json.dump(historico_movimentacoes, f, indent=4)
        
    logging.info("Histórico da organização salvo em 'historico.json'")

if __name__ == "__main__":
    organizar_e_salvar_historico(PASTA_PARA_ORGANIZAR)