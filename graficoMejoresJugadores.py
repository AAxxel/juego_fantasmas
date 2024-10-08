import matplotlib.pyplot as plt2
import numpy as np


def graficar_puntajes(jugadores, puntajes):
    plt2.plot(jugadores, puntajes, marker='o', color='b', linestyle='--')
    plt2.xlabel('Jugadores')
    plt2.ylabel('Puntaje')
    plt2.title('Mejores Jugadores')
    

def mostrar_grafico_puntaje(jugadores, puntajes):
    graficar_puntajes(jugadores, puntajes)
    plt2.show()

def devolver_grafico_puntaje(jugadores, puntajes):
    graficar_puntajes(jugadores, puntajes)
    return plt2.gcf()


