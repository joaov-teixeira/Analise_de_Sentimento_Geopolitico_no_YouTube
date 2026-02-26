import pandas as pd
import os

def limpar_estrutura_csv():
    # Caminho do seu arquivo normalizado (ajuste o nome se necessário)
    caminho_entrada = 'files/comments_ultra_cleaned.csv'
    caminho_saida = 'files/comments_v3_single_line.csv'
    
    if not os.path.exists(caminho_entrada):
        print(f"Erro: Arquivo {caminho_entrada} não encontrado.")
        return

    print("Iniciando remoção de quebras de linha e linhas vazias...")
    
    # Processamento em blocos para gerenciar o 1M de linhas
    chunks = pd.read_csv(caminho_entrada, chunksize=100000)
    
    total_original = 0
    total_final = 0
    primeira_vez = True
    
    for chunk in chunks:
        total_original += len(chunk)
        
        # 1. Remover quebras de linha (\n e \r) nos comentários originais e limpos
        # Isso garante que cada registro ocupe exatamente UMA linha física no arquivo
        chunk['comment'] = chunk['comment'].replace(r'[\r\n]+', ' ', regex=True)
        chunk['text_cleaned'] = chunk['text_cleaned'].replace(r'[\r\n]+', ' ', regex=True)
        
        # 2. Remover linhas onde o comentário ou o texto limpo estão vazios/NaN
        chunk = chunk.dropna(subset=['comment', 'text_cleaned'])
        
        # 3. Remover linhas que contenham apenas espaços em branco
        chunk = chunk[chunk['text_cleaned'].str.strip() != ""]
        
        total_final += len(chunk)
        
        # Salva a nova versão (V3)
        chunk.to_csv(caminho_saida, mode='a', index=False, header=primeira_vez, encoding='utf-8')
        primeira_vez = False
        print(f"Processados {total_original} registros... Mantidos: {total_final}")

    print(f"\n--- RELATÓRIO DE LIMPEZA DE ESTRUTURA ---")
    print(f"Total de linhas no arquivo original: {total_original}")
    print(f"Total de linhas após remover vazios: {total_final}")
    print(f"Linhas eliminadas (vazias ou corrompidas): {total_original - total_final}")
    print(f"Arquivo salvo em: {caminho_saida}")

if __name__ == "__main__":
    limpar_estrutura_csv()