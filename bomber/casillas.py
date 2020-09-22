import random
class Casilla:
    def __init__(self,id_casilla,vertices,estado,nivel):
        self.id_casilla = id_casilla
        self.con_fuego = False
        self.vertices = vertices
        self.nivel = nivel
        self.movimiento = False
        self.longitud_de_lado = 75
        self.longitud_de_lado2= 70
        self.casilla_con_pared_rompible = False
        self.ocupado = False
        self.casilla_con_pared_no_rompible = False
        for pos,index in enumerate(estado):
            estad = (index[0],index[1])
            if self.id_casilla == estad:
                self.ocupado = True
                self.casilla_con_pared_no_rompible = True
        self.numeroazar = random.randint(0,self.nivel) # Aca se define si la casilla va a ser con una pared rompible o no
        if self.id_casilla != (0,0) and self.id_casilla != (0,1) and self.id_casilla != (0,2) and self.id_casilla != (0,3) and self.id_casilla != (0,4): # Este if es para que haya un spawn sin bloques
            if self.ocupado == False and self.numeroazar == 0:
                self.casilla_con_pared_rompible = True
                self.ocupado = True

    def calcular_si_se_puede_mover(self,arista,pixel):# Hago un calculo que defina la posicion de los vertices y en base a eso responder
        self.movimiento = 1 * (arista[0] >= self.vertices[0]) * (arista[0] <= self.vertices[0] + self.longitud_de_lado) * (arista[1] >= self.vertices[1]) * (arista[1] <= self.vertices[1] + self.longitud_de_lado) * (self.ocupado == True) 
        self.aumento_de_casilla = 1 * (pixel[0] >= self.vertices[0]) * (pixel[0] <= self.vertices[0] + self.longitud_de_lado2) * (pixel[1] >= self.vertices[1]) * (pixel[1] <= self.vertices[1] + self.longitud_de_lado2) 
        return [self.movimiento,self.aumento_de_casilla]
    
    # Devuelve todos los atributos que necesite el mapa para que funcione el juego
    def devolver_estado_de_casilla(self):
        return self.ocupado

    def get_id_casilla(self):
        return self.id_casilla 

    def get_vertices(self):
        return self.vertices
    
    def get_con_fuego(self):
        return self.con_fuego

    def get_id_casilla_si_esta_con_una_pared_rompible(self):
        if self.casilla_con_pared_rompible == True:
            return self.vertices

    def get_id_casilla_si_esta_ocupada(self):
        if self.ocupado == False:
            return self.id_casilla

    def get_id_casilla_si_esta_desocupada(self):
        if self.casilla_con_pared_rompible == True:
            return self.id_casilla

    def transformar_a_casilla_atravesable(self):
        if self.casilla_con_pared_rompible == True  and self.casilla_con_pared_no_rompible == False:
            self.casilla_con_pared_rompible == False
            self.ocupado = False

    def transformar_a_casilla_con_fuego(self):
        if self.ocupado == False:
            self.con_fuego = True
    
    def transformar_a_casilla_sin_fuego(self):
        if self.con_fuego == True:
            self.con_fuego = False