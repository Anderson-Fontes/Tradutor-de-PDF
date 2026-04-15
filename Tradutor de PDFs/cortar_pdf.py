import fitz  # Esta é a biblioteca PyMuPDF que já foi instalada

arquivo_original = "arquivo1.pdf" # Mude para o nome do seu arquivo
paginas_por_bloco = 30

print("Fatiando o PDF...")
doc = fitz.open(arquivo_original)

for i in range(0, len(doc), paginas_por_bloco):
    novo_doc = fitz.open()
    # Pega um bloco de 40 páginas
    fim = min(i + paginas_por_bloco - 1, len(doc) - 1)
    novo_doc.insert_pdf(doc, from_page=i, to_page=fim)
    
    # Salva como parte_1.pdf, parte_2.pdf, etc.
    nome_saida = f"parte_{i // paginas_por_bloco + 1}.pdf"
    novo_doc.save(nome_saida)
    novo_doc.close()
    print(f"Salvo: {nome_saida}")

print("Pronto! PDF dividido com sucesso.")