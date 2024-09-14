# AUTORES: RICARDO FUENTES, VALERY FERNANDEZ, JUAN LUIS SUCERQUIA, MARIANA SANCHEZ

class ErrorAplicacion(Exception):

    def __init__(self,mensaje):
        self.mensaje_error_inicio = "Manejo de errores de la aplicacion:" + mensaje
        super().__init__(self.mensaje_error_inicio)