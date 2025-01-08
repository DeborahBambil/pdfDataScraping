#!/usr/bin/ python3

from PyPDF2 import PdfReader

def extrair_texto_pdf(caminho_pdf):
    leitor = PdfReader(caminho_pdf)
    texto = ''
    for pagina in range(len(leitor.pages)):
        texto += leitor.pages[pagina].extract_text()
    return texto

caminho_pdf = input("Digite o caminho do arquivo PDF: ")
texto = extrair_texto_pdf(caminho_pdf)

with open('texto_extraido.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(texto)

print("Texto salvo em texto_extraido.txt")