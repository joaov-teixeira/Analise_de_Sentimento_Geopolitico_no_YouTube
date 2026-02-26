							Exemplo de utilização do sentistrength 0.0.7

----------------------------------------------------------------------------------------------------------------------------------------------

O Sentistrength é um algoritmo de análise de sentimentos interessante para textos de redes sociais (geralmente curtos e carregados com sentimentos).
Ele utiliza um dicionário léxico anotado por seres humanos e melhorado com o uso de Aprendizado de Máquina. O SentiStrength atribui pontuações 
a tokens de um dicionário, sendo que as palavras com emoções positivas são atribuídos valores entre 1 e 5 e as palavras com emoções negativas são 
atribuídos valores entre -5 e -1. Os valores 1 e -1 são usados para indicar emoções neutras, enquanto que 5 e -5 são usados para indicar emoções 
muito positivas e muito negativas, respectivamente. E realizado um cálculo com a polaridade de cada termo com emoção na frase, resultando em scores 
que indicam o resultado da análise de sentimento.

----------------------------------------------------------------------------------------------------------------------------------------------

Para fazer o donwload do pacote Sentistrength 0.0.7, execute o seguinte comando (com o pip3 e o python3 já instalados em seu ambiente):

	pip3 install sentistrength==0.0.7

Guia para referência: https://pypi.org/project/sentistrength/0.0.7/

----------------------------------------------------------------------------------------------------------------------------------------------

O Sentistrength utiliza um dicionário com arquivos contendo termos classificadas (diretório ./SentiStrength_Data/) e um 
arquivo chamado ./SentiStrength.jar para realizar a análise de sentimentos. Ambos estão na presente pasta.

Obs: Devemos colocar os caminhos completos desses auxiliares (diretório e arquivo) no script python.

----------------------------------------------------------------------------------------------------------------------------------------------

O sentistrength 0.0.7 oferece alguns scores resultantes da análise de sentimentos de um texto, dentre os principais temos:

-dual
-trinary
-scale

Exemplo: 

	texto de entrada: 'mesmo com todo o sucesso ele vivia uma vida tediosa'

Scores resultantes:

	dual: [(positivo,negativo)] [(4,-3)] positivo em 4 e negativo em -3
	trinary: [(positivo,negativo,neutro)] [(4,-3,1)]  positivo em 4, negativo em -3 e neutro em 1  
	scale: [0.25] escala proporcional ao dual e ao trinary, variando entre 1 (muito positivo) e -1 (muito negativo). O valor 0 representa o neutro.

O score scale é muito interessante pois ele resume em apenas um valor a polaridade geral da frase.

----------------------------------------------------------------------------------------------------------------------------------------------

Descrição de outros dicionários 'SentiStrength_Data' opcionais contidos no diretório ./Outros_Dicionarios/

EN-US-original: base em inglês.
PT-BR_original: base original em português.
PT-BR_atualizado: mais termos em português, plural/singular, masculino/feminino, traduções do inglês.
PT-BR_normalizado: todos os termos do atualizado, sem acentuação e com os termos da eleição em um arquivo separado: TermosCandidatos.txt.

O dicionário utilizado por esse exemplo é o PT-BR_normalizado.

Como o dicionário PT-BR_normalizado não possui acentuações e caracteres em maiúsculo, todo o texto analisado necessita ser previamente
processado substituindo esses caracteres para fazermos a análise.

Ex: 'Ótimo' -> pré-processamento -> 'otimo'
----------------------------------------------------------------------------------------------------------------------------------------------
