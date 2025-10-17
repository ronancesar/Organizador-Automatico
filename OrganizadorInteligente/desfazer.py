import os
import shutil
import json

PASTA_ORGANIZADA = "C:/Users/Ronan/Downloads"
ARQUIVO_HISTORICO = os.path.join(PASTA_ORGANIZADA, "historico.json")

def desfazer_organizacao():
    try:
        with open(ARQUIVO_HISTORICO, "r") as f:
            historico = json.load(f)
    except FileNotFoundError:
        print("Erro: Arquivo 'historico.json' não encontrado. Nenhuma ação para desfazer.")
        return

    if not historico:
        print("Nenhuma movimentação registrada no histórico.")
        return

    print("Iniciando processo de desfazer...")
    for movimento in reversed(historico):
        try:
            shutil.move(movimento["de"], movimento["para"])
            print(f"Moveu de volta: '{os.path.basename(movimento['de'])}'")
        except FileNotFoundError:
            print(f"Aviso: Arquivo '{os.path.basename(movimento['de'])}' não encontrado. Pulando.")
        except Exception as e:
            print(f"Erro ao mover '{os.path.basename(movimento['de'])}': {e}")
            
    os.remove(ARQUIVO_HISTORICO)
    print("\nAção de desfazer concluída. O histórico foi limpo.")

if __name__ == "__main__":
    desfazer_organizacao()