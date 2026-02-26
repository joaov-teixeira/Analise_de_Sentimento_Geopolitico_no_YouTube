import pandas as pd
import os

BASE_PATH = r'C:\AMS_final\files'
df = pd.read_csv(os.path.join(BASE_PATH, 'comments_v16_dicionarioMod_final.csv'))

def gerar_dados_apresentacao():
    print("📊 Calculando métricas de impacto...")
    
    # 1. Porcentagem de Ódio Puro (Scores -4 e -5)
    df['odio_puro'] = df['Sentiment_Scale'].apply(lambda x: 1 if x <= -4 else 0)
    toxicidade = df.groupby('tema_geopolitico')['odio_puro'].mean() * 100
    
    # 2. Média de Likes por Nível de Sentimento
    # (Para provar se o negativo engaja mais)
    engajamento = df.groupby('Sentiment_Scale')['like_count'].mean()

    print("\n" + "="*40)
    print("🔥 RANKING DE TOXICIDADE (% DE ÓDIO PURO)")
    print("="*40)
    print(toxicidade.sort_values(ascending=False))

    print("\n" + "="*40)
    print("👍 MÉDIA DE LIKES POR SENTIMENTO")
    print("="*40)
    print(engajamento)

if __name__ == "__main__":
    gerar_dados_apresentacao()