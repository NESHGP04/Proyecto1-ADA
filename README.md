# Máquina de Turing - Sucesión de Fibonacci

> Implementación de una Máquina de Turing para calcular la sucesión de Fibonacci usando representación unaria

## Descripción

Este proyecto implementa una **Máquina de Turing determinista** que calcula el n-ésimo término de la sucesión de Fibonacci utilizando representación unaria. Desarrollado como parte del curso de Análisis y Diseño de Algoritmos en la Universidad del Valle de Guatemala.

### Algoritmo de Fibonacci
```
F(n) = F(n-1) + F(n-2)
```

## Características

- Simulador de Máquina de Turing en Python
- Configuración mediante archivo JSON
- Representación unaria de enteros no negativos
- Visualización paso a paso de la ejecución
- Análisis empírico de complejidad
- Máquina determinista de una sola cinta

## Convenciones

### Representación Unaria
- **0**: No se representa
- **1**: `1`
- **2**: `11`
- **3**: `111`
- **n**: n veces el símbolo `1`

### Símbolos de Cinta
- `1`: Representa una unidad
- `0`: Separador entre números
- `B`: Celda vacía (blanco)
- `A`: Indicador de posición

### Organización de la Cinta
Durante la ejecución, la máquina mantiene la estructura:
```
F(i-2) 0 F(i-1) 0 contador
```

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/NESHGP04/Proyecto1-ADA.git

# Navegar al directorio
cd Proyecto1-ADA

# Instalar dependencias (si las hay)
pip install -r requirements.txt
```

## Uso

### Ejecutar el simulador

```bash
python maquina.py
```

### Formato de Entrada

La entrada debe ser una cadena de unos (`1`) en representación unaria:

- Para calcular F(1): `1`
- Para calcular F(2): `11`
- Para calcular F(3): `111`
- Para calcular F(4): `1111`

### Ejemplo de Ejecución

```
Entrada (unaria): 11
Configuración inicial: 1 0 1 0 11
...
Salida: 11 (Fibonacci de 2 = 1)
```

## Estructura del Proyecto

```
Proyecto1-ADA/
├── fibonacci_tm.json    # Configuración de la Máquina de Turing
├── maquina.py           # Programa principal
└── README.md          # Este archivo
```

## Configuración de la Máquina

El archivo `fibonacci_tm.json` contiene:
- Estados de la máquina
- Alfabeto de entrada
- Alfabeto de cinta
- Estado inicial
- Estados finales
- Función de transición

### Formato de Transiciones

```json
{
  "estado_actual": {
    "simbolo_leido": ["estado_siguiente", "simbolo_escrito", "movimiento"]
  }
}
```

## Análisis de Complejidad

### Datos Experimentales

| n | Entrada | Pasos Ejecutados |
|---|---------|------------------|
| 1 | 1       | 2                |
| 2 | 11      | 20               |
| 3 | 111     | 53               |
| 4 | 1111    | 108              |
| 5 | 11111   | 215              |
| 6 | 111111  | 428              |

### Complejidad Temporal

El análisis empírico muestra que la complejidad temporal está acotada por:

```
T(n) = O(n · φⁿ)
```

- **Regresión polinomial**: Grado 3 con R² = 0.9994
- **Crecimiento**: Exponencial coherente con la sucesión de Fibonacci

## 🎥 Video Explicativo

[![Video Explicación](https://img.shields.io/badge/YouTube-Video_Explicativo-red)](https://youtu.be/_FwNm_uatnA)

## 👥 Autores

- **Camila Richter** - 23183
- **Marinés García** - 23391
- **Carlos Alburez** - 231311

**Instructor**: Gabriel Brolo  
**Sección**: 10

