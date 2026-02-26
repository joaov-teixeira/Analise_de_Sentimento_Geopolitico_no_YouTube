import pandas as pd
import re
import os

def categorizar_v5():
    caminho_entrada = 'files/comments_v3_single_line.csv'
    caminho_saida = 'files/comments_v4_categorized.csv'

    if not os.path.exists(caminho_entrada):
        print("Erro: Arquivo V3 não encontrado.")
        return

    # Dicionário de keywords por tema (usando regex para limite de palavra \b)
    # Aumentamos a abrangência para capturar o contexto correto
    temas_kws = {
        'EUA-Venezuela': [
            r'\bvenezuela\b', r'\bmaduro\b', r'\bvenezuelano\b', r'\bvenezuelana\b', 
            r'\bcaracas\b', r'\bchavista\b', r'\bcorina\b', r'\bedmundo\b', r'\bpetro\b'
        ],
        'EUA-Ira': [
            r'\biran\b', r'\bira\b', r'\bteera\b', r'\bayatollah\b', r'\bpersia\b', 
            r'\biraniano\b', r'\bteheran\b'
        ],
        'Russia-Ucrania': [
            r'\brussia\b', r'\bucrania\b', r'\bputin\b', r'\bzelensky\b', r'\botan\b', 
            r'\bkremlin\b', r'\brusso\b', r'\bucraniano\b', r'\bkiev\b', r'\bmoscou\b'
        ],
        'EUA-Brasil': [
            r'\bbrasil\b', r'\bbrasileiro\b', r'\bbrasileira\b', r'\btaxa\b', r'\btaxas\b', 
            r'\bimposto\b', r'\btaxacao\b', r'\bhaddad\b', r'\bitamaraty\b', r'\bdolar\b'
        ]
    }

    def classificar_com_scoring(texto):
        texto = str(texto).lower()
        pontos = {tema: 0 for tema in temas_kws.keys()}
        
        for tema, kws in temas_kws.items():
            for pattern in kws:
                # Conta quantas vezes a palavra exata aparece
                matches = re.findall(pattern, texto)
                pontos[tema] += len(matches)
        
        # O "ira" (verbo ou sentimento) ainda é um risco. 
        # Se houver empate entre Irã e outro país, o outro país ganha (regra de desempate)
        vencedor = max(pontos, key=pontos.get)
        
        if pontos[vencedor] == 0:
            return 'Outros'
        
        # Se o maior for Irã, mas Venezuela também tiver pontos, priorizamos Venezuela 
        # (Já que o seu exemplo mostrou que vídeos da Venezuela citam muito o Irã como comparação)
        if vencedor == 'EUA-Ira' and pontos['EUA-Venezuela'] > 0:
            return 'EUA-Venezuela'
            
        return vencedor

    print("Iniciando Categorização V5 com Scoring e Word Boundaries...")
    
    chunks = pd.read_csv(caminho_entrada, chunksize=150000)
    primeira_vez = True
    
    for chunk in chunks:
        # 1. Aplica a nova lógica de pontuação
        chunk['tema_geopolitico'] = chunk['text_cleaned'].apply(classificar_com_scoring)
        
        # 2. Remove a coluna original conforme solicitado para economizar espaço
        if 'comment' in chunk.columns:
            chunk = chunk.drop(columns=['comment'])
            
        # 3. Mantém apenas os categorizados
        df_final = chunk[chunk['tema_geopolitico'] != 'Outros']
        
        df_final.to_csv(caminho_saida, mode='a', index=False, header=primeira_vez, encoding='utf-8')
        primeira_vez = False
        print(f"Processando... {len(df_final)} linhas categorizadas neste bloco.")

    print(f"Sucesso! Arquivo gerado: {caminho_saida}")

if __name__ == "__main__":
    categorizar_v5()