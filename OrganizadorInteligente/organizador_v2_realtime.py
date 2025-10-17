import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

PASTA_PARA_ORGANIZAR = "C:/Users/Ronan/Downloads" 
MAPA_EXTENSOES = {
    "Imagens": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Musicas": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z", ".gz"],
    "Executaveis": [".exe", ".msi"]
}

class OrganizadorHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        time.sleep(1) 
        self.organizar_arquivo(event.src_path)

    def organizar_arquivo(self, caminho_arquivo):
        nome_arquivo = os.path.basename(caminho_arquivo)
        _, extensao = os.path.splitext(nome_arquivo)
        extensao = extensao.lower()

        if extensao in [".tmp", ".crdownload", ".part"]:
            print(f"Ignorando arquivo temporário: {nome_arquivo}")
            return

        if not extensao:
            return

        pasta_destino = "Outros"
        for nome_pasta, extensoes in MAPA_EXTENSOES.items():
            if extensao in extensoes:
                pasta_destino = nome_pasta
                break
        
        caminho_pasta_destino = os.path.join(os.path.dirname(caminho_arquivo), pasta_destino)

        if not os.path.exists(caminho_pasta_destino):
            os.makedirs(caminho_pasta_destino)
            print(f"Pasta '{pasta_destino}' criada.")

        caminho_novo_arquivo = os.path.join(caminho_pasta_destino, nome_arquivo)
        
        try:
            shutil.move(caminho_arquivo, caminho_novo_arquivo)
            print(f"Automático | Moveu: '{nome_arquivo}' -> para a pasta '{pasta_destino}'")
        except Exception as e:
            print(f"ERRO ao mover '{nome_arquivo}': {e}")


if __name__ == "__main__":
    print(f"Iniciando monitoramento em tempo real da pasta: {PASTA_PARA_ORGANIZAR}")
    print("Pressione CTRL+C para parar.")

    event_handler = OrganizadorHandler()
    observer = Observer()
    observer.schedule(event_handler, PASTA_PARA_ORGANIZAR, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("Monitoramento encerrado.")   