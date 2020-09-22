class Portal:
    def __init__(self,id_casilla):
        self.id_casilla = id_casilla
        self.pixeles_casilla = 80
        self.pixeles_muro = 10
        self.posicion = [self.id_casilla[0] * self.pixeles_casilla + self.pixeles_muro,
                        self.id_casilla[1] * self.pixeles_casilla + self.pixeles_muro] 
                                                                                    # La posicion se define en base al  
                                                                                    # id_casilla del objeto. Formula:
                                                                                    # id de casilla en X se le multiplica
                                                                                    # por el largo del lado de las casilla
                                                                                    # (lo mismo en Y) y se le suma 10 
        print('id_de_casilla_de_portal',self.id_casilla)

    # Metodos que sirven para devolverle al mapa informacion del objeto
    def get_posiciones(self):
        """Se devuelve la posicion del objeto"""
        return self.posicion

    def get_id_casilla(self):
        """Se devuelve el id de casilla del objeto"""
        return self.id_casilla