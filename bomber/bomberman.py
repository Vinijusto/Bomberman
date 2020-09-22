class JonSnow:
    def __init__(self,mapa,controlador):
        self.controlador = controlador
        self.advertencia_al_jugador = print('JonSnow tiene una zona segura, el spawn, donde nunca podra morir')
        self.mapa = mapa # Defino al mapa ya que estos dos objetos están estrechamente vinculados
        self.casilla = [0,0] # La casilla en donde esta el vertices  superior izquierdo
        self.posicion = [15,15] # Posicòn del objeto
        self.vidas = 3 # La cantidad de oportunidades que tiene el bomerman
        self.medidas = 40 # Medidas de JS, no hace falta declarar más por que es un cuadrado
        self.x = 10 
        self.y = 10
        # Defino las posciones de todas las vertices del cuadrado que encapsula al bm, que se usaran para consultar el estado del objeto
        self.vertices_1 = self.posicion
        self.vertices_2 = [self.posicion[0] + self.medidas, self.posicion[1]]
        self.vertices_3 = [self.posicion[0], self.posicion[1] + self.medidas]
        self.vertices_4 = [self.posicion[0] + self.medidas, self.posicion[1] + self.medidas]
        self.nueva_posicion_posible_parte_inferior = [0,0]
        self.nueva_posicion_posible_parte_superior = [0,0] 
        self.velocidad = 5 # Cuantos píxeles aumenta la x y la y del bm al moverse

    def mover_bm_derecha(self):
        """ Desplaza dependiendo (o no) al bomberman dependiendo del mapa, a la derecha"""
        # Le ordeno al mapa que le pregunta a la respectivas casillas subsecunetes si el objeto, en este caso bomberman,
        # si se puede mover. Cabe destecar que no se le pasa la coordenada exacta si no la que se tienta
        self.nueva_posicion_posible_parte_superior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0] + 1,
                                                                                                self.casilla[1]],
                                                                                                [self.vertices_2[0] + self.velocidad ,
                                                                                                self.vertices_2[1]],
                                                                                                [self.vertices_1[0] +  self.velocidad, self.vertices_1[1]])
        self.nueva_posicion_posible_parte_inferior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0] + 1,
                                                                                                self.casilla[1] + 1],
                                                                                                [self.vertices_4[0] + self.velocidad,
                                                                                                self.vertices_4[1]],
                                                                                                self.vertices_1)
        # Se aumenta la medida respectiva al movimiento, en este caso horizontal (x), con la condicion que las casillas le 
        # hayan respondido si (0) y que la posicion sea menor al limite que el bm pueda explorar
        if self.nueva_posicion_posible_parte_superior[0] != 1 and self.nueva_posicion_posible_parte_inferior[0] != 1:
            self.x += self.velocidad * (self.x <= 680)
        #print(self.nueva_posicion_posible_parte_superior)                 
        # Se redefine donde está, se haya movido o no
        self.posicion = [self.x,self.posicion[1]]
        # self.casilla = [self.casilla[0] + (self.nueva_posicion_posible_parte_superior == 0),self.casilla[1]]
        #if self.nueva_posicion_posible_parte_superior != None and self.nueva_posicion_posible_parte_inferior != None:
        self.casilla = [self.casilla[0] + self.nueva_posicion_posible_parte_superior[1], self.casilla[1]]
        # Redefino las vertices debido al movimiento horizontal generado (el atributo self.medidas es la longitud del bomberman)
        self.redefinir_vertices()
        # Le devuelvo a mapa la posicion del bm
        return self.posicion
        
    def mover_bm_abajo(self):
        """ Desplaza dependiendo (o no) al bomberman dependiendo del mapa, a abajo"""
        self.nueva_posicion_posible_parte_superior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0],
                                                                                                self.casilla[1] + 1],
                                                                                                [self.vertices_3[0], self.vertices_3[1] + self.velocidad],
                                                                                                [self.vertices_1[0], self.vertices_1[1]+ 5])
        self.nueva_posicion_posible_parte_inferior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0] + 1,
                                                                                                self.casilla[1] + 1],
                                                                                                [self.vertices_4[0],self.vertices_4[1]  + self.velocidad],
                                                                                                self.vertices_1)
        if self.nueva_posicion_posible_parte_superior[0] != 1 and self.nueva_posicion_posible_parte_inferior[0] != 1:
            self.y += self.velocidad * (self.y <= 680)
        self.posicion = [self.posicion[0],self.y]
        self.casilla = [self.casilla[0], self.casilla[1] + self.nueva_posicion_posible_parte_superior[1]]
        self.redefinir_vertices()
        return self.posicion

    def mover_bm_izquierda(self):
        """ Desplaza dependiendo (o no) al bomberman dependiendo del mapa, a la izquierda"""
        self.nueva_posicion_posible_parte_superior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0] - 1,
                                                                                                self.casilla[1]],
                                                                                                [self.vertices_1[0] - self.velocidad,self.vertices_1[1]], 
                                                                                                [self.vertices_1[0] - 5 - 5, self.vertices_1[1]])
        self.nueva_posicion_posible_parte_inferior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0] - 1,
                                                                                                self.casilla[1] + 1],
                                                                                                [self.vertices_3[0] - self.velocidad,self.vertices_3[1]],
                                                                                                [self.vertices_3[0] - 5,self.vertices_3[1]])    
        if self.nueva_posicion_posible_parte_superior[0] != 1 and self.nueva_posicion_posible_parte_inferior[0] != 1:
            self.x -= self.velocidad * (self.x >= 15)
        self.posicion = [self.x,self.posicion[1]]
        self.casilla = [self.casilla[0] - self.nueva_posicion_posible_parte_superior[1] *(self.nueva_posicion_posible_parte_inferior[0] != 1) * (self.nueva_posicion_posible_parte_superior[0] != 1), self.casilla[1]]
        self.redefinir_vertices()
        return self.posicion

    def mover_bm_arriba(self): 
        """ Desplaza dependiendo (o no) al bomberman dependiendo del mapa, a arriba"""
        self.nueva_posicion_posible_parte_superior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0],
                                                                                                self.casilla[1] - 1],
                                                                                                [self.vertices_1[0] ,self.vertices_1[1] - self.velocidad],
                                                                                                [self.vertices_1[0], self.vertices_1[1] - 5 -5])
        self.nueva_posicion_posible_parte_inferior = self.mapa.consultar_casilla_por_movimiento([self.casilla[0] + 1,
                                                                                                self.casilla[1] - 1],
                                                                                                [self.vertices_2[0] ,self.vertices_2[1] - self.velocidad],
                                                                                                [self.vertices_1[0],self.vertices_1[1]])
        self.y -= self.velocidad * (self.y >= 15) *(self.nueva_posicion_posible_parte_inferior[0] != 1) * (self.nueva_posicion_posible_parte_superior[0] != 1)
        self.posicion = [self.posicion[0],self.y]
        self.casilla = [self.casilla[0],self.casilla[1] - self.nueva_posicion_posible_parte_superior[1] *(self.nueva_posicion_posible_parte_inferior[0] != 1) * (self.nueva_posicion_posible_parte_superior[0] != 1)]
        self.redefinir_vertices()
        return self.posicion

    def respawnear(self):
        """Envia al bomberman a la casilla de spawn"""
        self.casilla = [0,0]
        self.vidas -= 1
        self.posicion = [15,15]
        self.x = 15
        self.y = 15
        print('Vidas: ',self.vidas)
        self.lista_de_acitvidades = [self.reiniciar_partida,self.pasar,self.pasar,self.pasar]
        self.lista_de_acitvidades[self.vidas]()

    def set_id_casilla(self):
        """Devuelve el id de la casilla en el que está parado en modo de tuple"""
        return (self.casilla[0],self.casilla[1])

    def get_id_casilla(self):
        """Devuelve el id de la casilla en el que está parado en modo de lista"""
        return self.casilla

    def get_pos(self):
        """Devuelve la posicion del bomberman en el mapa"""
        return self.posicion

    def reiniciar_partida(self):
        """Cuando las hps sean igual a 0 se reinicia el nivel"""
        self.controlador.resetear_nivel(0)

    def redefinir_vertices(self):
        """Redefine las vertices (vertices) en funcion de los movimentos"""
        self.nueva_posicion_posible_parte_inferior = [0,0]
        self.nueva_posicion_posible_parte_superior = [0,0]
        self.vertices_1 = self.posicion
        self.vertices_2 = [self.posicion[0] + self.medidas, self.posicion[1]]
        self.vertices_3 = [self.posicion[0], self.posicion[1] + self.medidas]
        self.vertices_4 = [self.posicion[0] + self.medidas, self.posicion[1] + self.medidas]

    def pasar(self):
        pass
    
        