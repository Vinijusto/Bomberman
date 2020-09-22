class Estallido:
    def __init__(self,coord):
        self.posicion = coord
        self.id_casilla = [(self.posicion[0] - 10) // 80,(self.posicion[1] - 10) // 80]
        self.longitud_de_fueguito_valyrio = 80
        self.posicion = [self.posicion[0] - 20, self.posicion[1] - 20]
    
    # Se calcula si un personaje esta dentro del estallido
    def comparacion(self,coords):
        self.comparacion_de_coords = 1 * (coords[0] >= self.posicion[0]) * (coords[0] <= self.posicion[0] + self.longitud_de_fueguito_valyrio) * (coords[1] >= self.posicion[1]) * (coords[1] <= self.posicion[1] + self.longitud_de_fueguito_valyrio)
        return self.comparacion_de_coords

    # Metodos que sirven para devolverle al mapa informacion del objeto
    def set_coords(self):
        return self.posicion
    
    def get_id_casilla(self):
        return self.id_casilla