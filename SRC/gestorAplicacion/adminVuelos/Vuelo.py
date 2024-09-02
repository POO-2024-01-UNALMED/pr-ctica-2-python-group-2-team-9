class Vuelo:
    def __init__(self, ID, precio, origen, destino, aeronave, distancia_en_km, fecha_de_salida, hora_de_salida):
        self.ID = ID
        self.precio = precio
        self.origen = origen
        self.destino = destino
        self.aeronave = aeronave
        self.distancia_en_km = distancia_en_km
        self.fecha_de_salida = fecha_de_salida
        self.hora_de_salida = hora_de_salida
        self.esta_completo = False
        self.tiquetes = []  # Lista de tiquetes
    
        self.aeronave.get_aerolinea().agregar_vuelo(self)

    def buscar_tiquete_por_id(self, tiquetes, ID):
        for tiquete in tiquetes:
            if tiquete.get_id() == ID:
                return tiquete
        return None

    # Getters y Setters
    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
        self.ID = ID

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_origen(self):
        return self.origen

    def set_origen(self, origen):
        self.origen = origen

    def get_destino(self):
        return self.destino

    def set_destino(self, destino):
        self.destino = destino

    def get_aeronave(self):
        return self.aeronave

    def set_aeronave(self, aeronave):
        self.aeronave = aeronave

    def get_distancia_en_km(self):
        return self.distancia_en_km

    def set_distancia_en_km(self, distancia_en_km):
        self.distancia_en_km = distancia_en_km


    def get_fecha_de_salida(self):
        return self.fecha_de_salida

    def set_fecha_de_salida(self, fecha_de_salida):
        self.fecha_de_salida = fecha_de_salida

    def get_tiquetes(self):
        return self.tiquetes

    def set_tiquetes(self, tiquetes):
        self.tiquetes = tiquetes

    def get_hora_de_salida(self):
        return self.hora_de_salida

    def set_hora_de_salida(self, hora_de_salida):
        self.hora_de_salida = hora_de_salida

    def is_esta_completo(self):
        return self.esta_completo

    def set_esta_completo(self, esta_completo):
        self.esta_completo = esta_completo
