### Librería de Operaciones para Números Complejos

## Descripción

Esta librería está diseñada para realizar operaciones matemáticas entre números complejos, tanto en su representación cartesiana como polar. La librería permite la manipulación y operación de números complejos modelados como tuplas, donde la primera posición representa la parte real y la segunda la parte imaginaria en la representación cartesiana. En la representación polar, la primera posición es la magnitud (módulo) y la segunda es la fase (ángulo en radianes).

## Operaciones

- **Suma:** `sumaC(complejo1, complejo2)`
- **Producto:** `multiplicacionC(complejo1, complejo2)`
- **División:** `divisionC(complejo1, complejo2)`
- **Módulo:** `moduloC(complejo1)`
- **Conjugado:** `conjugadoC(complejo1)`
- **Conversión Polar a Cartesiano:** `convertPolarCartesianoC(coordenadas_polares)`
- **Conversión Cartesiano a Polar:** `convertCartesianoPolarC(coordenadas_cartesianas)`
- **Fase:** `faseC(complejo1)`

## Requisitos

- [Python 3.12](https://www.python.org)

## Uso

1. **Instalación**:
   - Clone o descargue el repositorio.
   - Abra el proyecto en algun editor de código que soporte python (Visual Studio Code, Pycharm).
   - Importe la librería en su proyecto de Python.

2. **Ejemplo de Uso**:
   ```python
   import libComplejos as lc

   complejo1 = (3, 4)  # 3 + 4i
   complejo2 = (1, 2)  # 1 + 2i

   suma = lc.sumaC(complejo1, complejo2)
   print("Suma:", sum_result)

    # Conversión polar a cartesiano
    cordenada_Polar = (5, 0.927295218)
    cartesian_result = lc.convertPolarCartesianoC(cordenada_Polar)
    print("Coordenadas cartesianas:", cartesian_result)
    ```
## Autor
**Maria Valentina Torres Monsalve**

