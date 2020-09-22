import bomberman
import parednorompible
import casillas
import bomba
import paredrompbile
import random
import peron
import estallido
import whitewalker
import portal

class Mapa:
    def __init__(self,controlador,nivel):
        self.controlador = controlador
        self.nivel_o_dificultad = 1 * (nivel == 0) + nivel  # Atributo que sirve para definir la provabilidad de spawn de paredes rompibles
        self.provabilidad_de_spawn_de_casillas_rompibles = 1 + 3 * (self.nivel_o_dificultad >= 1) * (self.nivel_o_dificultad <= 2) + 2 * (self.nivel_o_dificultad > 2) * (self.nivel_o_dificultad <= 4) + 1 * (self.nivel_o_dificultad > 4) 
        self.posbm = [15,15] #Setea la posiciòn inicial del Bomberman
        self.bomberman = bomberman.JonSnow(self,self.controlador) #Instancio el objeto de la clase JonSnow (bomberman)
        self.pos_paredes = None # A definir
        self.pos_bombas = None # A definir
        self.cantidad_de_paredes_no_rompibles = 4 # Cantidad de paredes no rompibles
        self.distancia_entre_paredes_no_rompibles = 160 # Distancia entre paraedes no rompinles (dos casillas)
        self.longitud_de_lado_de_casilla = 80 # Ancho y alto de las casillas
        self.cantidad_de_casillas = 9 # 81 casillas
        self.casillas = [] # Lista para definir casillas
        self.bombas = [] # Lista para definir bombas
        self.portal = []
        self.existe_bomba = False
        self.estallido_existe = False
        self.estallidos = [] # Lista para definir casilas
        self.cant_bombas = 1 # Cantidad posibles de bombas en el mapa
        self.paredes_no_rompibles = [] # Una lista que sirve para devolverle a la vista las posiciones de las paredes no rompibles (fijas)
        self.pos_de_casillas_en_x = 10 # Atributo para definir las posiciones de las casillas
        self.pos_de_casillas_en_y = 10 # "
        self.pos_de_paredes_no_rompibles_en_y = 90 # Atributo para definir las posiciones de las paredes no rompbiles
        self.pos_de_paredes_no_rompibles_en_x = 90 # "
        self.lista_de_objetos = [] # Lista que se usa para almacenar la casilla de las pared no rompible 
        self.list_de_coords_aux = [] # Listas de posiciones que devuelve el mapa
        self.list_de_coords_aux_2 = []
        self.list_de_coords_aux_3 = []
        self.list_de_coords_aux_4 = []
        self.id_casilla = [0,0] # id casilla inicial del Bomberman
        self.white_walkers = [] # A definir
        self.cant_ww = 3 * (self.nivel_o_dificultad >= 1) * (self.nivel_o_dificultad <= 2) + 5 * (self.nivel_o_dificultad > 2) * (self.nivel_o_dificultad <= 4) + 8 * (self.nivel_o_dificultad > 4) 
        self.crear_todo_el_mapa() # Se crea el mapa
        self.analizar_bomberman()

    def tiempo(self,tiempo_de_bombas):
        """Funcion que sirve para estallar la bomba y dispersae el fuego del estallido"""
        self.analizar_bomberman()
        self.analizar_ww()
        self.tiempo_transcurrido = None
        if self.existe_bomba == False:
            self.controlador.alterar_tiempo_de_bomba()

        if tiempo_de_bombas >= 100000 and self.existe_bomba == True and len(self.bombas) <= 1 and self.estallido_existe == False:
            self.estallido_existe = True
            self.tiempo_transcurrido = True
            self.estallar_bomba() 
    
        if tiempo_de_bombas >= 200000 and self.existe_bomba == True and self.estallido_existe == True:
            self.desaparecer_fuego()
            self.estallido_existe = False
            self.existe_bomba = False
            self.controlador.alterar_tiempo_de_bomba()

        return self.tiempo_transcurrido

    def tiempo_2(self,tiempo_de_ww):
        """Calcua el tiempo en el que los WhiteWalkers tienen que cambiar de direccion"""
        if tiempo_de_ww > 20000:
                self.mover_ww()
                self.controlador.alterar_tiempo_de_ww()
        
    def crear_todo_el_mapa(self):
        """Crea los objetos iniciales y elementales del mapa (casillas, paredes no rompibles, WhiteWalkers, y el portal)"""
        for i in range(0,self.cantidad_de_paredes_no_rompibles): # Defino paredes no rompibles
            self.pos_de_paredes_no_rompibles_en_x += self.distancia_entre_paredes_no_rompibles * (i != 0)
            for g in range(0,self.cantidad_de_paredes_no_rompibles):
                if self.pos_de_paredes_no_rompibles_en_y == 570:
                    self.pos_de_paredes_no_rompibles_en_y = 90
                self.pos_de_paredes_no_rompibles_en_y += self.distancia_entre_paredes_no_rompibles * (g != 0)  
                self.paredes_no_rompibles.append(parednorompible.Parednorompible([self.pos_de_paredes_no_rompibles_en_x,self.pos_de_paredes_no_rompibles_en_y]))
        
        for i in range(0,len(self.paredes_no_rompibles)):
            self.lista_de_objetos.append(self.paredes_no_rompibles[i].set_estado_de_algunas_casillas()) # Se setean el estado de las casillas con una pared no rompible encima
        
        for i in range(0,self.cantidad_de_casillas): # Defino casillas y a su vez esta crea las casillas rompibles
            self.id_casilla[0] += 1 * (i != 0)
            self.pos_de_casillas_en_x += self.longitud_de_lado_de_casilla * (i != 0)
            for g in range(0,self.cantidad_de_casillas):
                if self.pos_de_casillas_en_y == 650:
                    self.pos_de_casillas_en_y = 10 
                self.pos_de_casillas_en_y += self.longitud_de_lado_de_casilla * (g != 0)
                if self.id_casilla[1] == 8:
                    self.id_casilla[1] = 0
                self.id_casilla[1] += 1 * (g != 0)
                self.set_id_casilla = (self.id_casilla[0],self.id_casilla[1])
                self.casillas.append(casillas.Casilla(self.set_id_casilla,[self.pos_de_casillas_en_x,self.pos_de_casillas_en_y],self.lista_de_objetos,self.provabilidad_de_spawn_de_casillas_rompibles))
        
        self.crear_portal()
        self.crear_white_walkers() # Se crean tres objetos de la clase WhiteWalker

    def crear_white_walkers(self): # Crea 5 white calkers
        self.lista_de_casillas_no_ocupadas_aux = []
        for i in range(0,len(self.casillas)): # Se le pide el estado de las casillas para establecer los posbibles spawn de los enemigos
            consulta_2 = self.casillas[i].get_id_casilla_si_esta_ocupada()
            # Este if es para que los enemigos no spawneen cerca al bomberman
            if consulta_2 != None and consulta_2 != (0,0) and consulta_2 != (0,1) and consulta_2 != (0,2) and consulta_2 != (0,3) and consulta_2 != (1,0) and consulta_2 != (2,0):
                self.lista_de_casillas_no_ocupadas_aux.append(consulta_2)
            
        for i in range(0,self.cant_ww):
            self.white_walkers.append(whitewalker.WhiteWalker(self.lista_de_casillas_no_ocupadas_aux[random.randint(0,len(self.lista_de_casillas_no_ocupadas_aux) - 1)],self))

    def crear_portal(self):
        self.list_de_casillas_con_pared_rompible = []
        for i in range(0,len(self.casillas)):
            consulta_a_casilla = self.casillas[i].get_id_casilla_si_esta_desocupada()
            if consulta_a_casilla != None:
                self.list_de_casillas_con_pared_rompible.append(consulta_a_casilla)

        randomizador = random.randint(0,len(self.list_de_casillas_con_pared_rompible) - 1)
        self.portal.append(portal.Portal(self.list_de_casillas_con_pared_rompible[randomizador]))

    # Creación o modificación de los atributos de los objetos
    def analizar_bomberman(self):
        """En base a la posicion del bomberman, los estallidos, el portal, y los WhiteWalkers se calcula si el primero
        el personaje paso de nivel, o murio"""
        conuslta_al_bm_por_posicion = self.bomberman.get_pos()
        consultar_id_casilla_del_bomberman = self.bomberman.get_id_casilla()
        # Le pregunta al bomberman donde está
        for i in range(0, len(self.estallidos)):
            respuesta_de_estallido = self.estallidos[i].comparacion(conuslta_al_bm_por_posicion)
            
            if respuesta_de_estallido == 1 and consultar_id_casilla_del_bomberman != [0,0] and consultar_id_casilla_del_bomberman != [0,1] and consultar_id_casilla_del_bomberman != [1,0]:
                self.bomberman.respawnear()

        for index,pos in enumerate(self.white_walkers):
            consultar_id_casilla_de_ww = self.white_walkers[index].get_id_casilla()

            if consultar_id_casilla_de_ww == consultar_id_casilla_del_bomberman and consultar_id_casilla_del_bomberman != [0,0] and consultar_id_casilla_del_bomberman != [0,1] and consultar_id_casilla_del_bomberman != [1,0]:
                self.bomberman.respawnear()

        portals = self.portal[0].get_id_casilla()
        bomermans = self.bomberman.set_id_casilla()
        if portals == bomermans and len(self.white_walkers) == 0:
            print('Ganastes, pasas al siguiente nivel: ',self.nivel_o_dificultad + 1)
            self.controlador.resetear_nivel(self.nivel_o_dificultad + 1)

    def analizar_ww(self):
        """Se analiza si los WhiteWalkers entraron en contacto con el estallido"""
        for index,pos in enumerate(self.white_walkers):
            vertice_superior_izquierdo_del_ww_a_analizar = self.white_walkers[index].get_posicion()

            for g in range(0, len(self.estallidos)): # Este for es para que se le prgunte a todos los estallidos existentes
                respuesta_del_estallido = self.estallidos[g].comparacion(vertice_superior_izquierdo_del_ww_a_analizar)

                if respuesta_del_estallido == 1: # Si la respuesta del objeto estallido = 1 entonces el WhiteWalker morirá, de lo contrario no
                    self.white_walkers[index].desaparecer(index)
    
    def delet_bomberman(self,identificador_de_lista):
        """Deletea a uno de los WhiteWalker en base al identificador de la lista(un int)"""
        self.white_walkers.pop(identificador_de_lista)
        
    def mover_bm_derecha(self):
        """El mapa le ordena al bomberman moverse a la derecha"""
        self.posbm = self.bomberman.mover_bm_derecha()
        
    def mover_bm_izquierda(self):
        """El mapa le ordena al bomberman moverse a la izquierda"""
        self.posbm =self.bomberman.mover_bm_izquierda()

    def mover_bm_abajo(self):
        """El mapa le ordena al bomberman moverse hacia abajo"""
        self.posbm = self.bomberman.mover_bm_abajo()

    def mover_bm_arriba(self):
        """El mapa le ordena al bomberman moverse hacia arriba"""
        self.posbm = self.bomberman.mover_bm_arriba()

    def consultar_casilla_por_movimiento(self,casilla_a_preguntar,vertice,pixel_definitorio_de_casilla):
        """Desde un objeto de clase bomberman se le ordena al mapa que le pregunte a la casilla correspondiente (definida
        por el mismo objeto bomberman) si se puede mover o no y definir en que casilla esta"""
        # Este if es para que detecte si son casillas coherentes(que no sean negativas o mayor a la cantidad total que existe de casillas)
        if casilla_a_preguntar[0] >= 0 and casilla_a_preguntar[0] <= 8 and casilla_a_preguntar[1] <= 8 and casilla_a_preguntar[1] >= 0:
            for index,pos in enumerate(self.casillas):       
                self.casilla_aux = self.casillas[index].get_id_casilla()
                casilla_a_preguntar = (casilla_a_preguntar[0], casilla_a_preguntar[1])
                if self.casilla_aux == casilla_a_preguntar:
                    self.respuesta_de_movimiento_de_bm = self.casillas[index].calcular_si_se_puede_mover(vertice,pixel_definitorio_de_casilla)
                    return self.respuesta_de_movimiento_de_bm
        return[0,0]

    def crear_bomba(self):
        """Crea la bomba. Le pide al bomberman que le pase la casilla del mismo"""
        if len(self.bombas) != self.cant_bombas and self.existe_bomba == False:
            self.existe_bomba = True            
            self.posicion_de_nueva_bomba = self.bomberman.set_id_casilla()
            self.bombas.append(bomba.Bomba(self.posicion_de_nueva_bomba,self))

    def estallar_bomba(self):
        """Estalla la bomba (solo puede haber una bomba a la vez y ademas no se puede plantar una mientras exista
        el estallido"""
        if len(self.bombas) == 1:
            self.bombas[0].estallar()
            self.bombas.pop(0) # Se elimina la bomba
            self.list_de_coords_aux_2 = [] 

    def desaparecer_fuego(self):
        """Desaparece el estallido"""
        if len(self.estallidos) >= 1:
            for i in range(0,len(self.casillas)):
                self.casillas[i].transformar_a_casilla_sin_fuego()

            self.estallidos = []
            self.controlador.restablecer_coordenadas_de_estallidos()     
            self.list_de_coords_aux_4 = []

    def eliminar_paredes_rompibles_cercanas(self,casilla_a_preguntar):
        """En base a la expansion del estallido se le pregunta a las casillas correspondientes si se tienen una casilla 
        rompible encima, de ser asi destruirla y ponerla en estado 'con fuego = True' lo que sirve para el bm y los ww,
         de lo contrario crear fuego"""
        self.mandale_mecha = None
        if casilla_a_preguntar[0] >= 0 and casilla_a_preguntar[0] <= 8 and casilla_a_preguntar[1] <= 8 and casilla_a_preguntar[1] >= 0:
            for index,pos in enumerate(self.casillas):       
                self.casilla_aux = self.casillas[index].get_id_casilla()
                casilla_a_preguntar = (casilla_a_preguntar[0], casilla_a_preguntar[1])
                self.consulta = self.casillas[index].devolver_estado_de_casilla()
                if self.casilla_aux == casilla_a_preguntar:
                    if self.consulta == True:
                        self.mandale_mecha = 0
                    self.casillas[index].transformar_a_casilla_atravesable()
                    self.casillas[index].transformar_a_casilla_con_fuego()
                    consulta = self.casillas[index].get_vertices()
                    for index2,po in enumerate(self.list_de_coords_aux_3):
                        if self.list_de_coords_aux_3[index2] == consulta:
                            self.list_de_coords_aux_3.pop(index2)
                            self.mandale_mecha = 0
                            break
                            self.controlador.restablecer_coordenadas_de_paredes_rompbiles()

        return self.mandale_mecha
               
    def crear_el_mismisimo_fuego_valiryo_proveniente_del_temible_Dragon_Drogo(self,coord):
        """Se crea un estallido con una coordenada determinada"""
        self.estallidos.append(estallido.Estallido(coord))
        self.controlador.restablecer_coordenadas_de_estallidos() 

    # A partir de esta línea, estos métodos, le devuelven al modelo (para que la vista le robe información) 
    # las ubiaciones de todos los objetos
    def posicion_de_paredes_no_rompibles(self):
        """Se agregan a una lista las coordenadas en el mapa de las paredes rompibles y se returnea"""
        for i in range(0,len(self.paredes_no_rompibles)):
            self.list_de_coords_aux.append(self.paredes_no_rompibles[i].set_coords())
             
        return self.list_de_coords_aux

    def posicion_de_bombas(self):
        """Se agrega a una lista las coordenada en el mapa de la bomba y se returnea"""
        if len(self.bombas) != 0:
            for i in range(0,len(self.bombas)):
                self.list_de_coords_aux_2.append(self.bombas[i].set_coords())

        return self.list_de_coords_aux_2
    
    def posicion_de_paredes_rompibles(self):
        """Se agregan a una lista las coordenadas en el mapa de las paredes rompibles y se returnea"""
        for i in range(0,len(self.casillas)):
            consulta = self.casillas[i].get_id_casilla_si_esta_con_una_pared_rompible()
            if consulta != None:
                self.list_de_coords_aux_3.append(consulta)
        
        return self.list_de_coords_aux_3


    def posicion_de_estallidos(self):
        """Se agrega a una lista las coordenada en el mapa de los estallidos y se returnea"""
        for i in range(0,len(self.estallidos)):
            consulta = self.estallidos[i].set_coords()
            self.list_de_coords_aux_4.append(consulta)

        return self.list_de_coords_aux_4

    def estadisticas_bm(self):
        """Se devuelve la coordenada del bomberman"""
        self.posbm = self.bomberman.get_pos()
        return self.posbm

    def posicion_de_ww(self):
        self.list_de_coords_aux_5 = []
        for i in range(0,len(self.white_walkers)):
            consulta = self.white_walkers[i].get_posicion()
            self.list_de_coords_aux_5.append(consulta)

        return self.list_de_coords_aux_5

    def posicion_de_portal(self):
        self.coords_portal = self.portal[0].get_posiciones()
        return self.coords_portal

    def mover_ww(self):
        """Se le ordena a los WhiteWalkers cambiar de direccion"""
        for i in range(0,len(self.white_walkers)):
            self.white_walkers[i].mover_aleatoriamente()

    def mover_rectilineamente_a_los_ww(self):
        """Se le ordena a los WhiteWalkers que caminen"""
        for i in range(0,len(self.white_walkers)):
            self.white_walkers[i].mover_rectilineamente()
