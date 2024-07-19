from enum import Enum, auto
from collections import namedtuple


Datos_Entrada = namedtuple("Datos_Entrada", ("precio", "edad_max"))

#adherencia
class TipoEntrada(Enum):  #se actualiza a tupla
    BEBE = Datos_Entrada(0, 2)
    NIÑO = Datos_Entrada(15, 12)
    ADULTO = Datos_Entrada(25, 64)
    JUBILADO = Datos_Entrada(20, 99)
class Entrada:
  def __init__(self, edad: int): #constructor de instancia
    self.__validate_edad(edad)
    self.__edad = edad
        
    for tipo in TipoEntrada: #esto itera sobre tipoentrada por value[posicion]
      if edad <= tipo.value.edad_max:
        self.tipo = tipo
        self.precio = tipo.value.precio
        break

  def __validate_edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no debe ser negativa")
        elif edad > 99:
            raise ValueError("La edad no puede ser mayor de 99")  
        
class Grupo_Entrada: #molde
  def __init__(self): #constructor (instancia)
    self.total = 0 #esto es el contador total precio
    self.num_entradas = 0 #esto es el contador de entradas

    self.tipos_entrada = {}
    for tipo in TipoEntrada:
      #if tipo.value > 0:
      self.tipos_entrada[tipo] = {'Q': 0, 'P': tipo.value.precio}

        # con dict comprehension
        #self.tipos_entrada = {tipo: {'Q': 0, 'P': tipo.value} for tipo in TipoEntrada # if tipo.value > 0 }
    """
    lista = []
    for tipo in TipoEntrada:
      lista.append((tipo.name, tipo.value))
    lista = [(tipo.name, tipo.value) for tipo in TipoEntrada]
    """
    """
    self.tipos_entrada = {
      TipoEntrada.BEBE: {"Q":0, "P":0},
      TipoEntrada.NIÑO: {"Q":0, "P":14},
      TipoEntrada.ADULTO: {"Q":0, "P":23},
      TipoEntrada.JUBILADO: {"Q":0, "P":18}
    }
    """
  def add_entrada(self, edad):
    """
    En funcion de la edad, crear una entrada e incrementar el contador de entradas.
    Con el precio de la entrada nueva incrementar el total.
    """ 
    """
    if edad not in range(0, 100):
      raise ValueError("La edad introducida no es válida")
    """
    nueva_entrada = Entrada(edad)
    self.num_entradas += 1
    self.total += nueva_entrada.precio
    self.tipos_entrada[nueva_entrada.tipo]['Q'] += 1

  def cantidad_entradas_por_tipo(self, tipo: TipoEntrada) -> int: 
    return self.tipos_entrada[tipo]['Q']
  
  def subtotal_tipo(self, tipo: TipoEntrada) -> int:
    return self.tipos_entrada[tipo]['Q'] * self.tipos_entrada[tipo]['P']