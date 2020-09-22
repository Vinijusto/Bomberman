import random
class WhiteWalker:
    def __init__(self,id_casilla,mapa):
        self.mapa = mapa # Defino al mapa ya que estos dos objetos están estrechamente vinculados
        self.casilla = id_casilla # Posicòn del objeto
        self.posicion = [self.casilla[0] * 80 + 10,self.casilla[1] * 80 + 10] # La casilla en donde esta el arista  superior izquierdo
        self.medidas = 65 # Medidas de JS, no hace falta declarar más por que es un cuadrado
        self.x = self.posicion[0]
        self.y = self.posicion[1]
        # Defino las posciones de todas las aristas del cuadrado que encapsula al bm, que se usaran para consultar el estado del objeto
        self.vertice_1 = self.posicion
        self.vertice_2 = [self.posicion[0] + self.medidas, self.posicion[1]]
        self.vertice_3 = [self.posicion[0], self.posicion[1] + self.medidas]
        self.vertice_4 = [self.posicion[0] + self.medidas, self.posicion[1] + self.medidas]
        self.nueva_posicion_posible_parte_inferior = [0,0]
        self.nueva_posicion_posible_parte_superior = [0,0]
        self.velocidad = 5 # Cuantos píxeles aumenta la x y la y del bm al moverse
        self.posibilidades_de_movimiento = [self.mover_bm_abajo, self.mover_bm_arriba, self.mover_bm_derecha, self.mover_bm_izquierda]
        self.mover_aleatoriamente()

    def mover_aleatoriamente(self):
        """Se randomiza un numero (se usa para definir a que elemnto llamar de la lista 'posibilidades_de_movimiento')"""
        self.randomizador = random.randint(0,4)

    def mover_rectilineamente(self):
        """Se mueve el Whitewalker en base al resultado del numero aleatorio"""
        if self.randomizador < 4:
            self.posibilidades_de_movimiento[self.randomizador]()

    def mover_bm_derecha(self):
        """El WhiteWalker en base a los resultados que le pidio al mapa se mueve o no a la derecha"""
        self.nueva_posicion_posible_parte_superior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0] + 1,
                                                                                                self.casilla[1]],
                                                                                                [self.vertice_2[0] + self.velocidad ,
                                                                                                self.vertice_2[1]],
                                                                                                [self.vertice_1[0] + 5, self.vertice_1[1]])
        self.nueva_posicion_posible_parte_inferior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0] + 1,
                                                                                                self.casilla[1] + 1],
                                                                                                [self.vertice_4[0] + self.velocidad,
                                                                                                self.vertice_4[1]],
                                                                                                self.vertice_1)
        if self.nueva_posicion_posible_parte_superior[0] != 1 and self.nueva_posicion_posible_parte_inferior[0] != 1:
            self.x += self.velocidad * (self.x <= 655)
        self.posicion = [self.x,self.posicion[1]]
        self.casilla = [self.casilla[0] + self.nueva_posicion_posible_parte_superior[1], self.casilla[1]]
        self.redefinir_vertices()
        
    def mover_bm_abajo(self):
        """El WhiteWalker en base a los resultados que le pidio al mapa se mueve o no hacia abajo"""
        self.nueva_posicion_posible_parte_superior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0],
                                                                                                self.casilla[1] + 1],
                                                                                                [self.vertice_3[0], self.vertice_3[1] + self.velocidad],
                                                                                                [self.vertice_1[0], self.vertice_1[1]+ 5])
        self.nueva_posicion_posible_parte_inferior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0] + 1,
                                                                                                self.casilla[1] + 1],
                                                                                                [self.vertice_4[0],self.vertice_4[1]  + self.velocidad],
                                                                                                self.vertice_1)
        if self.nueva_posicion_posible_parte_superior[0] != 1 and self.nueva_posicion_posible_parte_inferior[0] != 1:
            self.y += self.velocidad * (self.y <= 655)
        self.posicion = [self.posicion[0],self.y]
        self.casilla = [self.casilla[0], self.casilla[1] + self.nueva_posicion_posible_parte_superior[1]]
        self.redefinir_vertices()

    def mover_bm_izquierda(self):
        """El WhiteWalker en base a los resultados que le pidio al mapa se mueve o no a la izquierda"""
        self.nueva_posicion_posible_parte_superior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0] - 1,
                                                                                                      self.casilla[1]],
                                                                                                [self.vertice_1[0] - self.velocidad,self.vertice_1[1]], 
                                                                                                [self.vertice_1[0] - 5 - 5, self.vertice_1[1]])
        self.nueva_posicion_posible_parte_inferior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0] - 1,
                                                                                                        self.casilla[1] + 1],
                                                                                                [self.vertice_3[0] - self.velocidad,self.vertice_3[1]],
                                                                                                [self.vertice_3[0] - 5,self.vertice_3[1]])    
        if self.nueva_posicion_posible_parte_superior[0] != 1 and self.nueva_posicion_posible_parte_inferior[0] != 1:
            self.x -= self.velocidad * (self.x >= 15)
        self.posicion = [self.x,self.posicion[1]]
        self.casilla = [self.casilla[0] - self.nueva_posicion_posible_parte_superior[1] *(self.nueva_posicion_posible_parte_inferior[0] != 1) * (self.nueva_posicion_posible_parte_superior[0] != 1), self.casilla[1]]
        self.redefinir_vertices()

    def mover_bm_arriba(self): 
        """El WhiteWalker en base a los resultados que le pidio al mapa se mueve o no hacia arriba"""
        self.nueva_posicion_posible_parte_superior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0],
                                                                                                      self.casilla[1] - 1],
                                                                                                      [self.vertice_1[0] ,self.vertice_1[1] - self.velocidad],
                                                                                                      [self.vertice_1[0], self.vertice_1[1] - 5 -5])
        self.nueva_posicion_posible_parte_inferior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0] + 1,
                                                                                                              self.casilla[1] - 1],
                                                                                                              [self.vertice_2[0] ,self.vertice_2[1] - self.velocidad],
                                                                                                              [self.vertice_1[0],self.vertice_1[1]])
        self.y -= self.velocidad * (self.y >= 15) *(self.nueva_posicion_posible_parte_inferior[0] != 1) * (self.nueva_posicion_posible_parte_superior[0] != 1)
        self.posicion = [self.posicion[0],self.y]
        self.casilla = [self.casilla[0],self.casilla[1] - self.nueva_posicion_posible_parte_superior[1] * (self.nueva_posicion_posible_parte_inferior[0] != 1) * (self.nueva_posicion_posible_parte_superior[0] != 1)]
        self.redefinir_vertices()

    def redefinir_vertices(self):
        """Se redefinen los vertices de los WhiteWalkers"""
        self.nueva_posicion_posible_parte_inferior = [0,0]
        self.nueva_posicion_posible_parte_superior = [0,0]
        self.vertice_1 = self.posicion
        self.vertice_2 = [self.posicion[0] + self.medidas, self.posicion[1]]
        self.vertice_3 = [self.posicion[0], self.posicion[1] + self.medidas]
        self.vertice_4 = [self.posicion[0] + self.medidas, self.posicion[1] + self.medidas]

    # Metodos que sirven para devolverle al mapa informacion del objeto
    def get_posicion(self):
        """Se devuelve la posicion del objeto"""
        return self.posicion

    def get_id_casilla(self):
        """Se devuelve el id casilla del objeto"""
        return self.casilla
        
    def desaparecer(self,identificador_de_lista):
        """Le dice al mapa (donde fue instanciado) que lo elimine de la lista de objetos de tipo WhiteWalker"""
        self.mapa.delet_bomberman(identificador_de_lista)