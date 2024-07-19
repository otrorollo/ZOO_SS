from app.vistas import VistaInput, VistaGrupo, VistaInputEdad, VistaInputSN
from app.modelos import Grupo_Entrada
from simple_screen import DIMENSIONS, cls,locate,Input,Screen_manager


class Zoo:
    def __init__(self):
        self.grupo_entradas = Grupo_Entrada()
        self.x = (DIMENSIONS.w - 37 ) // 2
        self.VistaGrupo = VistaGrupo(self.grupo_entradas, self.x, 1)
        self.entrada_edad = VistaInputEdad("EDAD: ",self.x ,10)
        self.entrada_seguir = VistaInputSN("Otra vez (S/n): ",self.x ,12)

    def run(self):
        with Screen_manager:
        #Bucle de pantalla
            while True:
                cls()
                self.VistaGrupo.paint()
                edad = self.entrada_edad.paint()
                if edad == "":
                    respuesta = self.entrada_seguir.paint()
                    if respuesta.lower() == "s":
                        self.grupo_entradas = Grupo_Entrada()
                        self.VistaGrupo.grupo = self.grupo_entradas
                        continue
                    else: 
                        break
                        
                try:
                    edad = int(edad)
                    self.grupo_entradas.add_entrada(edad)
                except ValueError as e:
                    error_message = f"Error: {e} Pulsa enter para continuar"
                    msg_length = len(error_message)
                    error_x = (DIMENSIONS.w - msg_length) // 2
                    locate(error_x, DIMENSIONS.h - 2, error_message)
                    Input("Pulsa enter para continuar")




"""
with Screen_manager:
    #Instanciamos todo lo necesario, modelos y componentes gráficos
    grupo_entradas = Grupo_entrada()
    x = (DIMENSIONS.w - 37 )//2
    VistaGrupo = VistaGrupo(grupo_entradas, x, 1)
    entrada_edad = VistaEntrada("EDAD: ",x ,10)
    entrada_seguir = VistaEntrada("Otra vez (S/n): ",x ,12)
    #Bucle de pantalla
    while True:
        cls()
        VistaGrupo.paint()
        edad = entrada_edad.paint()
        if edad == "":
            respuesta = entrada_seguir.paint()
            if respuesta == "S":
                grupo_entradas = Grupo_entrada()
                VistaGrupo.grupo = grupo_entradas
                continue
            else: 
                break
        edad = int(edad)
        grupo_entradas.add_entrada(edad)
        #VistaGrupo.grupo.add_entrada(edad)
#Final "controlado" del programa
locate(1, DIMENSIONS.h - 2)
Input("pulse enter para salir")
"""
