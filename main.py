"""
- registrar alumnos.
- generar fichas de matricula
- mostrar la lista de todos los matriculados
- filtrar matriculados por programa de estudio
"""
lista_alumnos=[]
#inicio de problema
#necesito poder agregar mas alumnos sin neceisdad de crear tantas variables
#posible solucion cre o encerar el codigo en un cliclo while
nombre=input("Ingrese el nombre del alumno: ")
apellido=input("Ingrese el apeliido del alumno: ")
nombre2=input("Ingrese el nombre del alumno: ")
apellido2=input("Ingrese el apeliido del alumno: ")
alumno={
    "nombre":nombre,
    "apellido":apellido
}
alumno2={
    "nombre":nombre2,
    "apellido":apellido2
}
lista_alumnos.append(alumno)
lista_alumnos.append(alumno2)
#fin del problema

#deseo mostrar un menu con las opciones de agregar un nuevo alumnos y salir del programa.
print(lista_alumnos)
`
tarea 

"""
-registrar alumnos
- generar ficha de matricula 
-mostrar la lista  de todo los matriculados
- facilitar matriculados x pgrama de estudio 
"""
lista_alumnos=[]
while True:
    opcion= input***alija lo que deseas hacer
escribe () deseas registrar un alumno 
escfribe ()si deseas salir del programa
escribe tu respuesta:***"n"}
if opcion.lower ()***"n":
    break
nombre=input("ingresar el nombre del alumno: ")
apellido=input("ingrese el apellido del alumno ")
alumno={
    "nombre":nombre,
    "apellido"apellido
}
lista_alumnos.appendt(alumno)
print(lista_alumnos)