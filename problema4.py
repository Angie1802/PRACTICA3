
class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        area =self.largo * self.ancho
        return area

#EJEMPLO
try:
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    rectangulo= RECTANGULO(largo,ancho)

    area = rectangulo.calcular_area()
    print(f"El área del rectangulo es: {area:.2f}")
    
except ValueError:
    print("Por favor, ingrese un valor numérico en los datos.")