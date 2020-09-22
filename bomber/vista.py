import pygame,sys
from pygame.locals import *

class Vista:
    
    def __init__(self,model):
        pygame.init()
        self.diccionario_de_imagenes_de_partida = {
                                                    "goi" : pygame.image.load('./goi.png'),
                                                    "ww2" : pygame.image.load('./WhiteWalker.png'),
                                                    "portal" : pygame.image.load('./portal.png'),
                                                    "bomberman" : pygame.image.load('./JS.png'),
                                                    "fuego" : pygame.image.load('./fuego.png'),
                                                    "bomba" : pygame.image.load('./b.png'),
                                                    "fondopartida" : pygame.image.load('./fondopartida.png'),
                                                    "pared_no_rompible" : pygame.image.load('./pared.png'),
                                                    "paredes_rompibles" : pygame.image.load('./paredrompbile.png'),
                                                    }
        self.model = model
        self.cambio_de_estallidos = 1
        self.cambio_de_lista_de_parede_rompibles = 1
        self.window = pygame.display.set_mode((740,740))
        self.posiciones_de_paredes_no_rompibles = []
        self.posicion_paredes_rompibles = []
        self.posicion_de_portal = []
        self.diccionario_de_imagenes_de_partida["fuego"] = pygame.transform.scale(self.diccionario_de_imagenes_de_partida["fuego"],[100,100])
        self.diccionario_de_imagenes_de_partida["fondopartida"] = pygame.transform.scale(self.diccionario_de_imagenes_de_partida["fondopartida"],[740,740])
        self.diccionario_de_imagenes_de_partida["bomberman"] = pygame.transform.scale(self.diccionario_de_imagenes_de_partida["bomberman"],[45,45])
        pygame.display.set_caption('Game of ice')
        pygame.key.set_repeat(20)
        self.printear_partida()

    def restablecer_coordenadas_de_paredes_rompbiles(self):
        self.cambio_de_lista_de_parede_rompibles = 1

    def restablecer_coordenadas_de_estallidos(self):
        self.cambio_de_estallidos = 1
        
    def printear_partida(self):
        """En este metodo se piden todos los datos de las posiociones de los objetos que estan en el mapa y se dibujan en
        la pantalla"""
        self.poisicion_bm = self.model.estadisticas_bm()
        self.posicion_bombas = self.model.posicion_de_bombas()
        self.posicion_ww = self.model.posicion_de_ww()
        if self.posicion_de_portal == []:
            self.posicion_de_portal = self.model.posicion_de_portal()
        if self.cambio_de_estallidos == 1:
            self.posicion_estallidos = self.model.posicion_de_estallidos()
            self.cambio_de_estallidos = 0
        if self.cambio_de_lista_de_parede_rompibles == 1:
           self.posicion_paredes_rompibles = self.model.posicion_de_paredes_rompibles() 
           self.cambio_de_lista_de_parede_rompibles = 0
        if self.posiciones_de_paredes_no_rompibles == []:
            self.posiciones_de_paredes_no_rompibles = self.model.get_posiciones_paredes_no_rompibles()
        self.window.blit(self.diccionario_de_imagenes_de_partida["fondopartida"],[0,0])
        self.window.blit(self.diccionario_de_imagenes_de_partida["portal"],self.posicion_de_portal)
        for index,pos in enumerate(self.posicion_paredes_rompibles):
            self.window.blit(self.diccionario_de_imagenes_de_partida["paredes_rompibles"],self.posicion_paredes_rompibles[index])
        for index,pos in enumerate(self.posiciones_de_paredes_no_rompibles):
            self.window.blit(self.diccionario_de_imagenes_de_partida["pared_no_rompible"],self.posiciones_de_paredes_no_rompibles[index])
        if self.posicion_bombas != None:    
            for index,pos in enumerate(self.posicion_bombas):
                self.window.blit(self.diccionario_de_imagenes_de_partida["bomba"],self.posicion_bombas[index])
        pygame.draw.rect(self.window,(255,255,0),pygame.Rect(self.poisicion_bm[0],self.poisicion_bm[1],45,45),1)
        self.window.blit(self.diccionario_de_imagenes_de_partida["bomberman"],self.poisicion_bm)
        for index2,pos in enumerate(self.posicion_ww):
            pos1 = pos[0]
            pos2 = pos[1]
            self.window.blit(self.diccionario_de_imagenes_de_partida["ww2"],self.posicion_ww[index2])
            pygame.draw.rect(self.window,(255,120,5),pygame.Rect(pos1,pos2,70,70),1)
        for index,pos in enumerate(self.posicion_estallidos):
            self.window.blit(self.diccionario_de_imagenes_de_partida["fuego"],self.posicion_estallidos[index])

    def printear_nada(self):
        pygame.draw.rect(self.window,(153,255,51),pygame.Rect(0,0,740,740),740)
        self.window.blit(self.diccionario_de_imagenes_de_partida["goi"],(25,300))
        

    def borrar_todas_las_coordenadas(self,model):
        self.cambio_de_estallidos = 1
        self.model = model
        self.cambio_de_lista_de_parede_rompibles = 1
        self.posiciones_de_paredes_no_rompibles = []
        self.posicion_paredes_rompibles = []
        self.posicion_de_portal = []
        
