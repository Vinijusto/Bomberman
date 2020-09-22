class Parednorompible:
    def __init__(self,pos):
        self.posicion = pos
        self.id_casilla = [(self.posicion[0] - 10) // 80,(self.posicion[1] - 10) // 80]
    
    def set_coords(self):
        return self.posicion

    def set_estado_de_algunas_casillas(self):
        return self.id_casilla