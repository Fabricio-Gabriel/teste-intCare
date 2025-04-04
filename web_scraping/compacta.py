import os
import zipfile
import shutil

origem = "C:/Users/fabri/PycharmProjects/teste-intCare/web_scraping"
destino = "C:/Users/fabri/anexos_teste"
zip_nome = "anexos_teste.zip"
pasta_externa = "C:/Users/fabri/PycharmProjects/teste-intCare/Anexos/"

os.makedirs(destino, exist_ok=True)

for arquivo in os.listdir(origem):
    if arquivo[0] == 'a':
        caminho_arquivo = os.path.join(origem, arquivo)
        if os.path.isfile(caminho_arquivo):
            shutil.copy2(caminho_arquivo, destino)

with zipfile.ZipFile(zip_nome, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for pasta_raiz, _, arquivos in os.walk(destino):
        for arquivo in arquivos:
            caminho_completo = os.path.join(pasta_raiz, arquivo)
            caminho_relativo = os.path.relpath(caminho_completo, destino)
            zipf.write(caminho_completo, arcname=caminho_relativo)

shutil.move(zip_nome, os.path.join(pasta_externa, zip_nome))

print(f"Pasta '{destino}' foi compactada para '{zip_nome}' com sucesso")
