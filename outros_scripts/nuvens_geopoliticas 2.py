import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os
import re

# --- 1. CONFIGURAÇÃO DE CAMINHOS ---
BASE_PATH = r'C:\AMS_final\files'
SAVE_PATH = r'C:\AMS_final\apresentacao_visual\wordclouds_refinadas2'
ARQUIVO = os.path.join(BASE_PATH, 'comments_v16_dicionarioMod_final.csv')

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)

# --- 2. MEGA LISTA DE STOPWORDS REFINADA ---
# Inclui conectivos, pronomes e ruídos típicos de YouTube (com e sem acento)
STOPWORDS_BASE = set(STOPWORDS)
RUÍDO_EXTRA = {
    'e', 'é', 'não', 'nao', 'que', 'q', 'de', 'do', 'da', 'em', 'um', 'uma', 'os', 'as', 
    'para', 'pra', 'com', 'no', 'na', 'nos', 'nas', 'por', 'mais', 'mas', 'foi', 'vai', 
    'vou', 'está', 'tá', 'tem', 'tinha', 'ser', 'seu', 'sua', 'seus', 'suas', 'meu', 
    'minha', 'meus', 'minhas', 'ele', 'ela', 'eles', 'elas', 'você', 'vc', 'vcs', 
    'isso', 'isto', 'aquele', 'aquela', 'quem', 'qual', 'quando', 'onde', 'como', 
    'porque', 'porquê', 'pq', 'até', 'mesmo', 'também', 'ainda', 'só', 'so', 'tudo', 
    'pode', 'podem', 'fazer', 'disse', 'diz', 'falou', 'ver', 'ter', 'tenho', 'têm', 
    'seja', 'era', 'disso', 'daqui', 'aqui', 'ai', 'aí', 'lá', 'la', 'estão', 'estao', 'esta','trump', 'esse','pais',
}
STOPWORDS_PT = STOPWORDS_BASE.union(RUÍDO_EXTRA)

# Stopwords específicas para "limpar" o tema e focar nos adjetivos e gatilhos
STOPWORDS_TEMA = {
    'EUA-Brasil': {'brasil', 'eua', 'americano', 'brasileiro', 'governo', 'presidente'},
    'EUA-Venezuela': {'venezuela', 'eua', 'maduro', 'povo', 'ditador', 'nicolas'},
    'Polarizacao-Brasil-Interno': {'brasil', 'lula', 'bolsonaro', 'pt', 'governo', 'povo'},
    'Russia-Ucrania': {'russia', 'ucrania', 'china', 'esta', 'muito', 'mundo', 'todo', 'essa', 'brasil', 'putin', 'zelensky', 'guerra', 'pais', 'russo'},
    'EUA-China': {'china', 'esta', 'trump', 'muito', 'chinese', 'chineses', 'eua', 'paise', 'estado','chine', 'paises', 'chines', 'americano', 'esse' 'chines', 'economia', 'mundo', 'pais', 'xi'},
    'EUA-Ira': {'ira', 'eua', 'guerra', 'iraniano', 'americano', 'pais'},
    'EUA-Europa': {'europa', 'eua', 'uniao', 'europeia', 'paises', 'europeu'},
    'Lideranca-EUA-Hegemonia': {'eua', 'mundo', 'potencia', 'lider', 'hegemonia'},
    'Outros': set()
}

def gerar_nuvens_limpas():
    print("☁️ Iniciando Limpeza e Geração de WordClouds...")
    try:
        df = pd.read_csv(ARQUIVO, usecols=['text_cleaned', 'tema_geopolitico'])
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado em {ARQUIVO}")
        return

    # Processamento por Tema
    for cat in df['tema_geopolitico'].unique():
        print(f"📦 Filtrando tema: {cat}")
        df_cat = df[df['tema_geopolitico'] == cat]
        
        # Amostragem para performance (mantendo 30k comentários por tema)
        tamanho = min(30000, len(df_cat))
        texto = " ".join(df_cat['text_cleaned'].astype(str).sample(n=tamanho, random_state=42).str.lower())
        
        # Unifica as stopwords base com as específicas do tema
        sw_final = STOPWORDS_PT.union(STOPWORDS_TEMA.get(cat, set()))

        # Configuração Estética Superior
        wc = WordCloud(
            width=1200, 
            height=800, 
            background_color='black', 
            stopwords=sw_final,
            min_word_length=4,  # 👈 REFINAMENTO: Remove "e", "não", "vc", "pq" etc.
            max_words=100, 
            collocations=False, 
            colormap='autumn' if 'Venezuela' in cat else 'cool' if 'China' in cat else 'viridis'
        ).generate(texto)
        
        filename = f"WordCloud_{cat.replace('-', '_')}_Refinada.png"
        wc.to_file(os.path.join(SAVE_PATH, filename))

    print(f"✅ Sucesso! Nuvens salvas em: {SAVE_PATH}")

if __name__ == "__main__":
    gerar_nuvens_limpas()