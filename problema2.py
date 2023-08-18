while(True):
    try:
        lista=input("Digite la lista de notas separadas por una coma: ")
        list=lista.split(',')
        list=[int(lis.strip()) for lis in list]
        print('Las calificaciones son:', list)
        break

    except ValueError:
        print('Las notas ingresadas deben ser números enteros')
