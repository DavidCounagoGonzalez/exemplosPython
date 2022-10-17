#import math
from math import pi
from abc import ABC, abstractmethod

class ErroPrimeiroCadrante(Exception):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "Erro " + str (self.valor) + ": A coordenada non é do primeiro cadrante"


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX (self, x):
        if x<0:
            self.x=0
        else:
            self.x=x

    def getX(self):
        return self.x

    def __str__(self):
        print(super.__str__(self))
        return 'X = ' + str(self.x) +' Y = '+ str(self.y)

p= Punto(1,1)
p.setX(-32)
p.x=-50
print(p)


class Punto2:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def setX(self, x):
        if x < 0:
            raise ErroPrimeiroCadrante(1)
        else:
            self.__x = x

    def setY(self, y):
        if y < 0:
            raise ErroPrimeiroCadrante(2)
        else:
            self.__y = y


    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    x= property(getX, setX)
    y = property(getY, setY)

    def __str__(self):
        print(super.__str__(self))
        return 'X = ' + str(self.__x) + ' Y = ' + str(self.__y)

try:
    p2 = Punto2(1, 1)

    p2.setX (-32)
    p2.x = -50
    p2.y = 3
    p2._Punto2__y= -3
    p2.__y = -20

except ErroPrimeiroCadrante:
    print("Non se pode inicializar a clase con coordenadas que non pertenzan o primeiro cadrante")

print(p2)

class Persoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __lt__(self, outro):
        return self.idade < outro.idade

    def __le__(self, outro):
        return  self.idade<= outro.idade

    def __eq__(self, outro):
        return self.idade == outro.idade

    def __ge__(self, outro):
        return self.idade >= outro.idade

    def __gt__(self, outro):
        return self.idade > outro.idade

p1 = Persoa("Luis", 20)
p2 = Persoa("Adrián", 21)

print(p1<=p2)

class Polygon (ABC):

    @abstractmethod
    def numeroDeLados(self):
        pass

class Triangulo (Polygon):
    def __str__(self):
        return "Clase Triangulo"