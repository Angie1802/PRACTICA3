import math
class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

try:
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = CIRCULO(radio)
    
    area = circulo.calcular_area()
    print(f"El área del círculo con radio {radio} es: {area:.2f}")
    
except ValueError:
    print("Por favor, ingrese un valor numérico para el radio.")