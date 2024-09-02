class Aeronave:
    # ATRIBUTOS
    GASTO_GASOLINA = 120

    def __init__(self, nombre, aerolinea):
        self._nombre = nombre
        self._aerolinea = aerolinea
        self._descompuesto = False
        self._SILLAS_ECONOMICAS = []
        self._SILLAS_EJECUTIVAS = []

    # GETTERS Y SETTERS
    def get_aerolinea(self):
        return self._aerolinea

    def set_aerolinea(self, aerolinea):
        self._aerolinea = aerolinea

    def get_sillas_economicas(self):
        return self._SILLAS_ECONOMICAS

    def set_sillas_economicas(self, sillas_economicas):
        self._SILLAS_ECONOMICAS = sillas_economicas

    def get_sillas_ejecutivas(self):
        return self._SILLAS_EJECUTIVAS

    def set_sillas_ejecutivas(self, sillas_ejecutivas):
        self._SILLAS_EJECUTIVAS = sillas_ejecutivas

    def get_gasto_gasolina(self):
        return self.GASTO_GASOLINA

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def is_descompuesto(self):
        return self._descompuesto

    def set_descompuesto(self, descompuesto):
        self._descompuesto = descompuesto

    def __str__(self):
        return self._nombre

    # MÉTODOS
    def buscar_silla_por_ubicacion_y_tipo(self, ubicacion, tipo):
        if tipo.lower() == "economica":
            for silla in self._SILLAS_ECONOMICAS:
                if silla.is_estado() and silla.get_ubicacion() == ubicacion:
                    return silla
        elif tipo.lower() == "ejecutiva":
            for silla in self._SILLAS_EJECUTIVAS:
                if silla.is_estado() and silla.get_ubicacion() == ubicacion:
                    return silla
        return None

    def calcular_sillas_ocupadas(self):
        cont = 0
        for silla in self._SILLAS_ECONOMICAS:
            if silla.is_estado():
                cont += 1
        for silla in self._SILLAS_EJECUTIVAS:
            if silla.is_estado():
                cont += 1
        return f"Esta es la cantidad de sillas ocupadas: {cont}"

    # MÉTODO ABSTRACTO
    def calcular_consumo_gasolina(self, distancia_en_km):
        {}

