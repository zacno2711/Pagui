"""
Bancolombia requiere calcular los salarios de su nueva start up Pagui:

-Registrar id nombre, apellido, cargo, area, salario

-Requiere listar a los empleados

-Requiere calcular el salario neto de cada uno, teniendo presente que si gana <2 salarios minimos vigentes se le pago ayuda de transportes

-Imprimir colilla de pago

-Un empleado podra ingresar al sistema y buscar su cedula e imprimirla

-Un analista podra visualizar todos los empleados y todas las colillas, ademas buscar por empleado pero que se haga desde la consola"""


import os
import sys

import Analista_Empleado as view_Analista_empleado

# Importar los diferentes proyectos

# --------------- Limpiar consola ---------------

def limpiar_consola():  
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar consola
    
limpiar_consola()

# ---------------- ------------- ----------------

def mostrar_menu():
    
    limpiar_consola()

    print("\n" + " --------- INICIO DE SESIÓN  ---------- ")
    print("|                                      |")
    print("|  1. Iniciar sesión como asistente    |")
    print("|  2. Iniciar sesión como empleado     |")
    print("|  3. Salir                            |")
    print("|                                      |")
    print(" ---------------- ---- ---------------- \n")
    
opcion = "0"

while opcion != "3":

    mostrar_menu()
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        
        limpiar_consola()

        # ------- Iniciar sesión como asistente ---------
    
        usuario_Analista = "Analista"
        contraseña_Analista = "111"
        
        usuario_a = input("Nombre de usuario: ")
        contraseña_a = input("Contraseña: ")

        if usuario_a == usuario_Analista and contraseña_a == contraseña_Analista:
            limpiar_consola()
            print("\nInicio de sesión exitoso.\n")
            view_Analista_empleado.Analista()
        else:
            print("\nError: Nombre de usuario o contraseña incorrectos.\n")

        # --------------- Fin opción 1. -----------------   
        
    elif opcion == "2":
        
        limpiar_consola()
    
        # ------- Iniciar sesión como empleado ----------
        
        usuario_empleado = "empleado"
        contraseña_empleado = "111"
        
        usuario_e = input("Nombre de usuario: ")
        contraseña_e = input("Contraseña: ")

        if usuario_e == usuario_empleado and contraseña_e == contraseña_empleado:
            limpiar_consola()
            print("\nInicio de sesión exitoso.\n")
            view_Analista_empleado.Empleado()
        else:
            
            print("\nError: Nombre de usuario o contraseña incorrectos.\n")
        
        # --------------- Fin opción 2. -----------------    
    
    elif opcion == "3":
        
        limpiar_consola()
        
        print("\n" + "Saliendo del programa... \n \n")
        sys.exit()

    else:
        
        limpiar_consola()
        
        print("\n" + "Opción no válida. Por favor, selecciona una opción del menú. \n")
    
# ---------------- ------------- ----------------