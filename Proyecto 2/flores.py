class Flores:
    __numero=0
    __nombre=''
    __color=''
    __descipcion=''
    __vendidas=0
    def __init__(self,numero,nombre,color,descripcion):
        self.__numero=numero
        self.__nombre=nombre
        self.__color=color
        self.__descipcion=descripcion
        self.__vendidas=0
    def setVenta(self):
        self.__vendidas+=1
    def __str__(self):
        return('Numero:{}|| Nombre:{}').format(self.__numero,self.__nombre)
    def getNombre(self):
        return self.__nombre
    def getCodigo(self):
        return self.__numero