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

        self.ventana_operaciones = Frame(self.frame)
        self.ventana_operaciones.pack()

        if hayFecha:
            label = Label(self.ventana_operaciones, text = "Estos son los vuelos disponibles hacia: " + destino + " en la fecha " + fecha + " por nuestras aerolineas")
            label.pack()
            lista_general = Admin.consultarVuelosPorDestinoYFecha(destino, fecha, self.ventana_operaciones)
        else:
            label = Label(self.ventana_operaciones, text = "Estos son los vuelos disponibles hacia: " + destino + " por nuestras aerolineas")
            label.pack()
            lista_general = Admin.consultarVuelosPorDestino(destino, self.ventana_operaciones)
        if len(lista_general[0]) ==0:
            if hayFecha:
                messagebox.showinfo(title="Vuelos Disponibles",message= "Lo sentimos, no tenemos vuelos diponibles hacia " + destino+" en la fecha: " +fecha )
            else:
                messagebox.showinfo(title="Vuelos Disponibles",message= "Lo sentimos, no tenemos vuelos diponibles hacia " + destino )
            self.generarTiquete()
            return

        # Se ejecuta cada vez que se presiona el boton "siguiente", para reemplazar el label mostrado por pantalla

        def siguiente():
            self.contador_mostrarVuelosPorAerolineas +=1
            if self.contador_mostrarVuelosPorAerolineas == len(lista_labels):
                self.contador_mostrarVuelosPorAerolineas =0
            lista_labels[self.contador_mostrarVuelosPorAerolineas-1].pack_forget()
            lista_labels[self.contador_mostrarVuelosPorAerolineas].pack()

        boton_siguiente = Button(self.ventana_operaciones,text= "Siguiente",command = siguiente)
        boton_siguiente.pack()

        lista_labels = lista_general[0]
        lista_labels[0].pack()

        boton_siguiente = Button(self.ventana_operaciones,text= "Continuar con la compra", command = lambda: self.comprarTiquete(lista_general[1]))
        boton_siguiente.pack(side = BOTTOM)

        if len(lista_labels) == 0:
            messagebox.showinfo(title = "Buscar vuelos", message = "Lo sentimos, no tenemos vuelos hacia ese destino")
            return

    #-------------------------------------------------------------------------------------------------------------------------------------
    # Funcion auxiliar que permite continuar con la generacion de un tiquete de vuelo, pregunta por la aerolinea y vuelo que se
    # desea comprar, recoge las especificaciones de la silla y los datos del pasajero, para al final mostrar un resumen de la compra

    def comprarTiquete(self, nombres_aerolineas):
        self.label_proceso.config(text = "Compra del vuelo")
        self.label_descripcion.config(text = "Para efectuar la compra, seleccione la aerolínea con la que quiere viajar y el ID del vuelo que quiere comprar")

        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = Frame(self.frame)
        self.ventana_operaciones.pack()

        labelNombreAerolinea = Label(self.ventana_operaciones, text = "Seleccione la aerolinea con la que desea viajar")
        labelNombreAerolinea.pack(ipadx = 5, ipady = 5, padx = 3, pady= 3)

        # Es llamada cuando se selecciona una aerolinea en el combobox, y despliega un formulario que pregunta por el ID del vuelo a comprar

        def aerolineaSeleccionada(e):
            nombre = str(aerolineas.get())
            aerolinea = Aerolinea.buscarAerolineaPorNombre(nombre)
            aerolineas.config(state = DISABLED)
            label_id_tiquete = Label(self.ventana_operaciones,text="Ingrese el ID del vuelo que desea comprar.")
            label_id_tiquete.pack()
            formulario = FieldFrame(self.ventana_operaciones,"Info",["ID vuelo"],"valor",None,None,["int"])

            # Es llamada cuando se ingresa un ID, y continua con la toma de los datos del pasajero y de la silla. Al finalizar muestra por
            # pantalla un resumen de la compra desde el metodo modificarSilla

            def idVueloIngresado():
                self.ventana_operaciones.pack_forget()
                self.ventana_operaciones = Frame(self.frame)
                self.ventana_operaciones.pack()

                try:
                    hay_excepcion = formulario.aceptar()
                except ExcepcionEnteroString as owo:
                    messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                    aerolineaSeleccionada(4)
                    return

                if hay_excepcion:
                    aerolineaSeleccionada(9)
                    return

                id_vuelo = int(formulario.valor_entradas[0])
                vuelo = aerolinea.buscarVueloPorID(aerolinea.getVuelos(),id_vuelo)
                if vuelo == None:
                    messagebox.showinfo(title="Elegir vuelo",message="No existe un vuelo con ese ID en la aerolinea"+aerolinea.getNombre())
                    return

                self.label_proceso.config(text = "Toma de datos Pasajero")
                self.label_descripcion.config(text = "Recoge los datos del pasajero al que se le asociará el tiquete de compra")

                label_datos_pasajero = Label(self.ventana_operaciones,text="Ingrese los datos del pasajero.")
                label_datos_pasajero.pack()
                formulario_pasajero= FieldFrame(self.ventana_operaciones,"criterios",["Nombre","Edad","Pasaporte","E-mail"],"dAtOs",None,None,["string","int","string","string"])

                def datosPasajero():

                    self.label_proceso.config(text = "Resumen de la compra")
                    self.label_descripcion.config(text = "Enseña un breve resumen de la compra efectuada, recogida en el tiquete")

                    try:
                        hay_excepcion = formulario_pasajero.aceptar()
                    except ExcepcionEnteroString as owo:
                        messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                        return
                    except ExcepcionEnteroFloat as owo:
                        messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                        return
                    except ExcepcionStringNumero as owo:
                        messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                        return

                    if hay_excepcion:
                        return

                    tiquete=Admin.generarTiquete(vuelo)
                    formulario_pasajero.pack_forget()
                    Admin.asignarTiquete(formulario_pasajero.valor_entradas,tiquete)
                    self.modificarSilla(1,tiquete)  


                formulario_pasajero.botonAceptar.config(command=datosPasajero)

            formulario.botonAceptar.config(command=idVueloIngresado)

        aerolineas = Combobox(self.ventana_operaciones, values = nombres_aerolineas)
        aerolineas.pack(padx = 3, pady= 3)
        aerolineas.bind("<<ComboboxSelected>>",aerolineaSeleccionada)


    #-------------------------------------------------------------------------------------------------------------------------------------
    # Permite realizar la compra de un tiquete para un vuelo disponible, permitiendo buscar por destino y fecha, filtrar los vuelos, seleccionar
    # el vuelo y la silla a comprar. Por último, se recogen los datos del pasajero y se imprime por pantalla un resumen de la compra

    def generarTiquete(self):
        self.label_proceso.config(text = "Compra de un tiquete")
        self.label_descripcion.config(text = "Permite realizar la compra de un tiquete para un vuelo, buscando por destino o por destino y fecha.")

        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = Frame(self.frame)
        self.ventana_operaciones.pack()
        frame_botones = Frame(self.ventana_operaciones)
        frame_botones.pack(ipadx = 10, ipady =10, padx = 10, pady= 10)
        label = Label(frame_botones,text="Buscar vuelo por:")
        label.grid(row = 0, column =0,columnspan=2)

        # Es llamada si se eligió buscar un vuelo por Destino, recogiendo el destino deseado en un formulario y pasándoselo a la funcion
        # buscarVuelos

        def buscarPorDestino():
            self.label_proceso.config(text = "Buscar por destino")
            self.label_descripcion.config(text = "Ingresa el destino al que quiere viajar")

            boton_destino["state"]=DISABLED
            boton_destino_fecha["state"]=DISABLED
            formulario_destino=FieldFrame(self.ventana_operaciones,"Criterio",["Destino"],"Valor",None,None,["string"])
            formulario_destino.botonAceptar.config(command=lambda:self.buscarVuelos(formulario_destino))

        # Es llamada si se eligió buscar un vuelo por Destino y fecha, recogiendo el destino y la fecha deseados en un formulario y pasándoselo
        # a la funcion buscarVuelos

        def buscarPorDestinoYFecha():
            self.label_proceso.config(text = "Buscar por destino y fecha")
            self.label_descripcion.config(text = "Ingresa el destino y la fecha en la que quiere viajar")

            boton_destino_fecha["state"]=DISABLED
            boton_destino["state"]=DISABLED
            formulario_destino_fecha=FieldFrame(self.ventana_operaciones,"Criterio",["Destino","Fecha (DD-MM-AAAA)"],"Valor",None,None,["string","string"])
            formulario_destino_fecha.botonAceptar.config(command=lambda:self.buscarVuelos(formulario_destino_fecha))

        boton_destino = Button(frame_botones,text = "Destino",font=("Segoe UI", 10),command=buscarPorDestino)
        boton_destino.grid(row=1,column=0,padx=2,ipadx=5)
        boton_destino_fecha = Button(frame_botones,text = "Destino y fecha",font = ("Segoe UI", 10),command=buscarPorDestinoYFecha)
        boton_destino_fecha.grid(row=1,column=1,padx=2,ipadx=5)

    #-------------------------------------------------------------------------------------------------------------------------------------
    # Permite agregar un alojamiento a un tiquete comprado previamente, verificando que el tiquete exista y que no se tenga un alojamiento
    # comprado previamente, luego se listan (Label) los alojamientos ofrecidos en el destino que tiene el tiquete para que el usuario escoja
    # uno de ellos. Si esta disponible, se procede a preguntar (FieldFrame) cuantos dias son de estadia, se recalcula el precio del tiquete
    # y se muestra un resumen de la compra.

    def agregarAlojamientoTiquete(self):
        self.label_proceso.config(text = "Añadir un alojamiento a su compra")
        self.label_descripcion.config(text = "Permite añadir un alojamiento a su tiquete,\nmostrando los alojamientos disponibles en el lugar de destino")

        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = Frame(self.frame)
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=X)
        formulario = FieldFrame(self.ventana_operaciones,"info",["ID del tiquete"],"",None,None,["int"])

        # Funcion que se dispara cuando se presiona el botón aceptar del formulario que pregunta por el ID del tiquete al que se le desea cambiar
        # el alojamiento, desde aca se hacen los pasos necesarios para preguntar por el alojamiento que se quiere agregar y los días de estadia
        # para adjuntarselos al tiquete y recalcular su precio

        def eventoAgregarAlojamiento():
            self.label_descripcion.config(text = "Agregue un alojamiento a su tiquete de compra, seleccionando uno de la lista")
            formulario.pack_forget()

            try:
                hay_excepcion = formulario.aceptar()
            except ExcepcionEnteroString as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.agregarAlojamientoTiquete()
                return
            except ExcepcionEnteroFloat as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.agregarAlojamientoTiquete()
                return

            if hay_excepcion:
                self.agregarAlojamientoTiquete()
                return

            id_tiquete = formulario.valor_entradas[0]

            try:
                tiquete_solicitado =Admin.buscarTiqueteYAlojamiento(int(id_tiquete), 1)

            except ExcepcionIdTiquete as awa:
                messagebox.showwarning(title="Advertencia",message= awa.mensaje_error_inicio)
                self.agregarAlojamientoTiquete()
                return

            except ExcepcionAgregarAlojamiento as uwu:
                messagebox.showwarning(title ="Advertencia",message = uwu.mensaje_error_inicio)
                self.agregarAlojamientoTiquete()
                return

            lista_alojamientos= Alojamiento.buscarAlojamientoPorUbicacion(tiquete_solicitado.getVuelo().getDestino())
            if len(lista_alojamientos) == 0:
                mensaje = messagebox.showinfo(title = "Agregar alojamiento",message = "No hay alojamientos en ese destino.")
                return

            # Se llama a la funcion cuando se selecciona un alojamiento de la lista de alojamientos, se verifica que esta disponible
            # y posteriormente se pregunta por los días de estadía, para terminar imprimiendo por pantalla el tiquete
            def alojamientoSeleccionado(nombre):
                self.label_descripcion.config(text = "Ingrese los dias que se va a quedar en el alojamiento seleccionado")

                self.ventana_operaciones.pack_forget()
                alojamiento_solicitado=Admin.solicitarAlojamiento(tiquete_solicitado,nombre)
                if alojamiento_solicitado == None:
                    mensaje = messagebox.showinfo(title = "Agregar alojamiento", message = "Ese alojamiento no está disponible")
                    return

                # Es llamada cuando se ingresan los dias de estadia, se encarga de añadir el alojamiento al tiquete
                # con la clase auxiliar, y por ultimo imprime un resumen de la compra sumandole el precio del alojamiento
                def diasDeEstadia():
                    self.label_descripcion.config(text = "Gracias por su compra! Este es su tiquete:")
                    self.ventana_operaciones.pack_forget()

                    try:
                        hay_excepcion =self.ventana_operaciones.aceptar()
                    except ExcepcionEnteroString as owo:
                        messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                        alojamientoSeleccionado(nombre)
                        return
                    except ExcepcionEnteroFloat as owo:
                        messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                        alojamientoSeleccionado(nombre)
                        return

                    if hay_excepcion:
                        alojamientoSeleccionado(nombre)
                        return

                    Admin.agregarAlojamiento(tiquete_solicitado,alojamiento_solicitado,self.ventana_operaciones.valor_entradas[0])
                    self.ventana_operaciones = Label(self.frame)
                    self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=X)
                    self.ventana_operaciones.config(text=tiquete_solicitado.__str__())

                self.ventana_operaciones.pack_forget()
                self.ventana_operaciones = FieldFrame(self.frame,"Requisito",["Dias de estadia"],"valor",["1"],None,["int"])
                self.ventana_operaciones.botonAceptar.config(command=diasDeEstadia)

            # tabla de alojamientos disponibles en el lugar de destino, de donde se puede seleccionar un alojamiento
            label= Label(self.ventana_operaciones)
            label.pack()
            label["text"]+="\n"+ "-------------------------------------------------------------"
            label["text"]+="\n"+"{0:>10} {1:>15} {2:>18} {3:>12}".format("NOMBRE", "LOCACION", "PRECIO POR DIA", "ESTRELLAS")
            label["text"]+="\n"+"-------------------------------------------------------------"

            j = 0
            while j < len(lista_alojamientos):
                label_repetido =Label(self.ventana_operaciones)
                label_repetido.pack()
                label_repetido["text"]+="{0:>13} {1:>11} {2:>16} {3:>11}".format(lista_alojamientos[j].getNombre(), lista_alojamientos[j].getLocacion(), lista_alojamientos[j].getPrecio_dia(), lista_alojamientos[j].getEstrellas())
                label_repetido.bind("<ButtonPress-1>",lambda event,a=lista_alojamientos[j].getNombre():alojamientoSeleccionado(a))
                j += 1

            label_repetido["text"]+="\n"+"-------------------------------------------------------------"
            label_repetido["text"]+="\n"
            return

        formulario.botonAceptar.config(command=eventoAgregarAlojamiento)

    #--------------------------------------------------------------------------------------------------------------------------------------
    # Permite modificar el alojamiento y la silla de un tiquete, solicitando un ID de tiquete y verificando que existe, posteriormente se
    # pregunta si se desea cambiar la silla o el alojamiento, y segun lo que escoja, se ejecutan los métodos internos modificarSilla o
    # modificarAlojamiento

    def modificarTiquete(self):
        self.label_proceso.config(text = "Modificar Tiquete")
        self.label_descripcion.config(text = "Puede modificar los atributos Silla y Alojamiento (si ya tiene uno) de un tiquete comprado previamente")
        self.ventana_operaciones.pack_forget()
        self.ventana_operaciones = Frame(self.frame)
        self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2,fill=X)

        #Funcion que se dispara al darle en el boton aceptar del formulario que pregunta por el ID del tiquete. Se busca el tiquete para verificar
        # su existencia, y se despliegan dos botones que permiten elegir si se quiere modificar la silla o el alojamiento del tiquete

        def editarTiquete():

            try:
                hay_excepcion = formulario.aceptar()
            except ExcepcionEnteroString as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.modificarTiquete()
                return
            except ExcepcionEnteroFloat as owo:
                messagebox.showerror(title="Error",message=owo.mensaje_error_inicio)
                self.modificarTiquete()
                return

            if hay_excepcion:
                self.modificarTiquete()
                return

            try:
                tiquete = Aerolinea.BuscarTiquete(int(formulario.valor_entradas[0]))
            except ExcepcionIdTiquete as awa:
                messagebox.showwarning(title="Advertencia",message= awa.mensaje_error_inicio)
                self.modificarTiquete()
                return

            self.ventana_operaciones.pack_forget()
            self.ventana_operaciones = Frame(self.frame,relief="ridge",bd=2)
            self.ventana_operaciones.pack(ipadx = 2, ipady =2, padx = 2, pady= 2)
            label = Label(self.ventana_operaciones,text="Que opcion desea modificar de su tiquete",font = ("Segoe UI", 10))
            label.grid(row =0,column=0 ,columnspan=2,ipadx=10,ipady=10)
            boton_modificar_alojamiento = Button(self.ventana_operaciones,text = "Modificar alojamiento",font=("Segoe UI", 10),command=lambda:modificarAlojamiento(tiquete))
            boton_modificar_alojamiento.grid(row=1,column=0,padx=2,ipadx=5)
            boton_modificar_silla = Button(self.ventana_operaciones,text = "Modificar silla",font = ("Segoe UI", 10),command=lambda:self.modificarSilla(2,tiquete))
            boton_modificar_silla.grid(row=1,column=1,padx=2,ipadx=5)

        # Se llama cuando se elige modificarAlojamiento en el Frame anterior, luego de esto se siguen pasos similares a los expuestos en
        # agregar alojamiento para modificar el alojamiento que se tenia previamente.

        def modificarAlojamiento(tiquete):
            self.label_proceso.config(text = "Modificar alojamiento")
            self.label_descripcion.config(text = "Cambie el alojamiento que agrego a su tiquete de compra, seleccionando uno nuevo de la lista")

            self.ventana_operaciones.pack_forget()
            self.ventana_operaciones = Frame(self.frame)
            self.ventana_operaciones.pack()

            try:
                tiquete_solicitado = Admin.buscarTiqueteYAlojamiento(int(tiquete.getId()),2)

            except ExcepcionModificarAlojamiento as uwu:
                messagebox.showwarning(title ="Advertencia",message = uwu.mensaje_error_inicio)
                self.modificarTiquete()
                return

            lista_alojamientos= Alojamiento.buscarAlojamientoPorUbicacion(tiquete_solicitado.getVuelo().getDestino())
            if len(lista_alojamientos) == 0:
                mensaje = messagebox.showinfo(title = "Modificar alojamiento",message = "No hay alojamientos en ese destino.")
                return

            # Se llama a la funcion cuando se selecciona un alojamiento de la lista de alojamientos, se verifica que esta disponible
            # y posteriormente se pregunta por los días de estadía, para terminar imprimiendo por pantalla el tiquete

            def alojamientoSeleccionado(nombre):
                self.label_descripcion.config(text = "Ingrese los dias que se va a quedar en el alojamiento seleccionado")
