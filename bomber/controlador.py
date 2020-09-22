import pygame,sys
from pygame.locals import *
import vista
import peron
import mapa
import bomba
import time

clock = pygame.time.Clock()
class Controlador:
    def __init__(self):
        self.dou = 0
        self.transicion_de_mapa = False
        self.tiempo_transcurrido_entransaccion_de_nivel = 0
        self.tiempo_de_transicion_de_nivel = 1000000
        self.mapa = mapa.Mapa(self,0) # El cero es para setear el nivel inicial
        self.tiempo = 0
        self.tiempo_para_la_aleatoreailizacion_de_los_reyes_de_la_noche = 0
        self.bomba = False
        self.estallido = False
        self.model = peron.Model(self,self.mapa)
        self.vista = vista.Vista(self.model)
        self.main_loop()

    def main_loop(self):
        """Metodo principal y vital del programa que recibe todas las interacciones con el teclado y administra el timepo. 
        Tambien hace que cada 75 ms se reprintee el mapa"""
        while True:
            clock.tick(400)
            self.tiempo += 1000
            self.tiempo_para_la_aleatoreailizacion_de_los_reyes_de_la_noche += 1000
            if self.mapa != None:
                self.mapa.tiempo(self.tiempo)
                if self.mapa != None:
                    self.mapa.tiempo_2(self.tiempo_para_la_aleatoreailizacion_de_los_reyes_de_la_noche)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.KEYDOWN and self.mapa != None: 
                    
                    if event.key == pygame.K_d:
                        self.mapa.mover_bm_derecha()  

                    if event.key == pygame.K_w:
                        self.mapa.mover_bm_arriba()

                    if event.key == pygame.K_s:
                        self.mapa.mover_bm_abajo()
                    
                    if event.key == pygame.K_a:
                        self.mapa.mover_bm_izquierda()

                    if event.key == pygame.K_RETURN:
                        self.mapa.crear_bomba()

            if self.mapa != None and self.transicion_de_mapa == False:
                self.vista.printear_partida()
                self.mapa.mover_rectilineamente_a_los_ww()

            if self.transicion_de_mapa == True:
                self.vista.printear_nada()
                self.tiempo_transcurrido_entransaccion_de_nivel += 1000
                if self.tiempo_transcurrido_entransaccion_de_nivel >= self.tiempo_de_transicion_de_nivel:
                    self.transicion_de_mapa = False
                    self.tiempo_transcurrido_entransaccion_de_nivel = 0

            pygame.display.flip()
            
    def restablecer_coordenadas_de_paredes_rompbiles(self):
        """Le indica a la vista que teine que pedir de nuevo las posiciones de las casillas rompibles"""
        self.vista.restablecer_coordenadas_de_paredes_rompbiles()
    
    def restablecer_coordenadas_de_estallidos(self):
        """Le indica a la vista que tiene que pedir de nuevo la posicion de los estallidos"""
        self.vista.restablecer_coordenadas_de_estallidos()
    
    def alterar_tiempo_de_bomba(self):
        """Se resetea el temporiza de la bomba"""
        self.tiempo = 0

    def alterar_tiempo_de_ww(self):
        """Se resetea el temporizador de los ww"""
        self.tiempo_para_la_aleatoreailizacion_de_los_reyes_de_la_noche = 0

    def resetear_nivel(self,nivel):
        """Se vuelve a crear el mapa y el modelo"""
        self.mapa = None
        self.transicion_de_mapa = True
        self.vista.printear_nada()
        self.mapa = mapa.Mapa(self,nivel)
        self.model = peron.Model(self,self.mapa)
        self.vista.borrar_todas_las_coordenadas(self.model)

if __name__=="__main__":
    controlador = Controlador()