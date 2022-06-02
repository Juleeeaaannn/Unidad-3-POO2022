from aparato import Aparato


class Televisor(Aparato):
    __tipoPantalla=''
    __pulgadas=''
    __tipoDefinicion=''
    __conexion=False
    def __init__(self,marca,modelo,color,pais,precio,tipoPantalla,pulgadas,tipoDefinicion,conexion):
        super().__init__(self,marca,modelo,color,pais,precio,tipoPantalla,pulgadas,tipoDefinicion,conexion)
        self.__tipoPantalla=tipoPantalla
        self.__pulgadas=pulgadas
        self.__tipoDefinicion=tipoDefinicion
        self.__conexion=conexion
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                tipoPantalla=self.__tipoPantalla,
                pulgadas=self.__pulgadas,
                tipoDefinicion=self.__tipoDefinicion,
                conexion=self.__conexion
                )
                )
        return d