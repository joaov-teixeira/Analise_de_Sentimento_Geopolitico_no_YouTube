import os

def preparar_portugues_limpo():
    # Caminho onde você salvou os arquivos brutos
    pasta_origem = r'C:\AMS_Final\analise_de_sentimento\SentStrength_Data'
    
    # Arquivos que você descompactou do ZIP e o Político
    arquivo_base = os.path.join(pasta_origem, 'SentimentLookupTable.txt')
    arquivo_politico = os.path.join(pasta_origem, 'PoliticalEmotionLookupTable.txt')
    
    if not os.path.exists(arquivo_base):
        print("Erro: SentimentLookupTable.txt não encontrado!")
        return

    print("Limpando e unificando dicionários...")
    termos_finais = []

    # Lê o arquivo base e remove comentários/linhas vazias
    with open(arquivo_base, 'r', encoding='utf-8') as f:
        for linha in f:
            if linha.strip() and not linha.startswith('#'):
                termos_finais.append(linha.strip())

    # Adiciona os termos políticos (Bozo, Lula, etc)
    if os.path.exists(arquivo_politico):
        with open(arquivo_politico, 'r', encoding='utf-8') as f:
            for linha in f:
                if linha.strip() and not linha.startswith('#'):
                    termos_finais.append(linha.strip())

    # Salva com os DOIS nomes para não haver erro de detecção
    for nome in ['SentimentLookupTable.txt', 'EmotionLookupTable.txt']:
        caminho_final = os.path.join(pasta_origem, nome)
        with open(caminho_final, 'w', encoding='utf-8') as f:
            # SentiStrength exige uma quebra de linha simples no final
            f.write("\n".join(termos_finais) + "\n")
    
    print(f"✅ Sucesso! {len(termos_finais)} termos carregados e limpos.")

if __name__ == "__main__":
    preparar_portugues_limpo()