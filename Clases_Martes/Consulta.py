def Consulta_raw(archivo):
    f = open(archivo, mode='r')
    cont_archivo = f.read()
    print(cont_archivo)
    f.close()

def Consulta_lines(archivo):
    f = open(archivo, mode = 'r')
    for line in f:
        print(line, end= '')
    f.close()

def Consulta_lines_with(archivo):
    consul = []
    with open(archivo, mode = 'r') as f:
        for line in f:
            consul.append(line.strip())
    print(consul)

