import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen."
        elif self.x == 0:
            return "El punto está sobre el eje Y."
        elif self.y == 0:
            return "El punto está sobre el eje X."
        elif self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante."
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante."
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante."
        else:
            return "El punto está en el cuarto cuadrante."

    def vector(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return Punto(dx, dy)

    def distancia(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return math.sqrt(dx**2 + dy**2)

class Rectangulo:
    def __init__(self, punto_inicio=Punto(), punto_final=Punto()):
        self.punto_inicio = punto_inicio
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final.x - self.punto_inicio.x)

    def altura(self):
        return abs(self.punto_final.y - self.punto_inicio.y)

    def area(self):
        return self.base() * self.altura()

# Ejemplo de uso
p1 = Punto(2, 3)
p2 = Punto(5, 8)

rectangulo = Rectangulo(p1, p2)

print("Rectángulo:")
print("Punto inicial:", rectangulo.punto_inicio)
print("Punto final:", rectangulo.punto_final)
print("Base:", rectangulo.base())
print("Altura:", rectangulo.altura())
print("Área:", rectangulo.area())

#EXPERIMENTACIÓN
# Crear los puntos A, B, C y D
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

# Imprimir los puntos por pantalla
print("Punto A:", A)
print("Punto B:", B)
print("Punto C:", C)
print("Punto D:", D)

# Consultar cuadrantes
print("Cuadrante de A:", A.cuadrante())
print("Cuadrante de C:", C.cuadrante())
print("Cuadrante de D:", D.cuadrante())

# Consultar vectores AB y BA
vector_AB = A.vector(B)
vector_BA = B.vector(A)
print("Vector AB:", vector_AB)
print("Vector BA:", vector_BA)

# Consultar distancia entre puntos
print("Distancia entre A y B:", A.distancia(B))
print("Distancia entre B y A:", B.distancia(A))

# Determinar punto más lejano al origen
distancias_al_origen = {
    "A": A.distancia(Punto()),
    "B": B.distancia(Punto()),
    "C": C.distancia(Punto())
}
punto_mas_lejano = max(distancias_al_origen, key=distancias_al_origen.get)
print(f"El punto más lejano al origen es {punto_mas_lejano}")

# Crear un rectángulo utilizando los puntos A y B
rectangulo_AB = Rectangulo(A, B)

# Consultar base, altura y área del rectángulo
print("Base del rectángulo:", rectangulo_AB.base())
print("Altura del rectángulo:", rectangulo_AB.altura())
print("Área del rectángulo:", rectangulo_AB.area())