from Consulta import Consulta_lines_with

def libro_visitas(archivo):
    with open(archivo, 'a') as f:
        while True:
            nombre = input("Ingrese su nombre: ").strip()
            if nombre == '':
                break
            print("Bienvenido "+ nombre+"!")
            f.write(nombre+'\n')

archivo = 'libro_visitas.txt'
libro_visitas(archivo)
Consulta_lines_with(archivo)