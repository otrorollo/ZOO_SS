"""
               1         2         3
      1234567890123456789012345678901234567
01    TIPO             PU     Q       TOTAL
02    =====================================
03    BEBE (≤2)      0.00    99     9999.99
04    NINO (≤12)    14.00    99     9999.99
05    ADULTO (<65)  23.00    99     9999.99
06    JUBILADO      18.00    99     9999.99
07    -------------------------------------
08                          999    99999.99
09
10    EDAD:
11    CONF
"""

from app.modelos import Grupo_Entrada, TipoEntrada, Entrada
from simple_screen import locate, Print, cls, Screen_manager, Input


class VistaGrupo:
    def __init__(self, grupo: Grupo_Entrada, x=1, y=1):
        self.grupo = grupo
        self.x = x  # hay que crearlo como atributo para utilizarlo luego
        self.y = y

    def paint(self):
        #titulo de la tabla
        locate(self.x, self.y, "TIPO             PU     Q       TOTAL")
        locate(self.x, self.y + 1, "=====================================")
        
        # Iterar sobre los tipos de entradas definidos en el Enum TipoEntrada
        for indice, tipo in enumerate(TipoEntrada):
            locate(
                self.x,
                self.y + 3 + indice,
                f"{tipo.name:.<14s}{tipo.value.precio:5.2f}    {self.grupo.cantidad_entradas_por_tipo(tipo):2d}     {self.grupo.subtotal_tipo(tipo):7.2f}",
            )

        # Línea separadora y totales
        locate(self.x, self.y + 7, "-------------------------------------")
        locate(
            self.x,
            self.y + 8,
            f"                      {self.grupo.num_entradas:3d}    {self.grupo.total:8.2f}",
        )


class VistaEntrada:
    def __init__(self, etiqueta: str, x, y):
        self.etiqueta = etiqueta
        self.y = y
        self.x = x
        self.value = ""
        # (se inicia el value)

    def paint(self):
        locate(self.x, self.y, self.etiqueta)
        # self.value = Input() #nos permite un metodo de validacion desde dentro
        return Input()


print(__name__)
if __name__ == "__main__":
    with Screen_manager:
        # Crear un grupo de entradas y agregar algunas entradas
        grupo = Grupo_Entrada()
        grupo.add_entrada(2)
        grupo.add_entrada(6)
        grupo.add_entrada(15)
        # Crear y pintar la vista del grupo
        vg = VistaGrupo(grupo)
        vg.paint()
        # Crear otro grupo de entradas y agregar algunas entradas
        otrog = Grupo_Entrada()
        otrog.add_entrada(54)
        otrog.add_entrada(43)
        # Crear y pintar la vista del segundo grupo
        vg2 = VistaGrupo(otrog, 42, 1)
        vg2.paint()

        Input("Pulsa enter para acabar")
