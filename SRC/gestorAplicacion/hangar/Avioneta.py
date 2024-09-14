# AUTORES: RICARDO FUENTES, VALERY FERNANDEZ, JUAN LUIS SUCERQUIA, MARIANA SANCHEZ
class Avioneta:
    NUM_SILLAS_ECONOMICAS = 6
    NUM_SILLAS_EJECUTIVAS = 4

    def __init__(self, nombre, aerolinea):
        self.nombre = nombre
        self.aerolinea = aerolinea
        self.sillas_economicas = [None] * self.NUM_SILLAS_ECONOMICAS
        self.sillas_ejecutivas = [None] * self.NUM_SILLAS_EJECUTIVAS

        for num_posicion in range(self.NUM_SILLAS_EJECUTIVAS):
            if num_posicion % 4 == 0 or num_posicion % 4 == 3:
                ubicacion = "VENTANA"
            else:
                ubicacion = "PASILLO"

            self.sillas_ejecutivas[num_posicion] = Silla("EJECUTIVA", num_posicion, ubicacion)

        for num_posicion in range(self.NUM_SILLAS_ECONOMICAS):
            if num_posicion % 6 == 0 or num_posicion % 6 == 5:
                ubicacion = "VENTANA"
            elif num_posicion % 6 == 1 or num_posicion % 6 == 4:
                ubicacion = "CENTRAL"
            else:
                ubicacion = "PASILLO"

            self.sillas_economicas[num_posicion] = Silla("ECONOMICA", num_posicion, ubicacion)

    @staticmethod
    def get_num_sillas_economicas():
        return Avioneta.NUM_SILLAS_ECONOMICAS

    @staticmethod
    def get_num_sillas_ejecutivas():
        return Avioneta.NUM_SILLAS_EJECUTIVAS

    def calcular_sillas_ocupadas(self):
        cont = 0
        for silla in self.sillas_economicas:
            if silla.is_estado():
                cont += 1
        for silla in self.sillas_ejecutivas:
            if silla.is_estado():
                cont += 1
        return f"Sillas ocupadas en la avioneta: {cont}"

    def calcular_consumo_gasolina(self, distancia_en_km):
        consumido = self.get_gasto_gasolina() * distancia_en_km
        return consumido
