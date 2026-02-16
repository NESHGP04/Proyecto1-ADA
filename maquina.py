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