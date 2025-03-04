class Punto:
    #atributos
    x = 0.0
    y = 0.0
    def __init__(self,x,y):
        """""
        
        :param x:
            coordenada x del punto
        :param y:
            coordenada y de punto
        >>> p = Punto(1.0, 1.0)
        >>> print(p.x)
        1.0
        """""
        self.x = x
        self.y = y


    def x(self):
        """""
        >>> p = Punto(1.0, 1.0)
        >>> print(p.x())
        1.0
        """""
        return self.__x

if __name__ == '__main__':
import doctest

print(doctest.testmod(verbose=True))