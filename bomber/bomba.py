import time
class Bomba:
    def __init__(self,id_casilla,mapa):
        self.mapa = mapa
        self.longitud_lado = 80
        self.id_casilla = id_casilla
        self.pixeles_muros = 10
        self.posicion = (self.id_casilla[0] * self.longitud_lado + self.pixeles_muros,self.id_casilla[1] * self.longitud_lado + self.pixeles_muros)

    def estallar(self):
        """Se le ordena al mapa que se instancie el estallido y se eliminan las casilla rompibles"""
        self.mapa.crear_el_mismisimo_fuego_valiryo_proveniente_del_temible_Dragon_Drogo(self.posicion)
        # Con los segundos ifs se logra que la llama se expanda depeniendo del entorno del mapa
        self.fuego_a_la_derecha = self.mapa.eliminar_paredes_rompibles_cercanas([self.id_casilla[0] + 1,self.id_casilla[1]])
        if self.fuego_a_la_derecha == None:
            self.mapa.crear_el_mismisimo_fuego_valiryo_proveniente_del_temible_Dragon_Drogo([self.posicion[0] + self.longitud_lado, self.posicion[1]])
            self.fuego_mas_a_la_derecha = self.mapa.eliminar_paredes_rompibles_cercanas([self.id_casilla[0] + 2,self.id_casilla[1]])
            if self.fuego_mas_a_la_derecha == None:
                self.mapa.crear_el_mismisimo_fuego_valiryo_proveniente_del_temible_Dragon_Drogo([self.posicion[0] + self.longitud_lado + self.longitud_lado, self.posicion[1]])
        
        self.fuego_a_la_izquierda = self.mapa.eliminar_paredes_rompibles_cercanas([self.id_casilla[0] - 1,self.id_casilla[1]])
        if self.fuego_a_la_izquierda == None:
            self.mapa.crear_el_mismisimo_fuego_valiryo_proveniente_del_temible_Dragon_Drogo([self.posicion[0] - self.longitud_lado, self.posicion[1]])
            self.fuego_mas_a_la_izquierda = self.mapa.eliminar_paredes_rompibles_cercanas([self.id_casilla[0] - 2,self.id_casilla[1]])
            if self.fuego_mas_a_la_izquierda == None:
                self.mapa.crear_el_mismisimo_fuego_valiryo_proveniente_del_temible_Dragon_Drogo([self.posicion[0] - self.longitud_lado - self.longitud_lado, self.posicion[1]])
        
        self.fuego_a_la_abajo = self.mapa.eliminar_paredes_rompibles_cercanas([self.id_casilla[0],self.id_casilla[1] + 1])
        if self.fuego_a_la_abajo == None:
            self.mapa.crear_el_mismisimo_fuego_valiryo_proveniente_del_temible_Dragon_Drogo([self.posicion[0], self.posicion[1] + self.longitud_lado])
            self.fuego_mas_a_la_abajo = self.mapa.eliminar_paredes_rompibles_cercanas([self.id_casilla[0], self.id_casilla[1] + 2])
            if self.fuego_mas_a_la_abajo == None:
                self.mapa.crear_el_mismisimo_fuego_valiryo_proveniente_del_temible_Dragon_Drogo([self.posicion[0], self.posicion[1] + self.longitud_lado + self.longitud_lado])     
        
        self.fuego_a_la_arriba = self.mapa.eliminar_paredes_rompibles_cercanas([self.id_casilla[0],self.id_casilla[1] - 1])
        if self.fuego_a_la_arriba == None:
            self.mapa.crear_el_mismisimo_fuego_valiryo_proveniente_del_temible_Dragon_Drogo([self.posicion[0], self.posicion[1] - self.longitud_lado])
            self.fuego_mas_a_la_arriba = self.mapa.eliminar_paredes_rompibles_cercanas([self.id_casilla[0],self.id_casilla[1] - 2])
            if self.fuego_mas_a_la_arriba == None:
                self.mapa.crear_el_mismisimo_fuego_valiryo_proveniente_del_temible_Dragon_Drogo([self.posicion[0] , self.posicion[1] - self.longitud_lado - self.longitud_lado])
        
    # Metodos que sirven para devolverle al mapa informacion del objeto
    def set_coords(self):
        """Se devuelve la posicion"""
        return self.posicion

    def set_id_casilla(self):
        """Se devuelve el id casilla"""
        return self.id_casilla