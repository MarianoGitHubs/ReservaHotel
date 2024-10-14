import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from tkcalendar import DateEntry
from crear_conexion_bd import crear_conexion_bd
from insertar_datos import insertar_huesped
from faker import Faker

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Reservas Hotel")
        self.geometry("1000x700")  

        self.connection = None
        self.fake = Faker()  
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Campos de entrada
        self.campos = {
            "DNI": ctk.CTkEntry(main_frame),
            "CUIL": ctk.CTkEntry(main_frame),
            "NOMBRE": ctk.CTkEntry(main_frame),
            "APELLIDO": ctk.CTkEntry(main_frame),
            "TELEFONO": ctk.CTkEntry(main_frame),
            "MAIL": ctk.CTkEntry(main_frame),
            "DOMICILIO": ctk.CTkEntry(main_frame),
            "CONDICION_IVA": ctk.CTkEntry(main_frame),
            "TIPO_DE_CLIENTE": ctk.CTkComboBox(main_frame, values=["NUEVO", "VIP", "REGULAR"]),
            "FNAC": DateEntry(main_frame),
            "OBSERVACIONES": ctk.CTkTextbox(main_frame, height=100)
        }

        for i, (label, widget) in enumerate(self.campos.items()):
            display_label = label.replace("_", " ")
            ttk.Label(main_frame, text=display_label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
            widget.grid(row=i, column=1, sticky="ew", padx=5, pady=5)

        # Botones para generar huéspedes
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.grid(row=0, column=2, rowspan=len(self.campos), padx=10, pady=5)

        ctk.CTkButton(button_frame, text="Generar 50 Huéspedes", command=lambda: self.generar_huespedes(50)).pack(padx=5, pady=5)
        ctk.CTkButton(button_frame, text="Generar 100 Huéspedes", command=lambda: self.generar_huespedes(100)).pack(padx=5, pady=5)
        ctk.CTkButton(button_frame, text="Generar 500 Huéspedes", command=lambda: self.generar_huespedes(500)).pack(padx=5, pady=5)

        # Botón para insertar huésped
        ctk.CTkButton(main_frame, text="Insertar Huésped", command=self.insertar_huesped).grid(row=len(self.campos), column=0, columnspan=2, pady=10)

        # Botón para conectar/desconectar BD
        self.btn_conexion = ctk.CTkButton(main_frame, text="Conectar BD", command=self.toggle_conexion)
        self.btn_conexion.grid(row=len(self.campos)+1, column=0, columnspan=2, pady=10)

    def toggle_conexion(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.btn_conexion.configure(text="Conectar BD", fg_color="blue")
            messagebox.showinfo("Desconexión", "Se ha desconectado de la base de datos.")
        else:
            try:
                self.connection = crear_conexion_bd()
                if self.connection:
                    self.btn_conexion.configure(text="Desconectar BD", fg_color="green")
                    messagebox.showinfo("Conexión Exitosa", "Se ha conectado exitosamente a la base de datos.")
                else:
                    raise Exception("No se pudo establecer la conexión.")
            except Exception as e:
                messagebox.showerror("Error de Conexión", f"No se pudo conectar a la base de datos.\nError: {str(e)}")

    def insertar_huesped(self):
        if not self.connection:
            messagebox.showerror("Error", "No hay conexión a la base de datos.")
            return

        datos = {campo: widget.get() for campo, widget in self.campos.items() if campo != "OBSERVACIONES"}
        datos["OBSERVACIONES"] = self.campos["OBSERVACIONES"].get("1.0", tk.END).strip()

        try:
            insertar_huesped(self.connection, **datos)
            messagebox.showinfo("Éxito", "Huésped insertado correctamente.")

        except Exception as e:
            error_message = f"No se pudo insertar el huésped.\nError: {str(e)}"
            print(error_message)  
            messagebox.showerror("Error", error_message)

    def generar_huespedes(self, cantidad):
        if not self.connection:
            messagebox.showerror("Error", "No hay conexión a la base de datos.")
            return

        for _ in range(cantidad):
            huesped = {
                "DNI": self.fake.unique.random_number(digits=8, fix_len=True),
                "CUIL": self.fake.unique.random_number(digits=11, fix_len=True),
                "NOMBRE": self.fake.first_name(),
                "APELLIDO": self.fake.last_name(),
                "TELEFONO": self.fake.phone_number(),
                "MAIL": self.fake.email(),
                "DOMICILIO": self.fake.address(),
                "CONDICION_IVA": self.fake.random_element(elements=["Responsable Inscripto", "Monotributista", "Consumidor Final"]),
                "TIPO_DE_CLIENTE": self.fake.random_element(elements=["NUEVO", "VIP", "REGULAR"]),
                "FNAC": self.fake.date_of_birth(minimum_age=18, maximum_age=80),
                "OBSERVACIONES": self.fake.text(max_nb_chars=200)
            }

            try:
                insertar_huesped(self.connection, **huesped)
                print(f"Huésped {huesped['NOMBRE']} {huesped['APELLIDO']} insertado correctamente.")
            except Exception as e:
                print(f"Error al insertar el huésped: {str(e)}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
