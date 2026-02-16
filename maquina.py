import json
import os

class MaquinaTuring:
    def __init__(self, ruta_json):
        try:
            with open(ruta_json, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Componentes de la MT
            self.estados = data['Q']
            self.estado_inicial = data['S']
            self.blanco = data['b']
            self.finales = data['F']
            self.transiciones = data['transitions']
            self.reset()
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            exit()

    def reset(self):
        self.estado_actual = self.estado_inicial
        self.cinta = []
        self.posicion = 0
        self.contador_pasos = 0

    def cargar_entrada(self, cadena):
        self.reset()
        # Si la entrada esta vacia usamos el simbolo blanco por defecto
        self.cinta = list(cadena) if cadena else [self.blanco]
        self.posicion = 0

    def imprimir_config(self):
        # Muestra el estado actual y resalta la cabeza en la cinta
        copia_cinta = list(self.cinta)
        actual = copia_cinta[self.posicion]
        copia_cinta[self.posicion] = f"[{actual}]"
        
        cinta_visual = "".join(copia_cinta)
        print(f"Paso: {self.contador_pasos:<4} | Est: {self.estado_actual:<4} | Pos: {self.posicion:<3} | Cinta: {cinta_visual}")
