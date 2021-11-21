# -*- coding: utf-8 -*-
''' Análisis de preguntas sobre Python en stackoverflow

AUTOR: José A. Troyano
REVISOR: 
ÚLTIMA MODIFICACIÓN: 10/06/2019

En este proyecto trabajaremos con preguntas sobre el lenguaje Python. Los datos están
extraídos de stackoverflow, y se corresponden con una colección de preguntas desde 2008 hasta
2016 relacionadas con Python. La colección completa está disponible en Kaggle datasets
(https://www.kaggle.com/stackoverflow/pythonquestions). Los datos con los que trabajaremos incluyen
distintas informaciones sobre las preguntas y, a partir de ellos, generaremos una serie de 
informes y gráficas que resumirán aspectos relevantes de las temáticas más consultadas.


FORMATO DE ENTRADA:
-------------------
El formato de entrada es CSV. Cada registro del fichero de entrada ocupa una línea y contiene
cuatro informaciones sobre las preguntas (puntuación, título, año y  etiqueta principal). 
Estas son las primeras líneas de un fichero de entrada:

    score,title,year,tag
    21,How can I find the full path to a font from its display name on a Mac?,2008,photoshop
    27,Get a preview JPEG of a PDF on Windows?,2008,pdf
    40,Continuous Integration System for a Python Codebase,2008,extreme-programming
    25,cx_Oracle: How do I iterate over a result set?,2008,cx-oracle
    28,Using 'in' to match an attribute of Python objects in an array,2008,iteration
    30,Class views in Django,2008,oop
    20,Python and MySQL,2008,bpgsql


FUNCIONES A IMPLEMENTAR:
------------------------
- leer_preguntas(fichero):
    lee el fichero de preguntas y devuelve una lista de tuplas con nombre
- filtrar_por_año(preguntas, año):
    recibe una lista de preguntas y devuelve solo las del año recibido como parámetro
- calcular_etiquetas(preguntas):
    calcula el conjunto de etiquetas usadas en la colección de preguntas
- calcular_preguntas_mejor_valoradas(preguntas, limite=10):
    calcula las preguntas con las puntuaciones más altas
- contar_etiquetas(preguntas):
    calcula las frecuencias de las etiquetas de una lista de preguntas
- mostrar_distribucion_etiquetas(preguntas, etiquetas):
    muestra un diagrama de tarta con la distribución de uso de varias etiquetas
- calcular_palabras_clave(titulo, stopwords=[]):
    calcula la lista de palabras clave del título de una pregunta
- contar_palabras_clave(preguntas, stopwords=[]):
    calcula las frecuencias de las palabras clave usadas en una lista de preguntas
- agrupar_preguntas_por_año(preguntas):
    calcula un diccionario con una lista de preguntas por cada año
- mostrar_evolucion_etiquetas(preguntas, etiquetas):
    muestra la evolución del uso de etiquetas a lo largo del tiempo
'''

import csv
from collections import namedtuple, Counter
from itertools import groupby
from matplotlib import pyplot as plt

# EJERCICIO 1:
Pregunta = namedtuple('Pregunta', 'puntuacion, titulo, año, etiqueta')
def leer_preguntas(fichero):
    ''' Lee el fichero de registros y devuelve una lista de tuplas con nombre
    
    ENTRADA: 
       - fichero: nombre del fichero de entrada -> str
    SALIDA: 
       - lista de preguntas (puntuacion, titulo, año, etiqueta) -> [Pregunta(int, str, int, str)]
    '''
    pass


# EJERCICIO 2:
def filtrar_por_año(preguntas, año):
    ''' Recibe una lista de preguntas y devuelve solo las del año recibido como parámetro
    
    ENTRADA: 
       - preguntas: lista de preguntas (puntuacion, titulo, año, etiqueta) -> [Pregunta(int, str, int, str)]
       - año: del que se seleccionarán las preguntas -> int
    SALIDA: 
       - lista de preguntas seleccionadas -> [Pregunta(int, str, int, str)]
    '''
    pass


# EJERCICIO 3:
def calcular_etiquetas(preguntas):
    ''' Calcula el conjunto de etiquetas usadas en la colección de preguntas
    
    ENTRADA: 
       - preguntas: lista de preguntas (puntuacion, titulo, año, etiqueta) -> [Pregunta(int, str, int, str)]
    SALIDA: 
       - conjunto de etiquetas encontradas -> {str}
    '''
    pass


# EJERCICIO 4:
def calcular_preguntas_mejor_valoradas(preguntas, limite=10):
    ''' Calcula las preguntas con las puntuaciones más altas
    
    ENTRADA: 
       - preguntas: lista de preguntas (puntuacion, titulo, año, etiqueta) -> [Pregunta(int, str, int, str)]
       - limite: número de preguntas a recuperar -> int
    SALIDA: 
       - lista de tuplas (titulo, puntuacion) ordenada de mayor a menor puntuacion  -> [(str, int)]
    '''
    pass


# EJERCICIO 5:
def contar_etiquetas(preguntas):
    ''' Calcula las frecuencias de las etiquetas de una lista de preguntas
    
    ENTRADA: 
       - preguntas: lista de preguntas (puntuacion, titulo, año, etiqueta) -> [Pregunta(int, str, int, str)]
    SALIDA: 
       - diccionario cuyas claves son las etiquetas y los valores las frecuecias  -> {str: int}
    '''
    pass


# EJERCICIO 6:
def mostrar_distribucion_etiquetas(preguntas, etiquetas):
    ''' Muestra un diagrama de tarta con la distribución de uso de varias etiquetas
    
    ENTRADA: 
       - preguntas: lista de preguntas (puntuacion, titulo, año, etiqueta) -> [Pregunta(int, str, int, str)]
       - etiquetas: lista de etiquetas que se inlcuirán en la gráfica
    SALIDA EN PANTALLA: 
       - gráfica con un diagrama de tarta con un sector por cada etiqueta recibida
    
    Se usarán las siguientes instrucciones para generar la gráfica:
        plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.legend()
        plt.show()

    Donde 'tamaños' es una lista, alineada con la lista de etiquetas, con el número de preguntas para
    cada etiqueta.  
    '''
    pass


# EJERCICIO 7:
def calcular_palabras_clave(titulo, stopwords=[]):
    ''' Calcula la lista de palabras clave del título de una pregunta
    
    ENTRADA: 
       - titulo: descripción de la pregunta -> str
       - stopwords: palabras huecas, consideradas no relevantes como palabras clave
    SALIDA: 
       - lista de palabras clave encontradas en el título  -> [str]
    PROCEDIMIENTO:
       - Pasar el título a minúsculas
       - Descomponer el título en una lista de términos separados por espacios
       - Eliminar los siguientes símbolos de los términos: '¿?[](){}¡!-+/*,;.<>='
       - Dejar en la lista de términos solo aquellos que estén compuestos por letras
       - Eliminar de la lista los términos que aparezcan el la lista de stopwords
    '''
    pass


# EJERCICIO 8:
def contar_palabras_clave(preguntas, stopwords=[]):
    ''' Calcula las frecuencias de las palabras clave usadas en una lista de preguntas
    
    ENTRADA: 
       - preguntas: lista de preguntas (puntuacion, titulo, año, etiqueta) -> [Pregunta(int, str, int, str)]
       - stopwords: palabras huecas, consideradas no relevantes como palabras clave
    SALIDA: 
       - lista de tuplas (termino, frecuencia) ordenada de mayor a menor frecuencia  -> [(str, int)]
    '''
    pass


# EJERCICIO 9:
def agrupar_preguntas_por_año(preguntas):
    ''' Calcula un diccionario con una lista de preguntas por cada año
    
    ENTRADA: 
       - preguntas: lista de preguntas (puntuacion, titulo, año, etiqueta) -> [Pregunta(int, str, int, str)]
    SALIDA: 
       - diccionario cuyas claves son los años y los valores la lista de preguntas de cada año  
                               -> {int: [Pregunta(int, str, int, str)]}
    '''
    pass


# EJERCICIO 10: 
def mostrar_evolucion_etiquetas(preguntas, etiquetas):
    ''' Muestra la evolución del uso de etiquetas a lo largo del tiempo
    
    ENTRADA: 
       - preguntas: lista de preguntas (puntuacion, titulo, año, etiqueta) -> [Pregunta(int, str, int, str)]
       - etiquetas: lista de etiquetas que se inlcuirán en la gráfica
    SALIDA EN PANTALLA: 
       - gráfica con una línea para cada etiqueta con su evolución temporal
    
    Se usarán las siguientes instrucciones para generar la gráfica:
        for etiqueta, evolucion in zip(etiquetas, evoluciones):
            plt.plot(evolucion, label=etiqueta)
        plt.xticks(range(len(años)), años, rotation=80, fontsize=10)
        plt.legend()
        plt.show()

    Donde 'años' y 'evoluciones' son dos listas con la siguiente información:
       - años: lista de los años incluidos en la colección de preguntas, ordenados de menor a mayor
       - evoluciones: lista con la evolución de uso de cada etiqueta, alineada con la lista de etiquetas. 
                      Cada evolución consiste en una lista de frecuencias, alineada con la lista de años, 
                      correspondientes con el número de veces que la etiqueta ha sido usada cada año.   
    '''
    pass
