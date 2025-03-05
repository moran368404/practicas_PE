def Consulta_lines_with(archivo):
    consul = []
    with open(archivo, mode = 'r') as f:
        for line in f:
            consul.append(line.strip())
    print(consul)

def reg_invitados(archivo):
    nombre = input("Ingrese su nombre:")
    print("Hola "+ nombre + "!")
    with open(archivo, "a") as f:
        f.write(nombre + '\n')
        print('El nombre fue guardado con exito')

archivo = 'invitados.txt'
reg_invitados(archivo)
Consulta_lines_with(archivo)
