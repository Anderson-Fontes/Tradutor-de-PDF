import fitz  # PyMuPDF
import glob
import os

print("Buscando as partes traduzidas...")

# Pega todos os arquivos que começam com "traduzido_parte_"
arquivos = glob.glob("traduzido_parte_*.pdf")

# Se não encontrar nada, avisa e para o script
if not arquivos:
    print("Nenhum arquivo 'traduzido_parte_X.pdf' foi encontrado nesta pasta.")
    exit()

# PASSO IMPORTANTE: Ordenar numericamente! 
# Sem isso, o computador junta a parte 1 com a 10, depois a 2...
try:
    arquivos.sort(key=lambda x: int(x.split('_')[2].split('.')[0]))
except Exception as e:
    print(f"Erro ao ordenar os arquivos. Verifique os nomes. Erro: {e}")
    exit()

print(f"Encontrados {len(arquivos)} arquivos. Iniciando a fusão...")

# Cria um PDF novo e vazio
pdf_final = fitz.open()

# Vai abrindo cada pedaço e colando no PDF final
for arquivo in arquivos:
    print(f"Adicionando: {arquivo}")
    pdf_temp = fitz.open(arquivo)
    pdf_final.insert_pdf(pdf_temp)
    pdf_temp.close()

# Salva o resultado final
nome_final = "Documento_Final_Traduzido.pdf"
pdf_final.save(nome_final)
pdf_final.close()

print(f"\nSucesso absoluto! O seu arquivo completo foi salvo como: {nome_final}")