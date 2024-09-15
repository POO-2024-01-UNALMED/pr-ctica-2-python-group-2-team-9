#Autores: Ricardo Fuentes, Valery Fernandez, Juan Luis Sucerquia, Mariana Sanchez

from tkinter import messagebox
from tkinter.ttk import Combobox
from excepciones.ErrorAplicacion import *
from excepciones.ErrorAsignacion import *
from excepciones.ErrorFormato  import *
from tkinter import *
from FieldFrame import *
from gestorAplicacion.alojamiento.Alojamiento import Alojamiento
from gestorAplicacion.adminVuelos.Aerolinea import Aerolinea

class VentanaSecundaria(Toplevel):
    en_uso = False #Permite saber si hay una ventanaSecundaria abierta

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Ventana secundaria")
        self.option_add('*tearOff', FALSE)
        self.title("Aeropuerto El Sol")
        self.geometry("800x550")
        self.iconbitmap('SRC/imagenes/icono.ico')
        self.ventanaInicio = None
        self.focus()

        #ZONA DE Frames
        self.frame = Frame(self,relief="groove",bd=2)
        self.frame.pack(ipadx=50, padx=15,ipady=20,pady=15,expand=True,fill=BOTH)
        self.frame_proceso = Frame(self.frame,bg="gray80")
        self.frame_proceso.pack(ipadx=6, padx=2,ipady=2,pady=2,fill=X)
        self.frame_proceso.config(relief = "ridge")
        self.frame_proceso.config(bd=2)
        self.frame_descripcion = Frame(self.frame ,relief="ridge",bg="gray90")
        self.frame_descripcion.pack(ipadx=2, padx=2,ipady=2,pady=2,fill=X)
        self.frame_descripcion.config(bd=2)
        self.ventana_operaciones = Frame(self.frame,relief="groove",bd=2)
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=BOTH,expand = True)
        #FIN ZONA DE FRAME

        #ZONA DE Menus
        self.menubar = Menu(self)

        self.menuArchivo = Menu(self.menubar)
        self.menuArchivo.add_command(label = "Aplicacion", command = self.descripcionApp)
        self.menuArchivo.add_command(label = "Salir", command = self.salirVentana)

        self.menuProcesos = Menu(self.menubar)
        self.menuProcesos.add_command(label = "Ver vuelos disponibles por Aerolineas",command= self.mostrarVuelosPorAerolineas)
        self.menuProcesos.add_command(label = "Comprar tiquete para un vuelo por destino y fecha", command = self.generarTiquete)
        self.menuProcesos.add_command(label = "Agregar alojamiento en el destino del vuelo", command = self.agregarAlojamientoTiquete )
        self.menuProcesos.add_command(label = "Modificar tiquete comprado", command = self.modificarTiquete)

        self.menuAdmin = Menu(self.menuProcesos)
        self.menuProcesos.add_cascade(menu = self.menuAdmin,label = "Ver opciones de administrador")
        self.menuAdmin.add_command(label= "Listar pasajeros",command=self.listarPasajeros)
        self.menuAdmin.add_command(label= "Agregar vuelo",command=self.agregarVuelo)
        self.menuAdmin.add_command(label= "Cancelar vuelo",command=self.cancelarVuelo)
        self.menuAdmin.add_command(label= "Retirar avion",command=self.retirarAvion)
        self.menuAdmin.add_command(label= "Agregar alojamiento",command=self.agregarAlojamiento)
        self.menuAdmin.add_command(label= "Eliminar Alojamiento",command=self.eliminarAlojamiento)

        self.menuAyuda = Menu(self.menubar)
        self.menuAyuda.add_command(label = "Acerca de", command = self.ayuda)

        self.menubar.add_cascade(label = "Archivo", menu = self.menuArchivo)
        self.menubar.add_cascade(label = "Procesos y Consultas", menu = self.menuProcesos)
        self.menubar.add_cascade(label = "Ayuda", menu = self.menuAyuda)
        self["menu"] = self.menubar
        #FIN ZONAS DE MENUS


        #ZONA DE LABELS
        self.label_proceso = Label(self.frame_proceso,text= "Administrador Sistema de Reserva de Vuelos", font = ("Segoe UI", 12,"bold"),height=2, bg="gray80")
        self.label_proceso.pack(ipadx = 2, ipady =2, padx = 5, pady= 5)

        self.label_descripcion = Label(self.frame_descripcion, text = "Realiza reservaciones de vuelos y alojamientos, y mantén la informacion actualizada de vuelos, aviones y alojamientos", font = ("Segoe UI", 10), bg="gray90")
        self.label_descripcion.pack(ipadx = 2, ipady = 2, padx = 5, pady= 5)

        self.labelTexto = Label(self.ventana_operaciones, text = "Puedes hacerlo con las acciones dispuestas en el menu <Procesos y consultas>", font = ("Segoe UI", 10))
        self.labelInicio = Label(self.ventana_operaciones)
        self.imagenInicio = PhotoImage(file = 'SRC/imagenes/Reservacion.png')
        self.labelInicio["image"] = self.imagenInicio
        self.labelTexto.pack(ipadx = 10, ipady =10, padx = 10, pady= 10)
        self.labelInicio.pack(ipadx = 10, ipady =10, padx = 10, pady= 10)
        #FIN ZONA DE Labels

        self.contador_mostrarVuelosPorAerolineas = 0
        self.__class__.en_uso = True

    #--------------------------------------------------------------------------------------------------------------
    #Se despliega un Message Box con la informacion basica de lo que hace la aplicacion.
    def descripcionApp(self):
        descripcion = messagebox.showinfo(title = "Informacion", message = "SISTEMA DE RESERVA DE VUELOS",
        detail = "La aplicacion permite hacer reservaciones de un vuelo y un alojamiento en el lugar de destino, ademas de algunas opciones de administrador.")

    #--------------------------------------------------------------------------------------------------------------
    # Retorna a la Ventana de Inicio del programa.
    def salirVentana(self):
        self.__class__.en_uso = False
        self.ventanaInicio.deiconify()
        return super().destroy()

    #---------------------------------------------------------------------------------------------------------------------------------------
    # Muestra los vuelos disponibles por aerolinea, cada una en un frame que se actualiza por otro cada vez que se presiona el botón siguiente

    def mostrarVuelosPorAerolineas(self):
        self.label_proceso.config(text = "Vuelos disponibles por aerolínea")
        self.label_descripcion.config(text = "Aquí puede visualizar los vuelos que están disponibles por nuestrar aerolíneas")
        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones= Frame(self.frame,relief="groove",bd=2)
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=X)

        # Se ejecuta cada vez que se presiona el boton "siguiente", para reemplazar el label mostrado por pantalla
        def siguiente():
            self.contador_mostrarVuelosPorAerolineas +=1
            if self.contador_mostrarVuelosPorAerolineas == len(lista_labels):
                self.contador_mostrarVuelosPorAerolineas =0
            lista_labels[self.contador_mostrarVuelosPorAerolineas-1].pack_forget()
            lista_labels[self.contador_mostrarVuelosPorAerolineas].pack()

        boton_siguiente = Button(self.ventana_operaciones,text= "Siguiente",command=siguiente)
        boton_siguiente.pack()
        lista_labels=Admin.mostrarVuelosPorAerolineas(self.ventana_operaciones)
        lista_labels[0].pack()

    #-------------------------------------------------------------------------------------------------------------------------------------
    # Funcion auxiliar que permite mostrar una lista de vuelos disponibles por cada aerolinea hacia un destino seleccionado por el usuario
    # cada aerolinea en un frame que se actualiza por otro cada vez que se presiona el botón siguiente, y continuar con la compra de un
    # tiquete

    def buscarVuelos(self,formulario):
        try:
            hay_excepcion = formulario.aceptar()
        except ExcepcionStringNumero as owo:
            messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
            # self.generarTiquete()
            return
        if hay_excepcion:
            self.generarTiquete()
            return

        self.label_proceso.config(text = "Vuelos disponibles")
        self.label_descripcion.config(text = "Lista los vuelos disponibles de acuerdo a los parámetros ingresados")

        self.ventana_operaciones.pack_forget()

        hayFecha = False
        fecha = None
        destino = formulario.valor_entradas[0]
        lista_general = None

        if len(formulario.valor_entradas) == 2:
            hayFecha = True
            fecha = formulario.valor_entradas[1]