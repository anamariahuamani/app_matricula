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


## prectica de tarea


lista_alumnos=[]
def mensaje_menu():
    menu_opciones="""
        ...........Bienvenido al sistema!...........
        ................ Registrese ................
                        elije lo que deseas hacer: 
        1. Escribe [s] si deseas registrar un alumno
        2. Escribe [n] si deseas salir del programa
        Escribe tu respuesta: """
    return menu_opciones

def ingresar_datos_alumnos():
    id=len(lista_alumnos)+1
    cui=int(input("Ingrese el numero de su dni: "))
    nombre=input("Ingrese el nombre del alumno: ")
    apellido=input("Ingrese el apellido del alumno: ")
    numero_celular=int(input("Ingrese su numero de celular: "))
    programa_estudio=input("Ingrese programa de estudio: ")
    ciclo_academico=input("Ingrese su ciclo academico: ")
    email=input("Ingrese su correo electronico: ")
    guardar_datos_alumnos(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email)

def guardar_datos_alumnos(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email):
    alumno={
            "id":id,
            "cui":cui,
            "nombre":nombre,
            "apellido":apellido,
            "numero_celular":numero_celular,
            "programa_estudio":programa_estudio,
            "ciclo_academico":ciclo_academico,
            "email":email
            }
    lista_alumnos.append(alumno)

while True:
    menu_opciones=input(mensaje_menu())

    if menu_opciones.lower()=="n":
        print("saliendo del Sistema")
        break
    elif menu_opciones.lower()=="s":
        ingresar_datos_alumnos()  
    else:
        print("Opcion erronea")

print(lista_alumnos)


 