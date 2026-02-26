# -*- coding: UTF-8 -*-

from sentistrength import PySentiStr

#==============================================================================#
# coloque o caminho completo do arquivo e dir/ auxiliares (SentiStrength.jar e  
# SentiStrength_Data/) nas constantes abaixo:
#==============================================================================#
SENTISTRENGTH_DATA_PATH =  r'Exemplo Linux: /home/usuario/Downloads/sentistrength_exemplo/SentiStrength_Data/'
SENTISTRENGTH_JAR_PATH = r'Exemplo Linux: /home/usuario/Downloads/sentistrength_exemplo/SentiStrength.jar'

#==============================================================================#
# Guia para referência (com exemplo de config. de paths no Windows ao final da página):
# https://pypi.org/project/sentistrength/0.0.7/
#==============================================================================#


def main():
    #==========================================================================#
    # criando o objeto do sentistrength e setando os caminhos dos arquivos
    # auxiliares
    #==========================================================================#
    obj_sentistrength = PySentiStr()
    obj_sentistrength.setSentiStrengthPath(SENTISTRENGTH_JAR_PATH)
    obj_sentistrength.setSentiStrengthLanguageFolderPath(SENTISTRENGTH_DATA_PATH)
    
    #===========================================================================#
    # realizando a leitura do arquivo frases.txt e colocando as linhas 
    # na lista file_lines (file.readlines() retorna essa lista)
    #===========================================================================#
    with open('frases.txt','r') as file:
        file_lines = file.readlines()

    #===========================================================================#
    # iterando sobre a lista file_lines e realizando a análise de sentimentos  
    # dos textos obtendo como resultados 3 scores (dual, trinary e scale) 
    # similares e proporcionais para um mesmo texto de entrada
    #===========================================================================#
    for line in file_lines:
        text = line.strip() # para removermos o \n ao final da linha
        result_scale = obj_sentistrength.getSentiment(text,score ='scale')
        result_dual = obj_sentistrength.getSentiment(text,score ='dual')
        result_trinary = obj_sentistrength.getSentiment(text,score ='trinary')        
        print('text: {0}\nresult_scale: {1}\nresult_dual: {2}\nresult_trinary: {3}\n'
            .format(text,str(result_scale),str(result_dual),str(result_trinary)))

if __name__ == "__main__":
    main()
