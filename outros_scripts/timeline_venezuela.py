import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- CONFIGURAÇÃO ---
BASE_PATH = r'C:\AMS_final\files'
SAVE_PATH = r'C:\AMS_final\apresentacao_master'
# Garantir que o caminho do arquivo use barras invertidas duplas ou raw string
ARQUIVO = os.path.join(BASE_PATH, 'comments_v16_dicionarioMod_final.csv')

if not os.path.exists(SAVE_PATH): 
    os.makedirs(SAVE_PATH)

def gerar_timeline_picos_reais():
    print("📈 Corrigindo e Gerando Visualização de Picos Reais...")
    
    try:
        df = pd.read_csv(ARQUIVO)
        #errors='coerce' transforma datas inválidas em NaT (Not a Time) em vez de travar o código
        df['published_at'] = pd.to_datetime(df['published_at'], errors='coerce')
        df = df.dropna(subset=['published_at'])
        df['date'] = df['published_at'].dt.date
        
        # Filtro: Tema e Janela Temporal (Foco nos eventos recentes)
        df_ven = df[df['tema_geopolitico'] == 'EUA-Venezuela'].copy()
        
        # CORREÇÃO: Data de corte em formato ISO (YYYY-MM-DD)
        data_corte = pd.to_datetime('2025-7-01').date()
        df_ven = df_ven[df_ven['date'] >= data_corte]

        # Agrupamento diário
        timeline = df_ven.groupby('date')['Sentiment_Scale'].mean().reset_index()
        timeline['date'] = pd.to_datetime(timeline['date'])

        # --- ESTÉTICA ---
        plt.figure(figsize=(18, 9))
        sns.set_style("whitegrid")
        
        # Plotagem dos Picos Brutos
        plt.plot(timeline['date'], timeline['Sentiment_Scale'], 
                 color='#d63031', linewidth=1.5, marker='o', markersize=3, 
                 label='Sentimento Diário (Picos Reais)')

        # CORREÇÃO DOS EVENTOS: Datas em formato YYYY-MM-DD
        EVENTOS = [
        ('2025-07-01', 'AUMENTO DE TENSÃO GEOP.'),
        ('2025-8-19', 'MILITARIZAÇÃO DO CARIBE'),
        ('2026-01-03', 'CAPTURA DE MADURO'),
        ]
        
        for dt_str, label in EVENTOS:
            try:
                d = pd.to_datetime(dt_str)
                if d in timeline['date'].values:
                    plt.axvline(x=d, color='black', linestyle='-', linewidth=1, alpha=0.7)
                    plt.text(d, -1.5, f' {label}', rotation=90, fontweight='bold', color='black')
            except:
                continue # Pula datas que ainda estiverem erradas

        plt.title('VENEZUELA: ANÁLISE DE PICOS DE REATIVIDADE (NOV/2025 - JAN/2026)', fontsize=20, pad=20)
        plt.ylabel('Média Diária ($Sentiment\_Scale$)', fontsize=12)
        plt.axhline(0, color='black', linewidth=1.2)
        plt.ylim(-1.6, 0.1) 
        
        plt.savefig(os.path.join(SAVE_PATH, 'Timeline_Venezuela_Picos_Final11111111111111111111.png'), dpi=300, bbox_inches='tight')
        plt.close()
        print(f"✅ Sucesso! Gráfico salvo em: {SAVE_PATH}")

    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    gerar_timeline_picos_reais()