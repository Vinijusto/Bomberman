class Model:
    def __init__(self,controlador,mapa):
        self.controlador = controlador
        self.mapa = mapa

    def estadisticas_bm(self):
        self.pos_bm = self.mapa.estadisticas_bm()
        return self.pos_bm
    
    def get_posiciones_paredes_no_rompibles(self):
        self.posiciones_de_paredes_no_rompibles = self.mapa.posicion_de_paredes_no_rompibles()
        return self.posiciones_de_paredes_no_rompibles

    def posicion_de_bombas(self):
        self.pos_bombas = self.mapa.posicion_de_bombas()
        return self.pos_bombas

    def posicion_de_paredes_rompibles(self):
        self.pos_paredes_rompibles = self.mapa.posicion_de_paredes_rompibles()
        return self.pos_paredes_rompibles

    def posicion_de_estallidos(self):
        self.pos_estallidos = self.mapa.posicion_de_estallidos()
        return self.pos_estallidos

    def posicion_de_ww(self):
        self.pos_ww = self.mapa.posicion_de_ww()
        return self.pos_ww

    def posicion_de_portal(self):
        self.pos_de_portal = self.mapa.posicion_de_portal()
        return self.pos_de_portal
