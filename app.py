import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel

# Definición de la clase Empleado para representar a un empleado
class Empleado:
    def __init__(self, id, nombre, apellido, cargo, area, salario):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.area = area
        self.salario = salario

# Definición de la clase principal de la aplicación
class StartupPaguiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Startup Pagui")
        
        # Lista de empleados
        self.empleados = []
        
        # Salario mínimo en Colombia para 2023
        self.salario_minimo = 1160000
        
        # Crear una lista desplegable para mostrar los empleados
        self.listbox = tk.Listbox(root)
        self.listbox.pack()
        
        # Botones de la interfaz
        self.agregar_button = tk.Button(root, text="Agregar Empleado", command=self.agregar_empleado)
        self.agregar_button.pack()
        
        self.calcular_button = tk.Button(root, text="Calcular Salario Neto", command=self.calcular_salario_neto)
        self.calcular_button.pack()
        
        self.imprimir_button = tk.Button(root, text="Imprimir Colilla de Pago", command=self.imprimir_colilla_pago)
        self.imprimir_button.pack()
        
        self.buscar_button = tk.Button(root, text="Buscar Empleado por ID", command=self.buscar_empleado_por_id)
        self.buscar_button.pack()
        
        self.visualizar_button = tk.Button(root, text="Visualizar Colillas de Todos los Empleados", command=self.visualizar_colillas)
        self.visualizar_button.pack()

    # Función para agregar un empleado a la lista de empleados
    def agregar_empleado(self):
        empleado_info = simpledialog.askstring("Agregar Empleado", "Ingrese los datos del empleado (ID, Nombre, Apellido, Cargo, Área, Salario):")
        if empleado_info:
            try:
                id, nombre, apellido, cargo, area, salario = empleado_info.split(",")
                empleado = Empleado(int(id), nombre, apellido, cargo, area, float(salario))
                self.empleados.append(empleado)
                self.listbox.insert(tk.END, f"{empleado.id}: {empleado.nombre} {empleado.apellido}")
            except ValueError:
                messagebox.showerror("Error", "Formato de entrada incorrecto. Use ID, Nombre, Apellido, Cargo, Área, Salario")

    # Función para calcular el salario neto de un empleado
    def calcular_salario_neto(self):
        empleado_seleccionado = self.listbox.get(self.listbox.curselection())
        if empleado_seleccionado:
            empleado_id = int(empleado_seleccionado.split(":")[0])
            empleado = next((e for e in self.empleados if e.id == empleado_id), None)
            if empleado:
                salario_bruto = empleado.salario
                salario_neto = salario_bruto
                
                # Verificar si se debe agregar ayuda de transporte
                if salario_bruto < 2 * self.salario_minimo:
                    salario_neto += 140000  # Ayuda de transporte
                
                # Mostrar el salario neto en una ventana emergente
                messagebox.showinfo("Salario Neto", f"El salario neto de {empleado.nombre} {empleado.apellido} es: {salario_neto}")
            else:
                messagebox.showerror("Error", "Empleado no encontrado.")
        else:
            messagebox.showerror("Error", "Por favor, seleccione un empleado de la lista.")

    # Función para imprimir la colilla de pago de un empleado
    def imprimir_colilla_pago(self):
        empleado_seleccionado = self.listbox.get(self.listbox.curselection())
        if empleado_seleccionado:
            empleado_id = int(empleado_seleccionado.split(":")[0])
            empleado = next((e for e in self.empleados if e.id == empleado_id), None)
            if empleado:
                salario_bruto = empleado.salario
                salario_neto = salario_bruto
                
                # Verificar si se debe agregar ayuda de transporte
                if salario_bruto < 2 * self.salario_minimo:
                    salario_neto += 140000  # Ayuda de transporte
                
                # Crear una nueva ventana emergente para mostrar la colilla de pago
                colilla_window = Toplevel(self.root)
                colilla_window.title("Colilla de Pago")
                colilla_text = f"ID: {empleado.id}\nNombre: {empleado.nombre} {empleado.apellido}\n"
                colilla_text += f"Cargo: {empleado.cargo}\nÁrea: {empleado.area}\n"
                colilla_text += f"Salario Bruto: {salario_bruto}\nSalario Neto: {salario_neto}"
                tk.Label(colilla_window, text=colilla_text).pack()
            else:
                messagebox.showerror("Error", "Empleado no encontrado.")
        else:
            messagebox.showerror("Error", "Por favor, seleccione un empleado de la lista.")

    # Función para buscar un empleado por su ID
    def buscar_empleado_por_id(self):
        empleado_id = simpledialog.askinteger("Buscar Empleado por ID", "Ingrese el ID del empleado:")
        if empleado_id:
            empleado = next((e for e in self.empleados if e.id == empleado_id), None)
            if empleado:
                # Mostrar los detalles del empleado en una ventana emergente
                empleado_window = Toplevel(self.root)
                empleado_window.title("Detalles del Empleado")
                empleado_text = f"ID: {empleado.id}\nNombre: {empleado.nombre} {empleado.apellido}\n"
                empleado_text += f"Cargo: {empleado.cargo}\nÁrea: {empleado.area}\nSalario: {empleado.salario}"
                tk.Label(empleado_window, text=empleado_text).pack()
            else:
                messagebox.showerror("Error", "Empleado no encontrado.")
    
    # Función para visualizar las colillas de pago de todos los empleados
    def visualizar_colillas(self):
        if not self.empleados:
            messagebox.showinfo("Información", "No hay empleados registrados.")
            return
        
        colillas_window = Toplevel(self.root)
        colillas_window.title("Colillas de Pago de Todos los Empleados")
        
        for empleado in self.empleados:
            salario_bruto = empleado.salario
            salario_neto = salario_bruto
                
            # Verificar si se debe agregar ayuda de transporte
            if salario_bruto < 2 * self.salario_minimo:
                salario_neto += 140000  # Ayuda de transporte
            
            colilla_text = f"ID: {empleado.id}\nNombre: {empleado.nombre} {empleado.apellido}\n"
            colilla_text += f"Cargo: {empleado.cargo}\nÁrea: {empleado.area}\n"
            colilla_text += f"Salario Bruto: {salario_bruto}\nSalario Neto: {salario_neto}\n\n"
            
            tk.Label(colillas_window, text=colilla_text).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = StartupPaguiGUI(root)
    root.mainloop()
