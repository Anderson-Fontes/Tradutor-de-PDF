# 📄 Tradutor de PDFs

> Pipeline completo para **fatiar, traduzir e reunir** documentos PDF do inglês para o português — tudo de forma automática, local e gratuita.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Como Funciona](#-como-funciona)
- [Estrutura de Arquivos](#-estrutura-de-arquivos)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Detalhes Técnicos](#-detalhes-técnicos)
- [Limitações Conhecidas](#-limitações-conhecidas)
- [Solução de Problemas](#-solução-de-problemas)
- [Contribuindo](#-contribuindo)
- [Licença](#-licença)

---

## 🧠 Sobre o Projeto

O **Tradutor de PDFs** é uma solução em Python criada para quem precisa traduzir documentos PDF extensos do inglês para o português sem depender de serviços pagos ou ferramentas online com limitação de tamanho.

O problema que ele resolve é simples: a maioria dos tradutores online tem um limite de páginas por arquivo. Este projeto contorna isso **dividindo o PDF em blocos menores**, traduzindo cada um separadamente e, ao final, **reunindo tudo em um único documento traduzido**.

**Principais características:**

- ✅ Tradução automática via Google Tradutor (gratuito, sem API key)
- ✅ Suporte a PDFs de qualquer tamanho
- ✅ Retomada automática — se o processo cair, ele continua de onde parou
- ✅ Tradução de textos em parágrafos e em tabelas
- ✅ 100% local, sem envio de dados para servidores externos (exceto a tradução em si)

---

## ⚙️ Como Funciona

O projeto segue um pipeline de **3 etapas sequenciais**:

```
┌─────────────────┐     ┌─────────────────────┐     ┌───────────────────┐
│  1. FATIAR      │────▶│  2. TRADUZIR         │────▶│  3. JUNTAR        │
│  cortar_pdf.py  │     │  tradutor.py         │     │  juntar_pdf.py    │
│                 │     │                      │     │                   │
│ arquivo1.pdf    │     │ parte_1.pdf → docx   │     │ traduzido_parte_1 │
│   ↓             │     │ docx → tradução      │     │ traduzido_parte_2 │
│ parte_1.pdf     │     │ tradução → pdf       │     │ traduzido_parte_3 │
│ parte_2.pdf     │     │ parte_2.pdf → ...    │     │        ↓          │
│ parte_3.pdf     │     │                      │     │  Documento_Final  │
│ ...             │     │ traduzido_parte_X.pdf│     │  _Traduzido.pdf   │
└─────────────────┘     └─────────────────────┘     └───────────────────┘
```

**Etapa 1 — Fatiar (`cortar_pdf.py`):** Divide o PDF original em blocos de 30 páginas cada, gerando arquivos `parte_1.pdf`, `parte_2.pdf`, etc.

**Etapa 2 — Traduzir (`tradutor.py`):** Para cada `parte_X.pdf`, converte para DOCX (preservando a estrutura), traduz parágrafo a parágrafo usando o Google Tradutor e reconverte para PDF, gerando `traduzido_parte_X.pdf`. Se um arquivo já foi traduzido, ele é pulado automaticamente.

**Etapa 3 — Juntar (`juntar_pdf.py`):** Une todos os `traduzido_parte_X.pdf` em ordem numérica correta, gerando o arquivo `Documento_Final_Traduzido.pdf`.

---

## 📁 Estrutura de Arquivos

```
Tradutor de PDFs/
│
├── cortar_pdf.py        # Etapa 1: divide o PDF original em partes menores
├── tradutor.py          # Etapa 2: traduz cada parte de inglês para português
├── juntar_pdf.py        # Etapa 3: reúne todos os PDFs traduzidos em um só
│
├── arquivo1.pdf         # ← Coloque seu PDF aqui (ou ajuste o nome no script)
│
├── parte_1.pdf          # Gerados automaticamente pelo cortar_pdf.py
├── parte_2.pdf
├── ...
│
├── traduzido_parte_1.pdf  # Gerados automaticamente pelo tradutor.py
├── traduzido_parte_2.pdf
├── ...
│
└── Documento_Final_Traduzido.pdf  # Resultado final gerado pelo juntar_pdf.py
```

> **Dica:** Os arquivos intermediários (`parte_X.pdf` e `traduzido_parte_X.pdf`) podem ser deletados após a conclusão com sucesso.

---

## 🔧 Pré-requisitos

- **Python 3.8 ou superior**
- **pip** (gerenciador de pacotes do Python)
- Conexão com a internet (para a etapa de tradução)
- **Microsoft Word** instalado *(necessário para o `docx2pdf` no Windows)*  
  → Em Linux/Mac, use LibreOffice como alternativa (veja [Solução de Problemas](#-solução-de-problemas))

---

## 🚀 Instalação

**1. Clone o repositório:**

```bash
git clone https://github.com/Anderson-Fontes/Tradutor-de-PDF.git
cd "Tradutor-de-PDF/Tradutor de PDFs"
```

**2. (Recomendado) Crie um ambiente virtual:**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install PyMuPDF pdf2docx python-docx deep-translator docx2pdf
```

| Biblioteca | Função |
|---|---|
| `PyMuPDF` | Leitura, divisão e junção de arquivos PDF |
| `pdf2docx` | Conversão de PDF para DOCX preservando a estrutura |
| `python-docx` | Leitura e edição de arquivos DOCX |
| `deep-translator` | Interface com o Google Tradutor (gratuito) |
| `docx2pdf` | Conversão de DOCX de volta para PDF |

---

## 📖 Como Usar

### Passo 1 — Prepare seu arquivo

Coloque o PDF que deseja traduzir na mesma pasta dos scripts. O nome padrão esperado é `arquivo1.pdf`.

Se o seu arquivo tiver outro nome, abra o `cortar_pdf.py` e altere esta linha:

```python
arquivo_original = "arquivo1.pdf"  # ← Mude para o nome do seu arquivo
```

Você também pode ajustar o tamanho dos blocos (padrão: 30 páginas):

```python
paginas_por_bloco = 30  # ← Aumente ou diminua conforme necessário
```

---

### Passo 2 — Execute a Etapa 1: Fatiar

```bash
python cortar_pdf.py
```

**O que acontece:** O script lê o PDF original e gera arquivos `parte_1.pdf`, `parte_2.pdf`, etc. na mesma pasta.

**Saída esperada no terminal:**
```
Fatiando o PDF...
Salvo: parte_1.pdf
Salvo: parte_2.pdf
Salvo: parte_3.pdf
Pronto! PDF dividido com sucesso.
```

---

### Passo 3 — Execute a Etapa 2: Traduzir

```bash
python tradutor.py
```

> ⚠️ **Esta etapa pode demorar bastante**, dependendo do tamanho do documento e da velocidade da sua conexão. Para um PDF de 90 páginas (3 partes), espere entre 10 e 30 minutos.

**O que acontece:** Para cada `parte_X.pdf`, o script realiza as seguintes sub-etapas:
1. Converte o PDF para DOCX
2. Traduz cada parágrafo e célula de tabela via Google Tradutor
3. Reconverte o DOCX traduzido para PDF
4. Salva como `traduzido_parte_X.pdf`

**Saída esperada no terminal:**
```
Encontrados 3 arquivos para traduzir. Iniciando a fila...

Iniciando: parte_1.pdf...
1/4 - Convertendo para DOCX...
2/4 - Traduzindo o conteúdo...
3/4 - Reconstruindo o arquivo PDF...
4/4 - Concluído! Salvo como: traduzido_parte_1.pdf

Iniciando: parte_2.pdf...
...

TODOS OS ARQUIVOS FORAM TRADUZIDOS COM SUCESSO!
```

> 💡 **Se o processo cair no meio:** basta rodar `python tradutor.py` novamente. Os arquivos já traduzidos serão pulados automaticamente.

---

### Passo 4 — Execute a Etapa 3: Juntar

```bash
python juntar_pdf.py
```

**O que acontece:** O script localiza todos os `traduzido_parte_X.pdf`, os une em ordem correta e gera o arquivo final.

**Saída esperada no terminal:**
```
Buscando as partes traduzidas...
Encontrados 3 arquivos. Iniciando a fusão...
Adicionando: traduzido_parte_1.pdf
Adicionando: traduzido_parte_2.pdf
Adicionando: traduzido_parte_3.pdf

Sucesso absoluto! O seu arquivo completo foi salvo como: Documento_Final_Traduzido.pdf
```

---

### ✅ Resultado

O arquivo `Documento_Final_Traduzido.pdf` estará na mesma pasta, contendo o documento completo traduzido para o português.

---

## 🔬 Detalhes Técnicos

### Por que dividir em partes?

O Google Tradutor tem limites de caracteres por requisição. Dividir o PDF em blocos menores garante que cada tradução fique dentro do limite, evitando erros silenciosos (texto não traduzido) ou exceções.

### Por que converter para DOCX antes de traduzir?

A biblioteca `pdf2docx` consegue extrair o texto do PDF de forma estruturada — preservando parágrafos, colunas e tabelas. Isso permite que a tradução seja aplicada elemento a elemento, com muito mais fidelidade do que uma extração de texto puro.

### A ordenação numérica importa

Sem ordenação explícita, sistemas operacionais ordenam arquivos alfabeticamente: `parte_1`, `parte_10`, `parte_2`... O script usa `sort(key=lambda x: int(...))` para garantir a ordem numérica correta, evitando um PDF final fora de sequência.

### Retomada automática

O `tradutor.py` verifica se `traduzido_parte_X.pdf` já existe antes de processar `parte_X.pdf`. Isso torna o processo resiliente a interrupções.

---

## ⚠️ Limitações Conhecidas

- **Qualidade da tradução:** A tradução é automática (Google Tradutor) e pode não ser perfeita para textos técnicos, jurídicos ou com terminologia especializada. Recomenda-se revisão humana posterior.
- **Formatação:** PDFs com layouts muito complexos (múltiplas colunas, imagens com texto sobreposto, cabeçalhos e rodapés elaborados) podem perder formatação na conversão PDF → DOCX → PDF.
- **PDFs escaneados:** Documentos que são imagens digitalizadas (sem camada de texto selecionável) **não são suportados**. É necessário aplicar OCR antes de usar este pipeline.
- **Velocidade:** O processo é sequencial e pode ser lento para documentos muito grandes (200+ páginas). Não há paralelização implementada.
- **Dependência do Word (Windows):** O `docx2pdf` no Windows requer Microsoft Word instalado. Sem ele, a etapa 3/4 do tradutor falhará.

---

## 🛠️ Solução de Problemas

**`ModuleNotFoundError: No module named 'fitz'`**
```bash
pip install PyMuPDF
```

**`docx2pdf` falha no Linux/macOS**

Instale o LibreOffice e use-o como backend:
```bash
# Ubuntu/Debian
sudo apt install libreoffice

# macOS
brew install libreoffice
```
Depois, substitua `convert(docx_traduzido, arquivo_saida)` por:
```python
import subprocess
subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', docx_traduzido])
```

**A tradução parou no meio**

Simplesmente rode `python tradutor.py` novamente. Os arquivos já concluídos serão pulados.

**O PDF final está fora de ordem**

Verifique se todos os arquivos `traduzido_parte_X.pdf` estão na pasta e se os nomes seguem o padrão exato `traduzido_parte_1.pdf`, `traduzido_parte_2.pdf`, etc.

**Erro de limite do Google Tradutor (429 Too Many Requests)**

Reduza o tamanho dos blocos em `cortar_pdf.py`:
```python
paginas_por_bloco = 15  # Tente com blocos menores
```
Ou adicione um `time.sleep(1)` dentro do loop de tradução de parágrafos.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Se você encontrou um bug, tem uma sugestão de melhoria ou quer adicionar uma nova funcionalidade:

1. Faça um **fork** do repositório
2. Crie uma branch para sua feature: `git checkout -b minha-melhoria`
3. Faça suas alterações e commit: `git commit -m 'Adiciona suporte a OCR'`
4. Envie para o seu fork: `git push origin minha-melhoria`
5. Abra um **Pull Request** descrevendo o que foi feito

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">Feito com ☕ e Python por <a href="https://github.com/Anderson-Fontes">Anderson Fontes</a></p>
