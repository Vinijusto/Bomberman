class Paredrompible:
    def __init__(self,id_casilla):
        self.id_casilla = id_casilla
        self.posicion = (self.id_casilla[0] * 80 + 10,self.id_casilla[1] * 80 + 10)

    # Metodos que sirven para devolverle al mapa informacion del objeto
    def set_coords(self):
        return self.posicion

    def set_estado_de_algunas_casillas(self):
        return self.id_casilla