import pandas as pd
import os

def filtrar_com_auditoria():
    caminho_entrada = 'files/comments_ultra_cleaned.csv'
    caminho_pt = 'files/comments_v2_pt_only.csv'
    caminho_audit = 'files/comments_v2_spanish_audit.csv' # Rastro de Auditoria
    
    # Marcadores de Espanhol
    stopwords_es = [
        r'\b el \b', r'\b y \b', r'\b con \b', r'\b del \b', 
        r'\b los \b', r'\b las \b', r'\b pero \b', r'\b hablo \b',
        r'\b habla \b', r'\b hable \b', r'\b esta \b', r'\b este \b'
    ]
    regex_es = '|'.join(stopwords_es)
    
    if not os.path.exists(caminho_entrada):
        print(f"Erro: {caminho_entrada} não encontrado.")
        return

    # Limpa arquivos anteriores se existirem para evitar duplicidade no modo 'a' (append)
    for f in [caminho_pt, caminho_audit]:
        if os.path.exists(f): os.remove(f)

    print("Iniciando filtragem com Rastro de Auditoria...")
    
    chunks = pd.read_csv(caminho_entrada, chunksize=100000)
    
    total_pt = 0
    total_es = 0
    primeira_vez = True
    
    for chunk in chunks:
        # Identificação
        is_spanish = chunk['text_cleaned'].str.contains(regex_es, case=False, na=False, regex=True)
        
        df_pt = chunk[~is_spanish]
        df_es = chunk[is_spanish]
        
        total_pt += len(df_pt)
        total_es += len(df_es)
        
        # Salva a base limpa (PT)
        df_pt.to_csv(caminho_pt, mode='a', index=False, header=primeira_vez, encoding='utf-8')
        
        # Salva o rastro de auditoria (ES)
        df_es.to_csv(caminho_audit, mode='a', index=False, header=primeira_vez, encoding='utf-8')
        
        primeira_vez = False
        print(f"Processando... PT: {total_pt} | ES (Audit): {total_es}")

    print("\n--- RESUMO DO RASTRO DE AUDITORIA ---")
    print(f"Total de comentários preservados (PT): {total_pt}")
    print(f"Total de comentários movidos para auditoria (ES): {total_es}")
    
    # Exibe amostragem do que foi considerado espanhol
    if total_es > 0:
        print("\n--- AMOSTRAGEM DE COMENTÁRIOS IDENTIFICADOS COMO ESPANHOL ---")
        amostra = pd.read_csv(caminho_audit, nrows=50).sample(min(10, total_es))
        for idx, row in amostra.iterrows():
            print(f"- ORIGINAL: {row['comment'][:100]}...")
            print(f"  LIMPO: {row['text_cleaned'][:100]}\n")

if __name__ == "__main__":
    filtrar_com_auditoria()