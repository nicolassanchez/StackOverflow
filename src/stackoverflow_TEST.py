# -*- coding: utf-8 -*-

from stackoverflow import *

################################################################
#  Funciones de test
################################################################

def test_filtrar_por_año(preguntas):
    print("TEST de 'filtrar_por_año'")
    año = 2009
    print("   - Número de preguntas en '{}': {}".format(año, len(filtrar_por_año(preguntas, año))))
    año = 2015
    print("   - Número de preguntas en '{}': {}\n".format(año, len(filtrar_por_año(preguntas, año))))


def test_calcular_etiquetas(preguntas):
    print("TEST de 'calcular_etiquetas'")
    etiquetas = calcular_etiquetas(preguntas)
    print('   - Número de etiquetas: {}'.format(len(etiquetas)))
    print("   - Diez primeras: {}\n".format(sorted(list(etiquetas))[:10]))


def test_calcular_preguntas_mejor_valoradas(preguntas):
    print("TEST de 'calcular_preguntas_mejor_valoradas'")
    preguntas_mejor_valoradas = calcular_preguntas_mejor_valoradas(preguntas, limite=5)
    for p in preguntas_mejor_valoradas:
        print("   [{}] - {}".format(p[1], p[0]))
    print()
    

def test_contar_etiquetas(preguntas):
    print("TEST de 'contar_etiquetas'")
    frecuencias = contar_etiquetas(preguntas)
    etiquetas = sorted(frecuencias, key=frecuencias.get, reverse=True)
    for etiqueta in etiquetas[:5]:
        print("   {} -> {}".format(etiqueta, frecuencias[etiqueta]))
    print()
    

def test_mostrar_distribucion_etiquetas(preguntas):
    print("TEST de 'mostrar_distribucion_etiquetas'\n")
    etiquetas = ['list', 'file', 'string']
    mostrar_distribucion_etiquetas(preguntas, etiquetas)
    
    
def test_calcular_palabras_clave(stopwords):
    print("TEST de 'calcular_palabras_clave'")
    titulo = 'How do I make a menu that does not require the user to press [enter] to make a selection ?'
    print("   - Dejando stopwords: {}".format(calcular_palabras_clave(titulo)))
    print("   - Quitando stopwords: {}\n".format(calcular_palabras_clave(titulo, stopwords)))


def test_contar_palabras_clave(preguntas, stopwords):
    print("TEST de 'contar_palabras_clave'")
    print("   (solo las 5000 primeras preguntas para que la prueba sea más rápida)")
    frecuencias = contar_palabras_clave(preguntas[:5000], stopwords)
    print('   - Número de palabras: {}'.format(len(frecuencias)))
    print("   - Diez primeras: {}\n".format(frecuencias[:10]))

    
def test_agrupar_preguntas_por_año(preguntas):
    print("TEST de 'agrupar_preguntas_por_año'")
    preguntas_por_año = agrupar_preguntas_por_año(preguntas)
    for año in preguntas_por_año:
        print("   {} -> {} preguntas".format(año, len(preguntas_por_año[año])))
    print()


def test_mostrar_evolucion_etiquetas(preguntas):
    print("TEST de 'mostrar_evolucion_etiquetas'\n")
    etiquetas = ['list', 'file', 'string']
    mostrar_evolucion_etiquetas(preguntas, etiquetas)


################################################################
#  Programa principal
################################################################
with open('../data/stopwords.txt') as f:
    stopwords = [p.strip() for p in f]

preguntas = leer_preguntas('../data/stackoverflow_python_questions.csv')
print(len(preguntas), preguntas[:10], "\n")

#test_filtrar_por_año(preguntas)
#test_calcular_etiquetas(preguntas)
#test_calcular_preguntas_mejor_valoradas(preguntas)
#test_contar_etiquetas(preguntas)
#test_mostrar_distribucion_etiquetas(preguntas)
#test_calcular_palabras_clave(stopwords)
#test_contar_palabras_clave(preguntas, stopwords)
#test_agrupar_preguntas_por_año(preguntas)
#test_mostrar_evolucion_etiquetas(preguntas)


