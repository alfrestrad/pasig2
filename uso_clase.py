#



class colonia(Municipio):
    ah = 0
    # Definición de constructor
    def __init__(self, areaH, nombre, clave, pobTotal, altitud, superficie):
        super().__init__(nombre, clave, pobTotal, altitud, superficie)
        self.ah = areaH
        # Métodos d ela clase GET & SET 
        def getAH(self):
            return self.ah
        def setAH(self, ah):
            self.ah = ah
        # Métodos alternativos
        def infoAH(self, value):
            self.ah = self.ah + value
            self.info()
            print (sel.nom, "cuenta con ", self.ah, "áreas homogéneas")
            
col = colonia(5, "Toluca", "106", 7435435, 4700, 453634)
print(col.getAH(3))
print(col.getNom())

    