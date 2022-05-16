from math import *

class complex:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        return self.real+'i'+self.img

    def __repr__(self):
        return self.real + 'i' + self.img

    def __add__(self, other):
        return complex(self.real+other.real, self.img+other.img)

    def getRe(self):
        return self.real

    def getIm(self):
        return self.img

    def module(self):
        return sqrt(self.real**2 + self.img**2)

    def conj(self):
        return complex(self.real, -self.img)

    def __mul__(self, other):
        real = self.real*other.real - self.img*other.img
        img = self.real*other.img + self.img*other.real
        return complex(real, img)

    