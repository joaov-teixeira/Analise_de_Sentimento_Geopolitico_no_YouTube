# Análise de Sentimento Geopolítico no YouTube

<img width="4294" height="2803" alt="1_densidade_geopolitica" src="https://github.com/user-attachments/assets/a60ab274-e327-435b-b291-4d46d7b80f37" />

## Este projeto foi desenvolvido para a disciplina de Análise de Mídias Sociais na UFOP (Universidade Federal de Ouro Preto), sob a orientação da Professora Helen Lima. O trabalho explora como o público brasileiro reage e se expressa nos comentários do YouTube em relação a grandes eventos geopolíticos globais.

## Apresentação completa: 
https://github.com/joaov-teixeira/Analise_de_Sentimento_Geopolitico_no_YouTube/blob/main/APRESENTA%C3%87%C3%83O%20FINAL.pdf
## Files e dataset: 
https://drive.google.com/drive/folders/1h7tkjSffxfuiWf5WFgcYhVqeE-kFfHcR?usp=sharing

<img width="1200" height="800" alt="WordCloud_EUA_Venezuela_Refinada" src="https://github.com/user-attachments/assets/265b6791-d11a-46aa-bc85-006692b76011" />
<img width="3000" height="1800" alt="4_vies_fontes" src="https://github.com/user-attachments/assets/3a88b068-467b-433e-a1ee-833637310704" />

# Objetivo
## Analisar a opinião dos brasileiros sobre eventos políticos internacionais e o impacto desses acontecimentos nos discursos e no sentimento das comunidades digitais.

# Metodologia e Ferramentas
O projeto baseou-se na coleta automatizada de dados e no processamento de linguagem natural:

## YouTube Crawler: Desenvolvimento de um script customizado em Python utilizando a YouTube Data API v3.
## SentiStrength: Ferramenta utilizada para extrair a força do sentimento (positivo/negativo) dos comentários.
## Visualização: Geração de nuvens de palavras para identificar os termos mais recorrentes.

## Estratégia de Coleta:
## A coleta foi filtrada por palavras-chave e eixos temáticos específicos entre 11 de janeiro de 2025 e 31 de janeiro de 2026:
## Eixo Brasil-EUA: Focado em taxas de exportação, relação comercial, impacto do dólar e figuras políticas (Trump/Lula).
## Eixo Venezuela e Irã: Envolvendo sanções, conflitos no Oriente Médio, preço do petróleo e crises diplomáticas.
## Eixo Rússia e Ucrânia: Impacto no agronegócio brasileiro, consequências para o BRICS e posicionamento diplomático do Brasil.

# Dados Coletados
## O volume de dados processados demonstra a escala da análise:
## Vídeos analisados: Mais de 4.300 vídeos minerados.
## Base de dados bruta: 1.544.890 linhas de comentários extraídos e catalogados.

# Resultados e Conclusões
## Engajamento vs. Sentimento: Embora o volume de negatividade no discurso político seja alto, o engajamento positivo (likes) é superior. Comentários de apoio ou esperança recebem, em média, 2,2 vezes mais curtidas do que ofensas extremas.
## Comportamento por Fonte: A análise de densidade mostrou que não há diferença significativa na toxicidade entre canais de notícias oficiais (como G1 e CNN) e canais independentes. A radicalização parece ser um comportamento inerente ao tema geopolítico nas redes.
## Reatividade Temporal: Identificou-se uma correlação direta entre picos de sentimento e eventos reais, como a captura de Maduro e o anúncio de novas tarifas comerciais em janeiro de 2026.
## Tendência Geral: O discurso permaneceu majoritariamente negativo, refletindo um descontentamento do público brasileiro com o cenário econômico e diplomático estudado.

# Trabalhos Futuros
## Expansão Multiplataforma: Migrar o crawler para processar dados do X (Twitter) e TikTok para análise comparativa.
## Implementação de LLMs: Substituir o processamento léxico por IA Generativa para melhor detecção de sarcasmo e ironia política.
## Análise Preditiva: Desenvolver modelos que utilizem picos de toxicidade para prever a iminência de crises diplomáticas ou protestos civis.
