import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from tkcalendar import DateEntry
from crear_conexion_bd import conectar_bd
from insertar_datos import insertar_huesped
from faker import Faker
import os
import pyodbc

# Obtener la ruta del directorio actual donde está app.py
current_dir = os.path.dirname(os.path.abspath(__file__))

root = tk.Tk()
root.geometry("1080x720")
root.title("Reserva Hotel")

# CONFIG MENU COLOR
menu_bar_color = "#1e2330"

# ICONOS DE OPCIONES PRINCIPALES MENU
menu_icon = tk.PhotoImage(file=os.path.join(current_dir, 'imagenes', 'menu', 'menu.png'))
close_icon = tk.PhotoImage(file=os.path.join(current_dir, 'imagenes', 'menu', 'close.png'))
reserva_icon = tk.PhotoImage(file=os.path.join(current_dir, 'imagenes', 'menu', 'reserva.png'))
huesped_icon = tk.PhotoImage(file=os.path.join(current_dir, 'imagenes', 'menu', 'huesped.png'))
habitacion_icon = tk.PhotoImage(file=os.path.join(current_dir, 'imagenes', 'menu', 'habitacion.png'))
gerencia_icon = tk.PhotoImage(file=os.path.join(current_dir, 'imagenes', 'menu', 'gerencia.png'))
config_icon = tk.PhotoImage(file=os.path.join(current_dir, 'imagenes', 'menu', 'config.png'))

# FUNCIONES PARA CREAR LAS PAGINAS DE CADA OPCION

def reserva_page():
    # Frame principal para la página de reservas
    reserva_page_fm = tk.Frame(pagina_frame)
    
    # Variable para almacenar el botón actualmente seleccionado
    selected_button = None

    # Función para actualizar el estado de los botones y mostrar/ocultar secciones
    def update_button_state(button):
        nonlocal selected_button
        if selected_button:
            selected_button.config(fg="gray")  # Poner el texto en gris en el botón no seleccionado
        
        # Actualizar el botón seleccionado
        selected_button = button
        selected_button.config(fg=menu_bar_color)  # Poner el texto en negro en el botón seleccionado
        
        # Mostrar las secciones solo si el botón "Reservar" está seleccionado
        if button == reservar_btn:
            presupuesto_fm.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
            pago_fm.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
            checkinout_fm.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        else:
            presupuesto_fm.pack_forget()
            pago_fm.pack_forget()
            checkinout_fm.pack_forget()

    # Frame para los botones en la parte superior
    top_buttons_fm = tk.Frame(reserva_page_fm)
    top_buttons_fm.pack(fill=tk.X, pady=10)
    
    # Botón de Reservar
    reservar_btn = tk.Button(top_buttons_fm, text="Reservar", font=("Bold", 48), bd=0, fg="gray",
                             command=lambda: update_button_state(reservar_btn))
    reservar_btn.pack(side=tk.LEFT, padx=10)
    
    # Botón de Ver Reservas
    ver_reservas_btn = tk.Button(top_buttons_fm, text="Ver Reservas", font=("Bold", 48), bd=0, fg="gray",
                                 command=lambda: update_button_state(ver_reservas_btn))
    ver_reservas_btn.pack(side=tk.LEFT, padx=10)

    # Sub-Frames para secciones como Presupuesto, Pago, Check-In, etc.
    sections_fm = tk.Frame(reserva_page_fm)
    sections_fm.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Ejemplo de sección de Presupuesto
    presupuesto_fm = tk.Frame(sections_fm, bg="lightgrey", padx=10, pady=10)
    tk.Label(presupuesto_fm, text="Presupuesto", font=("Bold", 15)).pack(pady=5)
    tk.Entry(presupuesto_fm).pack(pady=5)
    
    # Sección de Pago
    pago_fm = tk.Frame(sections_fm, bg="lightgrey", padx=10, pady=10)
    tk.Label(pago_fm, text="Pago", font=("Bold", 15)).pack(pady=5)
    tk.Entry(pago_fm).pack(pady=5)
    
    # Sección de Check-In/Check-Out
    checkinout_fm = tk.Frame(sections_fm, bg="lightgrey", padx=10, pady=10)
    tk.Label(checkinout_fm, text="Check In", font=("Bold", 15)).pack(pady=5)
    tk.Entry(checkinout_fm).pack(pady=5)
    tk.Label(checkinout_fm, text="Check Out", font=("Bold", 15)).pack(pady=5)
    tk.Entry(checkinout_fm).pack(pady=5)
    
    # Empacar el frame principal
    reserva_page_fm.pack(fill=tk.BOTH, expand=True)

    # Marcar el botón "Reservar" como seleccionado al cargar la página
    update_button_state(reservar_btn)



def huesped_page():
    # Frame principal para la página de huesped
    huesped_page_fm = tk.Frame(pagina_frame)
    
    # Variable para almacenar el botón actualmente seleccionado
    selected_button = None

    # Función para actualizar el estado de los botones y mostrar/ocultar secciones
    def update_button_state(button):
        nonlocal selected_button
        if selected_button:
            selected_button.config(fg="gray")  # Poner el texto en gris en el botón no seleccionado
        
        # Actualizar el botón seleccionado
        selected_button = button
        selected_button.config(fg=menu_bar_color)  # Poner el texto en negro en el botón seleccionado
        
        # Mostrar las secciones solo si el botón "Reservar" está seleccionado
        if button == huesped_btn:
            registro_huesped_fm.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        else:
            registro_huesped_fm.pack_forget()


    # Frame para los botones en la parte superior
    top_buttons_fm = tk.Frame(huesped_page_fm)
    top_buttons_fm.pack(fill=tk.X, pady=10)
    
    # Botón de Reservar
    huesped_btn = tk.Button(top_buttons_fm, text="Nuevo Huésped", font=("Bold", 48), bd=0, fg="gray",
                             command=lambda: update_button_state(huesped_btn))
    huesped_btn.pack(side=tk.LEFT, padx=10)
    
    # Botón de Ver Reservas
    ver_huesped_btn = tk.Button(top_buttons_fm, text="Ver Huéspedes", font=("Bold", 48), bd=0, fg="gray",
                                 command=lambda: update_button_state(ver_huesped_btn))
    ver_huesped_btn.pack(side=tk.LEFT, padx=10)

    # Sub-Frames para secciones como Registrar, Pago, Check-In, etc.
    sections_fm = tk.Frame(huesped_page_fm)
    sections_fm.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Ejemplo de sección de Registrar
    registro_huesped_fm = tk.Frame(sections_fm, bg="lightgrey", padx=10, pady=10)
    tk.Label(registro_huesped_fm, text="Registrar Nuevo Huésped", font=("Bold", 15)).pack(pady=5)
    tk.Entry(registro_huesped_fm).pack(pady=5)
    
    # Empacar el frame principal
    huesped_page_fm.pack(fill=tk.BOTH, expand=True)

    # Marcar el botón "Huesped" como seleccionado al cargar la página
    update_button_state(huesped_btn)

    
def habitacion_page():
    # Frame principal para la página de huesped
    habitacion_page_fm = tk.Frame(pagina_frame)
    
    # Variable para almacenar el botón actualmente seleccionado
    selected_button = None

    # Función para actualizar el estado de los botones y mostrar/ocultar secciones
    def update_button_state(button):
        nonlocal selected_button
        if selected_button:
            selected_button.config(fg="gray")  # Poner el texto en gris en el botón no seleccionado
        
        # Actualizar el botón seleccionado
        selected_button = button
        selected_button.config(fg=menu_bar_color)  # Poner el texto en negro en el botón seleccionado
        
        # Mostrar las secciones solo si el botón "Reservar" está seleccionado
        if button == habitacion_btn:
            habitacion_fm.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        else:
            habitacion_fm.pack_forget()


    # Frame para los botones en la parte superior
    top_buttons_fm = tk.Frame(habitacion_page_fm)
    top_buttons_fm.pack(fill=tk.X, pady=10)
    
    # Botón de Reservar
    habitacion_btn = tk.Button(top_buttons_fm, text="Habitaciones", font=("Bold", 48), bd=0, fg="gray",
                             command=lambda: update_button_state(habitacion_btn))
    habitacion_btn.pack(side=tk.LEFT, padx=10)
    
    # Botón de Ver Reservas
    servicios_btn = tk.Button(top_buttons_fm, text="Servicios Adicionales", font=("Bold", 48), bd=0, fg="gray",
                                 command=lambda: update_button_state(servicios_btn))
    servicios_btn.pack(side=tk.LEFT, padx=10)

    # Sub-Frames para secciones como Registrar, Pago, Check-In, etc.
    sections_fm = tk.Frame(habitacion_page_fm)
    sections_fm.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Ejemplo de sección de Registrar
    habitacion_fm = tk.Frame(sections_fm, bg="lightgrey", padx=10, pady=10)
    tk.Label(habitacion_fm, text="Ver Habitaciones", font=("Bold", 15)).pack(pady=5)
    tk.Entry(habitacion_fm).pack(pady=5)
    
    # Empacar el frame principal
    habitacion_page_fm.pack(fill=tk.BOTH, expand=True)

    # Marcar el botón "Huesped" como seleccionado al cargar la página
    update_button_state(habitacion_btn)
    
def gerente_page():
    # Frame principal para la página de huesped
    gerente_page_fm = tk.Frame(pagina_frame)
    
    # Variable para almacenar el botón actualmente seleccionado
    selected_button = None

    # Función para actualizar el estado de los botones y mostrar/ocultar secciones
    def update_button_state(button):
        nonlocal selected_button
        if selected_button:
            selected_button.config(fg="gray")  # Poner el texto en gris en el botón no seleccionado
        
        # Actualizar el botón seleccionado
        selected_button = button
        selected_button.config(fg=menu_bar_color)  # Poner el texto en negro en el botón seleccionado
        
        # Mostrar las secciones solo si el botón "Reservar" está seleccionado
        if button == empleado_btn:
            empleado_fm.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        else:
            empleado_fm.pack_forget()


    # Frame para los botones en la parte superior
    top_buttons_fm = tk.Frame(gerente_page_fm)
    top_buttons_fm.pack(fill=tk.X, pady=10)
    
    # Botón de Empleados
    empleado_btn = tk.Button(top_buttons_fm, text="Empleados", font=("Bold", 48), bd=0, fg="gray",
                             command=lambda: update_button_state(empleado_btn))
    empleado_btn.pack(side=tk.LEFT, padx=10)
    
    # Botón de Ver Reportes
    reportes_btn = tk.Button(top_buttons_fm, text="Reportes", font=("Bold", 48), bd=0, fg="gray",
                                 command=lambda: update_button_state(reportes_btn))
    reportes_btn.pack(side=tk.LEFT, padx=10)

    # Botón de Ver Actualizacion de Servicios
    actualizar_btn = tk.Button(top_buttons_fm, text="Servicios", font=("Bold", 48), bd=0, fg="gray",
                                 command=lambda: update_button_state(actualizar_btn))
    actualizar_btn.pack(side=tk.LEFT, padx=10)

    # Sub-Frames para secciones como Registrar, Pago, Check-In, etc.
    sections_fm = tk.Frame(gerente_page_fm)
    sections_fm.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Ejemplo de sección de Registrar
    empleado_fm = tk.Frame(sections_fm, bg="lightgrey", padx=10, pady=10)
    tk.Label(empleado_fm, text="Registrar Nuevo Huésped", font=("Bold", 15)).pack(pady=5)
    tk.Entry(empleado_fm).pack(pady=5)
    
    # Empacar el frame principal
    gerente_page_fm.pack(fill=tk.BOTH, expand=True)

    # Marcar el botón "Huesped" como seleccionado al cargar la página
    update_button_state(gerente_btn)

# Valores predeterminados para los campos de la base de datos
default_server = 'TSSIT01'
default_database = 'reservahotel'
default_user = 'Soporte'
default_password = 'Instituto_2023'


# Función para la página de configuraciones
def config_page():
    # Frame principal para la página de configuración
    config_page_fm = tk.Frame(pagina_frame)

    # Frame para los botones en la parte superior
    top_buttons_fm = tk.Frame(config_page_fm)
    top_buttons_fm.pack(fill=tk.X, pady=10)

    # Botón de Configuración
    config_btn = tk.Button(top_buttons_fm, text="Configurar Base de Datos", font=("Bold", 48), bd=0, fg=menu_bar_color)
    config_btn.pack(side=tk.LEFT, padx=10)

    # Sub-Frame para la sección de configuración
    sections_fm = tk.Frame(config_page_fm)
    sections_fm.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    # Frame interno para los campos de configuración
    configurar_fm = tk.Frame(sections_fm, bg="lightgrey", padx=10, pady=10)
    configurar_fm.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Variables de entrada para los campos
    server_var = tk.StringVar(value=default_server)
    database_var = tk.StringVar(value=default_database)
    user_var = tk.StringVar(value=default_user)
    password_var = tk.StringVar(value=default_password)

    # Campos de configuración de conexión
    tk.Label(configurar_fm, text="Servidor:", font=("Arial", 12)).pack(anchor='w', padx=20)
    server_entry = tk.Entry(configurar_fm, textvariable=server_var)
    server_entry.pack(fill=tk.X, padx=20, pady=5)

    tk.Label(configurar_fm, text="Base de Datos:", font=("Arial", 12)).pack(anchor='w', padx=20)
    database_entry = tk.Entry(configurar_fm, textvariable=database_var)
    database_entry.pack(fill=tk.X, padx=20, pady=5)

    tk.Label(configurar_fm, text="Usuario:", font=("Arial", 12)).pack(anchor='w', padx=20)
    user_entry = tk.Entry(configurar_fm, textvariable=user_var)
    user_entry.pack(fill=tk.X, padx=20, pady=5)

    tk.Label(configurar_fm, text="Contraseña:", font=("Arial", 12)).pack(anchor='w', padx=20)
    password_entry = tk.Entry(configurar_fm, textvariable=password_var, show="*")
    password_entry.pack(fill=tk.X, padx=20, pady=5)

    # Conexión y desconexión de base de datos
    connection = None

    # Función para conectar
    def conectar():
        nonlocal connection
        connection = conectar_bd(
            server_var.get(),
            database_var.get(),
            user_var.get(),
            password_var.get()
        )
        if connection:
            status_label.config(text="Conectado a la base de datos", fg="green")
        else:
            status_label.config(text="Error al conectar", fg="red")

    # Función para desconectar
    def desconectar():
        nonlocal connection
        if connection:
            connection.close()
            connection = None
            status_label.config(text="Desconectado", fg="red")
            print("Conexión cerrada exitosamente.")
        else:
            status_label.config(text="No hay conexión activa", fg="red")

    # Botones de Conectar y Desconectar
    connect_btn = tk.Button(configurar_fm, text="Conectar", command=conectar, bg="lightgreen", font=("Bold", 12))
    connect_btn.pack(side=tk.LEFT, padx=20, pady=20)

    disconnect_btn = tk.Button(configurar_fm, text="Desconectar", command=desconectar, bg="lightcoral", font=("Bold", 12))
    disconnect_btn.pack(side=tk.LEFT, padx=20, pady=20)

    # Etiqueta de estado de conexión
    status_label = tk.Label(configurar_fm, text="Desconectado", font=("Arial", 12), fg="red")
    status_label.pack(pady=10)

    # Empacar el frame principal
    config_page_fm.pack(fill=tk.BOTH, expand=True)



# CREACION DE LAS  PAGINAS QUE CONTIENEN LAS OPCIONES PRINCIPALES
pagina_frame = tk.Frame(root, bg='gainsboro')
pagina_frame.place(relwidth=1.0, relheight=1.0, x=50)
reserva_page()



menu_bar_frame = tk.Frame(root, bg=menu_bar_color)

# FUNCION DEL INDICADOR OPCION SELECIONADA

def cambio_indicator(indicator_lb, page):
    reserva_btn_indicator.config(bg=menu_bar_color)
    huesped_btn_indicator.config(bg=menu_bar_color)
    habitacion_btn_indicator.config(bg=menu_bar_color)
    gerente_btn_indicator.config(bg=menu_bar_color)
    config_btn_indicator.config(bg=menu_bar_color)
    
    indicator_lb.config(bg='white')
    
    if menu_bar_frame.winfo_width() > 65:
        contraer_menu_bar()
        
    for frame in pagina_frame.winfo_children():
        frame.destroy()
    
    page()
    
    

# FUNCION EXPANSION DE MENU

def extender_menu_bar():
    menu_bar_frame.config(width=250)
    menu_btn.config(image=close_icon)
    menu_btn.config(command=contraer_menu_bar)

# FUNCION CONTRAER DE MENU

def contraer_menu_bar():
     menu_bar_frame.config(width=65)
     menu_btn.config(image=menu_icon)
     menu_btn.config(command=extender_menu_bar)



        
# BOTON DEL MENU
menu_btn = tk.Button(menu_bar_frame, 
                    image=menu_icon, 
                    bg=menu_bar_color,
                    bd=0, 
                    activebackground=menu_bar_color,
                    command=extender_menu_bar)
menu_btn.place(x=4, y=10)


# BOTON DE RESERVA
reserva_btn = tk.Button(menu_bar_frame, 
                       image=reserva_icon, 
                       bg=menu_bar_color,
                       bd=0, 
                       activebackground=menu_bar_color,
                       command=lambda: cambio_indicator(indicator_lb=reserva_btn_indicator,
                                                        page=reserva_page))
reserva_btn.place(x=9, y=200)

# INDICADOR BOTON
reserva_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
reserva_btn_indicator.place(x=3, y=200, height=45, width=3)

# NOMBRE BOTON / PAGINA
reserva_page_lb = tk.Label(menu_bar_frame,
                          text='Reservas',
                          bg = menu_bar_color,
                          fg = 'white',
                          font = ('Bold', 15),
                          anchor=tk.W)
reserva_page_lb.place(x=70,
                      y=200,
                      width=180,
                      height=40)

reserva_page_lb.bind('<Button-1>', lambda e: cambio_indicator(indicator_lb=reserva_btn_indicator, page=reserva_page))

# BOTON DE HUESPED
huesped_btn = tk.Button(menu_bar_frame, 
                       image=huesped_icon, 
                       bg=menu_bar_color,
                       bd=0, 
                       activebackground=menu_bar_color,
                       command=lambda: cambio_indicator(indicator_lb=huesped_btn_indicator,
                                                        page=huesped_page))
huesped_btn.place(x=9, y=270)

# INDICADOR BOTON
huesped_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
huesped_btn_indicator.place(x=3, y=270, height=45, width=3)

# NOMBRE BOTON / PAGINA
huesped_page_lb = tk.Label(menu_bar_frame,
                          text='Huésped',
                          bg = menu_bar_color,
                          fg = 'white',
                          font = ('Bold', 15),
                          anchor=tk.W)
huesped_page_lb.place(x=70,
                      y=270,
                      width=180,
                      height=40)

huesped_page_lb.bind('<Button-1>', lambda e: cambio_indicator(indicator_lb=huesped_btn_indicator, page=huesped_page))

# BOTON DE HABITACION
habitacion_btn = tk.Button(menu_bar_frame, 
                          image=habitacion_icon, 
                          bg=menu_bar_color,
                          bd=0, 
                          activebackground=menu_bar_color,
                          command=lambda: cambio_indicator(indicator_lb=habitacion_btn_indicator,
                                                           page=habitacion_page))
habitacion_btn.place(x=9, y=340)

# INDICADOR BOTON
habitacion_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
habitacion_btn_indicator.place(x=3, y=340, height=45, width=3)

# NOMBRE BOTON / PAGINA
habitacion_page_lb = tk.Label(menu_bar_frame,
                          text='Habitaciones',
                          bg = menu_bar_color,
                          fg = 'white',
                          font = ('Bold', 15),
                          anchor=tk.W)
habitacion_page_lb.place(x=70,
                      y=340,
                      width=180,
                      height=40)

habitacion_page_lb.bind('<Button-1>', lambda e: cambio_indicator(indicator_lb=habitacion_btn_indicator, page=habitacion_page))

# BOTON DE GERENTE
gerente_btn = tk.Button(menu_bar_frame, 
                       image=gerencia_icon, 
                       bg=menu_bar_color,
                       bd=0, 
                       activebackground=menu_bar_color,
                       command=lambda: cambio_indicator(indicator_lb=gerente_btn_indicator,
                                                        page=gerente_page))
gerente_btn.place(x=9, y=410)

# INDICADOR BOTON
gerente_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
gerente_btn_indicator.place(x=3, y=410, height=45, width=3)

# NOMBRE BOTON / PAGINA
gerente_page_lb = tk.Label(menu_bar_frame,
                          text='Gerencia',
                          bg = menu_bar_color,
                          fg = 'white',
                          font = ('Bold', 15),
                          anchor=tk.W)
gerente_page_lb.place(x=70,
                      y=410,
                      width=180,
                      height=40)

gerente_page_lb.bind('<Button-1>', lambda e: cambio_indicator(indicator_lb=gerente_btn_indicator, page=gerente_page))

# BOTON DE CONFIGURACION
config_btn = tk.Button(menu_bar_frame, 
                      image=config_icon, 
                      bg=menu_bar_color,
                      bd=0, 
                      activebackground=menu_bar_color,
                      command=lambda: cambio_indicator(indicator_lb=config_btn_indicator,
                                                       page=config_page))
config_btn.place(x=9, y=480)

# INDICADOR BOTON
config_btn_indicator = tk.Label(menu_bar_frame, bg=menu_bar_color)
config_btn_indicator.place(x=3, y=480, height=45, width=3)

# NOMBRE BOTON / PAGINA
config_page_lb = tk.Label(menu_bar_frame,
                          text='Configuraciones',
                          bg = menu_bar_color,
                          fg = 'white',
                          font = ('Bold', 15),
                          anchor=tk.W)
config_page_lb.place(x=70,
                      y=480,
                      width=180,
                      height=40)

config_page_lb.bind('<Button-1>', lambda e: cambio_indicator(indicator_lb=config_btn_indicator, page=config_page))

menu_bar_frame.pack(side=tk.LEFT, fill=tk.Y)
menu_bar_frame.pack_propagate(False)
menu_bar_frame.configure(width=65)

root.mainloop()