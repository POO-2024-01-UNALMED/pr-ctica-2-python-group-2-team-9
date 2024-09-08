#Corran esta clase 

from tkinter import *
from Admin import Admin

class ventana_inicio(Tk):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        # CONFIGURACION PARAMETROS PRINCIPALES DE LA VENTANA
        self.geometry("800x500")
        self.title("Inicio")
        self.option_add("*tearOff", False)
        self.resizable(0,0)

        # CONFIGURACION VR--TEXTO HDV DESARROLLADORES
        self.varHDV = StringVar()
        self.varHDV.set("Desarrolladores")
        self.hola =StringVar()
        self.hola.set('')

        # CONFIGURACION ZONA DE MENU
        self.menubar = Menu(self)
        self.menuInicio = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menuInicio, label="Inicio")
        self.menuInicio.add_command(label="Descripcion",command=self.desno)
        self.menuInicio.add_command(label="Salir",command=self.salir)
        self["menu"] = self.menubar

        #CONFIGURACION ZONA FRAMES
        self.P1 = Frame(self, width=400, height=500, bg="Gray95")
        self.P1.pack(side=LEFT)
        self.P3 = Frame(self.P1, width=400, height=150)
        self.P3.grid(row=0, column=0)
        self.saludo = Label(self.P3, text="Bienvenido al sistema de reservas de vuelo\n""Haz click en la imagen para empezar\n", font=("Segoe UI", 12))
        self.P4 = Frame(self.P1, width=400, height=350, bg="black")
        self.P4.grid(row=1, column=0)
        self.contenedorImagen = Label(self.P4)
        self.P2 = Frame(self, width=400, height=500, bg="yellow")
        self.P2.pack(side=RIGHT)
        self.P5 = Frame(self.P2, width=400, height=150, bg="Gray")
        self.P5.grid(row=0, column=0)
        self.textoHDV = Label(self.P5, textvariable=self.varHDV, font = ("Segoe UI", 8))
        self.textoHDV.place(x=200, y=75, anchor="center")
        self.P6 = Frame(self.P2, width=400, height=350, bg="Gray")
        self.P6.grid(row = 1, column = 0)
        self.saludo.place(x=200, y=75, anchor="center")
        self.W1 = Frame(self.P6, width=200, height=170, bg="Blue")
        self.W1.place(x=0, y=0)
        self.W2 = Frame(self.P6, width=200, height=170, bg="White")
        self.W2.place(x=200, y=0)
        self.W3 = Frame(self.P6, width=200, height=180, bg="Green")
        self.W3.place(x=0, y=170)
        self.W4 = Frame(self.P6, width=200, height=180, bg="Red")
        self.W4.place(x=200, y=170)
        self.holla = Label(self.P3, textvariable=self.hola, font=("Segoe UI", 8))
        self.holla.place(x=200, y=120, anchor="center")

    #GENERA LA SALIDA DEL TEXTO DE EN LA DESCRIPCION
    def desno(self):
        self.hola.set("Permite la compra de un tiquete para un vuelo, con seleccion de\n" "silla y alojamiento, ademas de la ejecucion de opciones de administrador ✈")

    #GENERA LA SALIDA DE LA VENTANA DE INICIO DANDO CULMINADO EL FUNCIONAMIENTO DE LA APLICACION
    def salir(self):
        Admin.salirDelSistema()
        return super().destroy()

if __name__ == "__main__":
    ventana_inicios = ventana_inicio()
    ventana_inicios.mainloop()