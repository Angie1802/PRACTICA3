class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        if self.notas:
            print("Notas:", ", ".join(map(str, self.notas)))

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, notas):
        self.notas = notas

#EJEMPLO
nombre = input("Ingrese el nombre del alumno: ")
numero_registro = input("Ingrese el número de registro del alumno: ")

alumno = Alumno(nombre, numero_registro)

edad = int(input("Ingrese la edad del alumno: "))
alumno.setAge(edad)

notas_input = input("Ingrese las notas del alumno separadas por comas: ")
notas = [float(nota) for nota in notas_input.split(',')]
alumno.setNota(notas)

alumno.display()
