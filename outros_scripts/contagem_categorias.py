import pandas as pd
import os

# --- CAMINHO DO SEU ARQUIVO ---
ARQUIVO = r'C:\AMS_final\files\comments_v16_dicionarioMod_final.csv'

def contar_comentarios_por_tema():
    if not os.path.exists(ARQUIVO):
        print(f"❌ Erro: O arquivo não foi encontrado em {ARQUIVO}")
        return

    # Carregar apenas a coluna necessária para economizar memória
    df = pd.read_csv(ARQUIVO, usecols=['tema_geopolitico'])
    
    # Realizar a contagem
    contagem = df['tema_geopolitico'].value_counts()
    total = len(df)

    print("\n" + "="*50)
    print(f"📊 DISTRIBUIÇÃO DOS {total:,} COMENTÁRIOS")
    print("="*50)
    
    for tema, qtd in contagem.items():
        percentual = (qtd / total) * 100
        print(f"🔹 {tema:<30} | {qtd:>7,} comentários ({percentual:.2f}%)")
    
    print("="*50)

if __name__ == "__main__":
    contar_comentarios_por_tema()