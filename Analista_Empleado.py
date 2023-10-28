def Analista():

    class Empleado:
        def __init__(self, id, nombre, apellido, cargo, area, salario):
            self.id = id
            self.nombre = nombre
            self.apellido = apellido
            self.cargo = cargo
            self.area = area
            self.salario = salario

    class PaguiStartup:
        
        def __init__(self):
            self.empleados = []
            self.colillas_pago = []

        def agregar_empleado(self, empleado):
            self.empleados.append(empleado)

        def listar_empleados(self):
            for empleado in self.empleados:
                print(f"ID: {empleado.id}, Nombre: {empleado.nombre}, Cargo: {empleado.cargo}")

        def calcular_salario_neto(self):
            for empleado in self.empleados:
                salario_minimo = 1000000  # Valor del salario mínimo vigente (ejemplo)
                if empleado.salario < 2 * salario_minimo:
                    salario_neto = empleado.salario + 140000  # Ayuda de transporte de 50,000 (ejemplo)
                else:
                    salario_neto = empleado.salario
                self.colillas_pago.append((empleado, salario_neto))

        def imprimir_colilla_pago(self):
            for empleado, salario_neto in self.colillas_pago:
                print(f"ID: {empleado.id}, Nombre: {empleado.nombre}, Salario Neto: {salario_neto}")

        def buscar_empleado_por_id(self, id):
            empleado_encontrado = next((empleado for empleado in self.empleados if empleado.id == id), None)
            if empleado_encontrado:
                print(f"ID: {empleado_encontrado.id}, Nombre: {empleado_encontrado.nombre}, Cargo: {empleado_encontrado.cargo}")
            else:
                print("Empleado no encontrado")

        def registrar_empleado_manualmente(self):
            id = int(input("Ingrese el ID del empleado: "))
            nombre = input("Ingrese el nombre del empleado: ")
            apellido = input("Ingrese el apellido del empleado: ")
            cargo = input("Ingrese el cargo del empleado: ")
            area = input("Ingrese el área del empleado: ")
            salario = float(input("Ingrese el salario del empleado: "))
            
            empleado = Empleado(id, nombre, apellido, cargo, area, salario)
            self.agregar_empleado(empleado)
            print(f"Empleado {nombre} {apellido} registrado con éxito.")

    # Crear una instancia de PaguiStartup
    pagui = PaguiStartup()

    # Interacción para registrar empleados
    while True:
        print("\nMenú:")
        print("1. Registrar empleado")
        print("2. Listar empleados")
        print("3. Calcular salarios netos")
        print("4. Imprimir colillas de pago")
        print("5. Buscar empleado por ID")
        print("6. Cerrar sesion")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            pagui.registrar_empleado_manualmente()
        elif opcion == "2":
            print("\nEmpleados:")
            pagui.listar_empleados()
        elif opcion == "3":
            pagui.calcular_salario_neto()
            print("\nSalarios netos calculados.")
        elif opcion == "4":
            print("\nColillas de Pago:")
            pagui.imprimir_colilla_pago()
        elif opcion == "5":
            id_buscado = int(input("Ingrese el ID del empleado a buscar: "))
            pagui.buscar_empleado_por_id(id_buscado)
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            
            Analista(pagui)
                
def Empleado():
        
        class PaguiStartup:
                
            def __init__(self):
                self.empleados = []
                self.colillas_pago = []

            def buscar_empleado_por_id(self, id):
                empleado_encontrado = next((empleado for empleado in self.empleados if empleado.id == id), None)
                if empleado_encontrado:
                    print(f"ID: {empleado_encontrado.id}, Nombre: {empleado_encontrado.nombre}, Cargo: {empleado_encontrado.cargo}")
                else:
                    print("Empleado no encontrado")
        pagui = PaguiStartup()          
        while True:
            print("\nMenú:")
            print("1. Buscar colilla de pago con tu cedula")
            print("2. Cerrar sesion")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id_buscado = int(input("Ingrese el ID del empleado a buscar: "))
                pagui.buscar_empleado_por_id(id_buscado)
            elif opcion == "2":
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")