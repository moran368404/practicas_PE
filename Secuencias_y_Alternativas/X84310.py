def grade(s):
    if s < 5:
        return 'suspens'
    elif s < 7:
        return 'aprovat'
    elif s < 9:
        return 'notable'
    elif s < 10:
        return 'excel.lent'
    else:
        return 'MH'

with open("mi_fichero.txt", "w") as f:
    f.write("Primera línea del archivo.")



