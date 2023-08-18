import random

def generar_numeros_aleatorios(cantidad):
    numeros_aleatorios = [random.randint(0, 100) for _ in range(cantidad)]
    return numeros_aleatorios

def mostrar_lista(lista):
    print("Lista:", lista)

def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", lista_ordenada)


