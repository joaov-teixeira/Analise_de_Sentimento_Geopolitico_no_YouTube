import pandas as pd
import unicodedata
import re
import os
import langdetect

# OPCIONAL: Se quiser filtrar idiomas, instale: pip install langdetect
try:
    from langdetect import detect, DetectorFactory
    DetectorFactory.seed = 0
    HAS_LANGDETECT = True
except ImportError:
    HAS_LANGDETECT = False

def limpeza_profunda(texto):
    if not isinstance(texto, str) or texto.strip() == "":
        return ""

    # 1. Filtro de Idioma (Opcional, mas recomendado para o seu caso)
    if HAS_LANGDETECT:
        try:
            if detect(texto) != 'pt': # Mantém apenas Português
                return "___EXCLUIR___"
        except:
            pass

    # 2. Conversão para minúsculo absoluta
    texto = texto.lower()

    # 3. Remoção de Acentos (NFKD + filtragem de caracteres não-ASCII)
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ASCII', 'ignore').decode('ASCII')

    # 4. Regex Agressivo: Mantém apenas letras e espaços
    # Isso remove emojis, pontuação excessiva e caracteres especiais que o SentiStrength ignora
    texto = re.sub(r'[^a-z\s]', '', texto)

    # 5. Remoção de espaços extras
    texto = " ".join(texto.split())

    return texto

def processar():
    caminho_entrada = 'files/comments_info.csv'
    caminho_saida = 'files/comments_ultra_cleaned.csv'
    
    # Colunas que você confirmou ter no seu CSV
    colunas = ['video_id', 'comment', 'published_at', 'like_count']
    
    print("Iniciando limpeza profunda de 1.7M de linhas...")
    
    # Processamento em pedaços (chunks) para não estourar a RAM
    chunks = pd.read_csv(caminho_entrada, usecols=colunas, chunksize=100000)
    
    primeira_vez = True
    for chunk in chunks:
        # Aplica a limpeza
        chunk['text_cleaned'] = chunk['comment'].apply(limpeza_profunda)
        
        # Remove os que foram marcados como estrangeiros ou que ficaram vazios
        chunk = chunk[chunk['text_cleaned'] != "___EXCLUIR___"]
        chunk = chunk[chunk['text_cleaned'].str.len() > 2]
        
        # Salva mantendo os metadados que você precisa para o relatório
        chunk.to_csv(caminho_saida, mode='a', index=False, header=primeira_vez, encoding='utf-8')
        primeira_vez = False
        print(f"Processados +100k linhas...")

    print(f"Limpeza concluída! Verifique o arquivo: {caminho_saida}")

if __name__ == "__main__":
    processar()