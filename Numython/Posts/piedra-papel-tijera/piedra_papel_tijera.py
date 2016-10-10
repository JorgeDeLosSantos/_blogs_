# -*- coding: utf8 -*-
import random

def quien_gana(j1,j2):
    piedra = {"piedra":0, "papel":-1, "tijera":1}
    papel = {"piedra":1, "papel":0, "tijera":-1}
    tijera = {"piedra":-1, "papel":1, "tijera":0}
    tomar = {"piedra":piedra, "papel":papel, "tijera":tijera}
    return tomar[j1][j2]

def jugar():
    n = input('Partidas que quieres jugar... ')
    opciones = ["piedra","papel","tijera"]
    resultados = []
    k = 0
    while k<n:
        pc_opcion = random.choice(opciones)
        jugador_opcion = raw_input("Escoja: (piedra, papel o tijera): ")
        if jugador_opcion in opciones:
            resultados.append(quien_gana(jugador_opcion, pc_opcion))
        k += 1

    if resultados.count(1) > resultados.count(-1):
        print("Has ganado\n")
    else:
        print("Intentalo de nuevo\n")

    print("Ganados: %s"%resultados.count(1))
    print("Empatados: %s"%resultados.count(0))
    print("Perdidos: %s"%resultados.count(-1))

if __name__=='__main__':
    jugar()
