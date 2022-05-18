"""
    Q1. Ecrire une fonction en langage Python qui retourne 𝑰𝒎𝒐𝒚 après l’avoir calculée par la méthode des
        trapèzes.
"""
from numpy import *


def moy(mesure):
    dt = 2
    tinit = 0
    tf = (len(mesure) - 1) * dt
    T = arange(0, len(mesure)*dt, dt)
    integ = 0
    for i in range(0, len(T)-1):
        integ += (mesure[i+1] + mesure[i]) * (T[i+1] - T[i])/2

    return 1.0/integ*tf


def ecart(mesure):
    im = moy(mesure)
    tmp = []
    tf = (len(mesure) - 1) * 2
    for i in range(len(mesure)):
        tmp.append((mesure[i] - im)**2)

    ec = moy(tmp)/tf
    return ec ** 0.5
