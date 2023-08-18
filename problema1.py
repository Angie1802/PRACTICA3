while(True):
    try:
        fraccion=input("Escriba la fracción con el formato X/Y: ")
        x,y=map(int,fraccion.split('/'))
        
        if x>y : 
           raise ValueError
        
        porcentaje=round(x/y*100)
        
                
        if porcentaje<1:
            print("E")
        elif porcentaje>99:
            print("F")
        else:
            print(f"El porcentaje de gasolina es {porcentaje}%")
        
    except ValueError:
        print("Por favor ingrese números enteros en el formato indicado, recuerde que X debe ser menor a Y")

    except ZeroDivisionError:
        print("Verifique el valor de Y, no puede ser 0")
