config = {
  # Configuração da região da coleta -> Formato: ISO 3166-1 alpha-2
  "region_code": "BR",         

  # Configuração da linguagem da coleta -> Formato: ISO 639-1   
  "relevance_language": "pt",     

  # A coleta ocorre da data final para a data inicial -> [ano, mês, dia]
  "start_date": [2025, 1, 11], 
  "end_date": [2026, 1, 31],

  # API que receberá uma requisição PATCH com payload de um JSON contendo informações acerca da coleta
  # Mantenha uma string vazia "" Caso não tenha configurado
  "api_endpoint": "",
  # Intervalo, em segundos, entre cada envio de dados para a API
  "api_cooldown": 60,                                                   

  # Intervalo, em segundos, entre cada tentativa de requisição para a API apos falha
  "try_again_timeout": 60,                                              

  # Palavras que serão utilizadas para filtrar os títulos dos vídeos
  "key_words": [
    "EUA", "Estados Unidos", "Brasil", "taxas", "Venezuela", "Trump", "Guerra", "Lula", "Diplomacia"
  "Irã", "Rússia", "Ucrânia", "petróleo", "sanções", "dólar", "Maduro", "Petrólio", "Nicolás Maduro"
  ], 

  

  # KEYs da API v3 do YouTube  INSIRIR KEYS DA API AQUI:
  "youtube_keys": [
    # "key 1",
    # "key 2",
    # "key 3",
  ],

  # Queries que serão utilizadas na pesquisa
  "queries": [
  # Eixo Brasil-EUA (Economia e Taxas)
  "EUA taxas e impacto exportação Brasil",
  "Relação comercial Brasil e EUA governo",
  "Impacto do dólar nas exportações brasileiras para os EUA",
  "Taxação americana sobre produtos brasileiros",
  "Brasil e EUA Trump e Bolsonaro",

  # Eixo Venezuela e Irã (Energia e Geopolítica)
  "Conflito Eua e Venezuela",
  "Invasão dos EUA na Venezuela",
  "EUA Trump Venezuela Nicolas Maduro",
  "Sanções EUA contra Venezuela impacto Brasil",
  "Tensões EUA e Irã no Oriente Médio",
  "Brasil e Venezuela relações diplomáticas e influência dos EUA",
  "Conflito Irã e Israel",
  "Conflito Irã e Israel impacto brasil",

  # Eixo Rússia e Ucrânia (Agro e Alianças)
  "Guerra Rússia e Ucrânia impacto Brasil",
  "EUA sanções Rússia consequências para o BRICS e Brasil",
  "Posicionamento do Brasil no conflito Rússia Ucrânia",
  "Escalada militar OTAN e Rússia impacto no brasileiro"
]
}
