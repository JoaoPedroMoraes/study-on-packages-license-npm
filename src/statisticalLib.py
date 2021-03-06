import statistics as st
import matplotlib.pyplot as plt
import numpy as np
from numpy import array
import math
import csv
import json
import pandas as pd

def lerCSV(arquivo, titulo_coluna, indice_coluna):
    with open(arquivo) as csvfile:
        # Adiciona os valores a um objeto, onde cada item vai ser uma linha
        temp = csv.reader(csvfile, delimiter=',')
        # Cria lista que vai receber os dados do objeto
        readCSV = []
        # Transforma o objeto em uma lista
        for line in temp:
            readCSV.append(line)

        lista = []

        for row in readCSV:
            if(row[indice_coluna] != titulo_coluna) and (row[indice_coluna] != 'True') and (row[indice_coluna] != 'False'):
                lista.append(int(row[indice_coluna]))            
            elif(row[indice_coluna] != titulo_coluna):
                lista.append(row[indice_coluna])
        return sorted(lista)

def statistics(x, name_lista):
    lista = sorted(x)
    # Média é a soma dos valores de elementos dividido pela quantidade de elementos.
    media = st.mean(lista)
    # Mediana é o valor que divide o conjunto X pela metade
    mediana = st.median(lista)
    # Moda é o valor que aparece com mais frequência no conjunto.
    moda = st.mode(lista)
    # Mínimo é o menor valor pertencente ao conjunto.
    minimo = min(lista)
    # Máximo é o maior valor pertencente ao conjunto.
    maximo = max(lista)
    # Amplitude é a diferença entre o valor máximo e o valor mínimo do conjunto.
    amplitude = max(lista) - min(lista)
    # Desvio Padrão identifica o quão próximo ou longe da média estão os elementos do conjunto. O cálculo do desvio padrão é dado pela raiz quadrada da variância.
    desvio = st.stdev(lista)
    # Variância é uma medida de dispersão que indica o quão longe os valores estão da média do conjunto. A fórmula matemática é dada pela soma do quadrado da diferença de cada valor para a média, dividido pelo número de elementos, conforme abaixo:
    varianca = st.variance(lista)
    # Coeficiente de Variação é a razão entre o desvio padrão e a variância
    coeficiente_var = st.stdev(lista) / st.mean(lista) * 100
    # Coeficiente de Assimetria identifica assimetrias no gráfico da função de densidade do conjunto. Um valor positivo indica uma elevação na esquerda, enquanto um negativo indica uma elevação na direita.
    coeficiente_ass = st.median(lista[len(lista)//2:]) / (st.median(lista) ** 3/2)
    # Quartis são valores que dividem o conjunto em subconjuntos com 25% dos elementos, cada.
    Q1 = st.median(lista[:len(lista)//2])
    Q2 = st.median(lista)
    Q3 = st.median(lista[len(lista)//2:])
    print(f'=====| {name_lista} |=====')
    print('# MEDIDAS DE CENTRALIDADE')
    print('- Media = {:.2f}'.format(media))                                
    print('- Mediana = {:.2f}'.format(mediana))
    print('- Moda = '+ str(moda) )
    print('- Minimo = ' + str(minimo) )
    print('- Maximo = ' + str(maximo) )
    print('# MEDIDAS DE DISPERSÃO')
    print('- Ampĺitude = ' + str(amplitude) )
    print('- Desvio Padrão = {:.2f}'.format(desvio))
    print('- Variança = {:.2f}'.format(varianca))
    print('- Coeficiente de Variação = {:.2f} %'.format(coeficiente_var))
    print('- Coeficiente de Assimetria = {:.3f}'.format(coeficiente_ass))
    print('- Q1 = '+ str(Q1))
    print('- Q2 = '+ str(Q2))
    print('- Q3 = '+ str(Q3))


    class objeto:
        def __init__(self, media, mediana, moda, minimo, maximo, amplitude, desvio, varianca, coeficiente_var, coeficiente_ass, q1, q2, q3 ):
            self.media = media
            self.mediana = mediana
            self.moda = moda
            self.minimo = minimo
            self.maximo = maximo
            self.amplitude = amplitude
            self.desvio = desvio
            self.varianca = varianca
            self.coeficiente_var = coeficiente_var
            self.coeficiente_ass = coeficiente_ass
            self.q1 = Q1
            self.q2 = Q2
            self.q3 = Q3

    return objeto( media, mediana, moda, minimo, maximo, amplitude, desvio, varianca, coeficiente_var, coeficiente_ass, Q1, Q2, Q3 )

#Define funções para gerar os graficos
extension = 'eps'
# Say, "the default sans-serif font is COMIC SANS"
# plt.rcParams["font.family"] = "Times New Roman"
plt.rc('font',family='Times New Roman')

def pizza(valores, labels, titulo, arquivo):        
        fig1, ax1 = plt.subplots()
        ax1.pie(valores, labels = labels, autopct='%1.1f%%', shadow=False, startangle=90)
        ax1.axis('equal')
        plt.title(titulo)
        plt.savefig(f'./graphs/{arquivo}.{extension}', bbox_inches='tight')
        plt.show()

def histograma(valores, titulo, labelX, labelY, arquivo):
        k = round(1+3.3*math.log10(len(valores)))
        plt.hist(valores, rwidth=0.9, bins=k)
        plt.title(titulo)
        plt.xlabel(labelX)
        plt.ylabel(labelY)
        plt.grid(axis='y', alpha=0.9)
        plt.savefig(f'./graphs/{arquivo}.{extension}', bbox_inches='tight')
        plt.show()

def histogramaSelectK(valores, titulo, labelX, labelY, arquivo, k):
        plt.hist(valores, rwidth=0.9, bins=k)
        plt.title(titulo)
        plt.xlabel(labelX)
        plt.ylabel(labelY)
        plt.grid(axis='y', alpha=0.9)
        plt.savefig(f'./graphs/{arquivo}.{extension}', bbox_inches='tight')
        plt.show()

def barras(valores, labels, titulo, arquivo):        
        plt.bar(labels, valores, color='blue')
        plt.title(titulo)
        for x,y in zip(labels, valores):
            plt.annotate(y, # this is the text
                        (x,y), # this is the point to label
                        textcoords="offset points", # how to position the text
                        xytext=(0,2), # distance from text to points (x,y)
                        ha='center') # horizontal alignment can be left, right or center
        plt.savefig(f'./graphs/{arquivo}.{extension}', bbox_inches='tight')
        plt.show()


def detect_outlier(data_1):
    outliers=[]    
    threshold=3
    mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)
    
    
    for y in data_1:
        z_score= (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers