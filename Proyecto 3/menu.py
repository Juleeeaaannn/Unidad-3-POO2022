from manejadorcontrato import ManejaContrato 
from manejadorjugador import ManejaJugador
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.salir}
    def opcion(self,op,ManejadorJ,ManejadorC):
        func=self.__switcher.get(op,lambda:'opcion incorrecta!')
        if(op=='1' or op=='2' or op=='3'):
            func(ManejadorJ,ManejadorC)
        else:
            func()
    def opcion1(self,ManejadorC,ManejadorJ):
        if(type(ManejadorC)==ManejaContrato and type(ManejadorJ)==ManejaJugador):
            pass