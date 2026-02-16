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

    def ejecutar_paso(self):
        simbolo_leido = self.cinta[self.posicion]
        
        # Validacion de transicion existente
        if self.estado_actual not in self.transiciones or simbolo_leido not in self.transiciones[self.estado_actual]:
            return False

        nuevo_estado, escribir, mov = self.transiciones[self.estado_actual][simbolo_leido]
        
        # Actualizacion de la cinta y el estado
        self.cinta[self.posicion] = escribir
        self.estado_actual = nuevo_estado
        self.posicion += mov
        self.contador_pasos += 1

        # Crecimiento dinamico de la cinta para simular que es infinita
        if self.posicion < 0:
            self.cinta.insert(0, self.blanco)
            self.posicion = 0
        elif self.posicion >= len(self.cinta):
            self.cinta.append(self.blanco)
        
        return True

    def iniciar(self):
        print("\n--- Simulacion Iniciada ---")
        self.imprimir_config()
        
        while self.estado_actual not in self.finales:
            if not self.ejecutar_paso():
                print("Halt: No hay mas transiciones.")
                break
            self.imprimir_config()
        
        # Resultado final procesado
        final = "".join(self.cinta).replace(self.blanco, "")
        print("\n" + "="*35)
        print(f"PASOS TOTALES: {self.contador_pasos}")
        print(f"CONTENIDO FINAL: {final}")
        print(f"VALOR (LONGITUD): {len(final)}")
        print("="*35)

def menu():
    config = "fibonacci_tm.json"
    mt = MaquinaTuring(config)

    while True:
        print("\nPROYECTO: ANALISIS DE ALGORITMOS")
        print(f"Leyendo: {config}")
        user_input = input("Entrada (unaria): ").strip()
        
        mt.cargar_entrada(user_input)
        mt.iniciar()
        
        op = input("\nProbar con otra cadena? (s/n): ").lower()
        if op != 's':
            print("Cerrando simulador...")
            break

# Ejecucion directa del programa
menu()