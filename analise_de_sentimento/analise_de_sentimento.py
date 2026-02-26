import os
import pandas as pd
import subprocess
import time

# --- CONFIGURAÇÃO DE CAMINHOS ---
DIRETORIO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
RAIZ_PROJETO = os.path.dirname(DIRETORIO_SCRIPT)

# 1. Mantenha a pasta como SentStrength_Data (conforme o help do JAR)
CAMINHO_JAR = os.path.join(DIRETORIO_SCRIPT, 'SentiStrength.jar')
CAMINHO_DADOS = os.path.join(DIRETORIO_SCRIPT, 'SentStrength_Data') + os.sep

# 2. Arquivos de entrada e saída
ARQUIVO_ENTRADA = os.path.join(RAIZ_PROJETO, 'files', 'comments_v6_total.csv')
ARQUIVO_TEMPORARIO = os.path.join(RAIZ_PROJETO, 'files', 'temp_para_sentimento.txt')
ARQUIVO_SAIDA_FINAL = os.path.join(RAIZ_PROJETO, 'files', 'comments_v16_dicionarioMod_final.csv')

def executar_analise_nativa():
    if not os.path.exists(ARQUIVO_ENTRADA):
        print(f"Erro: {ARQUIVO_ENTRADA} não encontrado.")
        return

    print("🚀 Passo 1: Preparando arquivo temporário...")
    df = pd.read_csv(ARQUIVO_ENTRADA)
    # Limpeza básica para evitar erros de leitura no JAR
    df['text_cleaned'] = df['text_cleaned'].fillna('neutro').astype(str).str.replace('\n', ' ')
    df['text_cleaned'].to_csv(ARQUIVO_TEMPORARIO, index=False, header=False, encoding='utf-8')

    print("🔥 Passo 2: Executando SentiStrength com 'sentidata'...")
    # AJUSTE CRÍTICO: 'sentidata' conforme o seu log de erro
    comando = [
        'java', '-jar', CAMINHO_JAR,
        'sentidata', CAMINHO_DADOS,
        'input', ARQUIVO_TEMPORARIO,
        'wait'
    ]

    start_time = time.time()
    try:
        # shell=True às vezes ajuda no Windows com caminhos complexos
        subprocess.run(comando, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro na execução: {e}")
        return

    # O SentiStrength gera automaticamente o arquivo com sufixo 0_out.txt
    arquivo_gerado = ARQUIVO_TEMPORARIO.replace('.txt', '0_out.txt')
    
    if not os.path.exists(arquivo_gerado):
        print("Erro: O arquivo de saída não foi localizado.")
        return

    print("📊 Passo 3: Consolidando resultados...")
    df_scores = pd.read_csv(arquivo_gerado, sep='\t')
    
    df['Positive'] = df_scores['Positive']
    df['Negative'] = df_scores['Negative']
    df['Sentiment_Scale'] = df['Positive'] + df['Negative']

    df.to_csv(ARQUIVO_SAIDA_FINAL, index=False, encoding='utf-8')
    
    print(f"\n✅ CONCLUÍDO EM {(time.time() - start_time) / 60:.2f} MINUTOS!")
    print(f"Arquivo salvo: {ARQUIVO_SAIDA_FINAL}")

if __name__ == "__main__":
    executar_analise_nativa()