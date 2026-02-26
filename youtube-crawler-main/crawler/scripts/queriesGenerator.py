import re


data = {
  "actor": (
    "EUA",
    "Estados Unidos",
    "Governo Americano",
    "Biden",
    "Trump"
  ),
  "target": (
    "Brasil",
    "Venezuela",
    "Irã",
    "Rússia",
    "Ucrânia"
  ),
  "topic": (
    "taxas de aço",
    "sanções",
    "tensões diplomáticas",
    "impacto na economia",
    "preço da gasolina",
    "exportações",
    "conflito",
    "crise"
  )
}
# TEMPLATES NÃO PODEM CONTER A MESMA VARIÁVEL MAIS DE UMA VEZ
templates = [
  "[actor] e [target] [topic]",
  "tensões [actor] [target]",
  "[target] taxas [actor]"
]

def extract_variables(string):
  regex = r"\[(\w+)\]"
  variables = re.findall(regex, string)
  return variables

def generate_single_template(template, data):
  temp = [template]
  temp_2 = []

  n = len(extract_variables(template))

  for element in data:
    for string in temp:
      for value in data[element]:
        temp_2.append(string.replace(f"[{element}]", value))
    
    for item in temp_2:
      temp.append(item)
    for item in temp:
      if(len(extract_variables(item)) == n):
        temp.remove(item)
    n -= 1
    temp_2 = []

  res = []

  for item in temp:
    if len(extract_variables(item)) == 0 : 
      res.append(item)
  
  return res

# Pode sobrecarregar o limite de pesquisas da API
def generate_queries():
  # Inserção manual de pesquisas podem ser realizadas dentro da lista queries
  queries = [
        "EUA e Brasil taxas de exportação aço", 
        "Como a guerra na Ucrânia afeta o agronegócio brasileiro",
        "EUA e Venezuela impacto no preço do petróleo Brasil",
        "Sanções americanas contra Rússia consequências para o Brasil",
        "Relação Brasil e Estados Unidos análise política",
        "Tensões EUA e Irã e o impacto na economia brasileira",
        "Novas taxas de importação EUA 2026 Brasil",
        "Disputa comercial EUA e China reflexos no Brasil"
        
        # Olhar marcas, termos, perguntas (ex. pod mata, vaper causa cancer?)
       # Olhar as top marcas vendidas no mundo, brasil, procurar notícias, etc....
    ]


  # Para cada template
  for template in templates:
    
    # Cria o dicionario com os dados necessários para o template
    templateData = {} 
    for variable in extract_variables(template):
      templateData[variable] = data[variable]

    # Gera o conjunto de strings para aquele template
    list = generate_single_template(template, templateData)
    queries += list

  return queries