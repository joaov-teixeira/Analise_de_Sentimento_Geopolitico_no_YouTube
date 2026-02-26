import pandas as pd
import re
import os

def categorizar_v6():
    caminho_entrada = 'files/comments_v3_single_line.csv'
    caminho_saida = 'files/comments_v6_total.csv'

    if not os.path.exists(caminho_entrada):
        print("Erro: Arquivo V3 não encontrado.")
        return

    # Limpeza de arquivo anterior
    if os.path.exists(caminho_saida): os.remove(caminho_saida)

    # Dicionário Expandido de Keywords (\b garante a palavra exata)
    temas_kws = {
        'EUA-Venezuela': [
            r'\bvenezuela\b', r'\bmaduro\b', r'\bvenezuelano\b', r'\bcaracas\b', 
            r'\bchavista\b', r'\bcorina\b', r'\bpetro\b'
        ],
        'EUA-Ira': [
            r'\biran\b', r'\bira\b', r'\bteera\b', r'\bayatollah\b', r'\biraniano\b'
        ],
        'Russia-Ucrania': [
            r'\brussia\b', r'\bucrania\b', r'\bputin\b', r'\bzelensky\b', r'\botan\b', 
            r'\brusso\b', r'\bucraniano\b'
        ],
        'EUA-Brasil': [
            r'\bbrasil\b', r'\bbrasileiro\b', r'\btaxa\b', r'\btaxas\b', 
            r'\bimposto\b', r'\btaxacao\b', r'\bdolar\b'
        ],
        'EUA-China': [
            r'\bchina\b', r'\bchines\b', r'\bchineses\b', r'\bxangai\b', r'\bpequim\b', r'\btiktok\b'
        ],
        'EUA-Europa': [
            r'\beuropa\b', r'\bdinamarca\b', r'\bgroenlandia\b', r'\bue\b', 
            r'\buniao europeia\b', r'\bmercosul\b', r'\bfranca\b', r'\balemanha\b'
        ],
        'Polarizacao-Brasil-Interno': [
            r'\blula\b', r'\blule\b', r'\bbolsonaro\b', r'\bbozo\b', r'\bstf\b', 
            r'\bxandao\b', r'\bbostil\b', r'\bentreguista\b', r'\bmaga\b'
        ],
        'Lideranca-EUA-Hegemonia': [
            r'\bdono do mundo\b', r'\bimperialismo\b', r'\bpsicopata\b', 
            r'\blaranjao\b', r'\bnarcisista\b', r'\bpotencia\b'
        ]
    }

    def classificar_com_scoring_v6(texto):
        texto = str(texto).lower()
        pontos = {tema: 0 for tema in temas_kws.keys()}
        
        for tema, kws in temas_kws.items():
            for pattern in kws:
                matches = re.findall(pattern, texto)
                pontos[tema] += len(matches)
        
        vencedor = max(pontos, key=pontos.get)
        
        if pontos[vencedor] == 0:
            return 'Outros'
        
        # Desempate estratégico: priorizar Venezuela sobre Irã em caso de conflito
        if vencedor == 'EUA-Ira' and pontos['EUA-Venezuela'] > 0:
            return 'EUA-Venezuela'
            
        return vencedor

    print("Iniciando Categorização V6 Total (890k registros)...")
    
    chunks = pd.read_csv(caminho_entrada, chunksize=150000)
    primeira_vez = True
    
    for chunk in chunks:
        # 1. Classificação com os novos eixos
        chunk['tema_geopolitico'] = chunk['text_cleaned'].apply(classificar_com_scoring_v6)
        
        # 2. Remoção da coluna original 'comment' para otimização
        if 'comment' in chunk.columns:
            chunk = chunk.drop(columns=['comment'])
            
        # 3. SALVAR TUDO (Inclusive a categoria 'Outros')
        chunk.to_csv(caminho_saida, mode='a', index=False, header=primeira_vez, encoding='utf-8')
        primeira_vez = False
        print(f"Processando bloco... Gravando dados categorizados e 'Outros'.")

    print(f"\nSucesso! Base completa e categorizada salva em: {caminho_saida}")

if __name__ == "__main__":
    categorizar_v6()