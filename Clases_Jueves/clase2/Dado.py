import random

class Dado:
    def __init__(self, caras=6):
        """""
        Aqui definimos las caras que tendra el dado, como estamos utilizando un dado tradicional definimos unicamente
        caras del 1 al 6
        """""
        self.caras = caras

    def tirar_dado(self):
        """""
        Simulamos el lanzamiento de un dado, esta funcion solamente retorna un numero aleatorio entre 1 y el numero de 
        caras que tenga definido el dado.
        """""
        return random.randint(1,self.caras)

dado = Dado()
res = dado.tirar_dado()
print(f"Resultado del dado: {res}")