import pandas as pd
import os

# --- CONFIGURAÇÃO ---
BASE_PATH = r'C:\AMS_final\files'
ARQUIVO_SENTIMENTO = os.path.join(BASE_PATH, 'comments_v16_dicionarioMod_final.csv')
ARQUIVO_DICIONARIO = os.path.join(BASE_PATH, 'SentimentLookupTable.txt')

def carregar_dicionario():
    dic = {}
    with open(ARQUIVO_DICIONARIO, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                dic[parts[0].lower()] = int(parts[1])
    return dic

def investigar_picos():
    print("🔍 Iniciando Investigação Forense...")
    df = pd.read_csv(ARQUIVO_SENTIMENTO)
    df['published_at'] = pd.to_datetime(df['published_at'])
    df['date'] = df['published_at'].dt.date
    
    # 1. Identificar as 5 datas com maior negatividade média
    picos_negativos = df.groupby('date')['Sentiment_Scale'].mean().nsmallest(5)
    dicionario = carregar_dicionario()

    print("\n" + "="*60)
    print("☢️ TOP 5 DATAS DE NEGATIVIDADE EXTREMA")
    print("="*60)

    for data, media in picos_negativos.items():
        print(f"\n📅 DATA: {data} | MÉDIA DE SENTIMENTO: {media:.2f}")
        
        # Filtra comentários desse dia e pega os 5 mais negativos
        comentarios_dia = df[df['date'] == data].nsmallest(5, 'Sentiment_Scale')
        
        for idx, row in comentarios_dia.iterrows():
            texto = str(row['text_cleaned']).lower()
            score = row['Sentiment_Scale']
            tema = row['tema_geopolitico']
            
            # Descobrir quais palavras do dicionário estão no comentário
            palavras_encontradas = [f"{p}({s})" for p, s in dicionario.items() if f" {p} " in f" {texto} "]
            
            print(f"\n   [Score: {score}] [Tema: {tema}]")
            print(f"   💬 Comentário: {texto[:150]}...")
            print(f"   🧠 Gatilhos Detectados: {', '.join(palavras_encontradas)}")

if __name__ == "__main__":
    investigar_picos()