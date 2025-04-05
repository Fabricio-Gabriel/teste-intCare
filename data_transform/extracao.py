import camelot
import pandas as pd
import zipfile
import os

pdf_file = '../web_scraping/anexo_1_rol.pdf'
tables = camelot.read_pdf(pdf_file, pages='all', flavor='stream')

if not tables:
    raise ValueError("Nenhuma tabela encontrada no PDF.")


df_list = [t.df for t in tables]
df_raw = pd.concat(df_list, ignore_index=True)


header_idx = None
for idx, row in df_raw.iterrows():
    if row.iloc[0].strip().upper() == "PROCEDIMENTO":
        header_idx = idx
        break

if header_idx is None:
    raise ValueError("Linha de cabeçalho não encontrada no DataFrame.")

df_valid = df_raw.iloc[header_idx:].reset_index(drop=True)
new_header = df_valid.iloc[0]
df_valid = df_valid[1:].reset_index(drop=True)
df_valid.columns = new_header

rename_dict = {
    'OD': 'Seg. Odontológica',
    'AMB': 'Seg. Ambulatorial'
}
df_valid.rename(columns=rename_dict, inplace=True)


csv_file = 'dados_extraidos.csv'
df_valid.to_csv(csv_file, index=False, encoding='utf-8-sig')
print(f"CSV salvo em: {os.path.abspath(csv_file)}")

seu_nome = "fabricio_melquiades"
zip_filename = f"Teste_{seu_nome}.zip"
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(csv_file, arcname=os.path.basename(csv_file))
print(f"Arquivo ZIP criado: {os.path.abspath(zip_filename)}")