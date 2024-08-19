
import math

def divisionC(a,b):
    """
    Calcula la división de dos números complejos representados como tuplas.

    Parameters:
        a (tuple): Una tupla (parte_real, parte_imaginaria) que representa el primer número complejo.
        b (tuple): Una tupla (parte_real, parte_imaginaria) que representa el segundo número complejo.

    Returns:
        tuple: Una tupla (parte_real, parte_imaginaria) que representa el resultado de la división.
    """

    if ((b[0]**2 + b[1]**2) == 0):
        return ["La division no se puede realizar"]
    else:
        part_real = ((a[0]*b[0]) + (a[1]*b[1]))/(b[0]**2 + b[1]**2)
        part_ima = ((b[0]*a[1]) - (a[0]*b[1]))/(b[0]**2 + b[1]**2)
        return (part_real,part_ima)

def multiplicacionC(a,b):
    """
    Calcula la multiplicación de dos números complejos representados como tuplas.

    Parameters:
        a (tuple): Una tupla (parte_real, parte_imaginaria) que representa el primer número complejo.
        b (tuple): Una tupla (parte_real, parte_imaginaria) que representa el segundo número complejo.

    Returns:
        tuple: Una tupla (parte_real, parte_imaginaria) que representa el resultado de la multiplicación.
    """
    part_real = (a[0]*b[0]) - (a[1]*b[1])
    part_ima = (a[0]*b[1]) + (b[0]*a[1])
    return (part_real,part_ima)

def sumaC(a,b):
    """
    Calcula la suma de dos números complejos representados como tuplas.

    Parameters:
        a (tuple): Una tupla (parte_real, parte_imaginaria) que representa el primer número complejo.
        b (tuple): Una tupla (parte_real, parte_imaginaria) que representa el segundo número complejo.
        
    Returns:
        tuple: Una tupla (parte_real, parte_imaginaria) que representa el resultado de la suma.
    """
    part_real = (a[0]+b[0])
    part_ima = (a[1]+b[1])
    return (part_real,part_ima)

def moduloC(a):
    """
    Calcula el módulo de un número complejo representado como tupla.

    Parameters:
        a (tuple): Una tupla (parte_real, parte_imaginaria) que representa un número complejo.

    Returns:
        float : Una float que representa el resultado del módulo.
    """
    modulo = (a[0]**2+ a[1]**2)**(1/2)
    return modulo

def conjugadoC(a):
    """
    Calcula el conjugado de un número complejo representado como tupla.

    Parameters:
        a (tuple): Una tupla (parte_real, parte_imaginaria) que representa un número complejo.

    Returns:
        tuple: Una tupla (parte_real, parte_imaginaria) que representa el resultado del conjugado.
    """
    imaginario = (-1)*a[1]
    return (a[0],imaginario)

def faseC(a):
    """
    Calcula la fase(ángulo) de un número complejo representado como tupla.

    Parameters:
        a (tuple): Una tupla (parte_real, parte_imaginaria) que representa un número complejo.

    Returns:
        float : Un float que representa el resultado de la fase.
    """
    angulo =  math.atan2(a[1],a[0])
    return angulo

def convertCartesianoPolarC(a):
    """
    Hace la conversión de un numero complejo representado en coordenadas cartesianas a polares.

    Parameters:
        a (tuple): Una tupla (parte_real, parte_imaginaria) que representa un número complejo.

    Returns:
        tuple: Una tupla (longitud, ángulo) que representa el número complejo en coordenadas polares.
    """
    p = moduloC(a)
    angulo = faseC(a)
    return (p, angulo)

def convertPolarCartesianoC(a):
    """
    Hace la conversión de un numero complejo representado en coordenadas polares a cartesianas.

    Parameters:
        a (tuple): Una tupla (parte_real, parte_imaginaria) que representa un número complejo.

    Returns:
        tuple: Una tupla (longitud, ángulo) que representa el número complejo en coordenadas cartesianas.
    """
    part_real = a[0]* math.cos(a[1])
    part_ima = a[0]* math.sin(a[1])
    return (part_real, part_ima)

def prettyPrintingC(a):
    if (len(a) < 2):
        print(a[0])
    else:
        if (a[1] > 0):
            print(a[0],"+",a[1],"i" )
        elif(a[1] == 0):
            print(a[0])
        elif(a[0] == 0):
            print(a[1],"i")
        else:
            print(a[0],a[1],"i" )
            
def prettyPrintingCP(a):
    print(a[0],",",a[1]) 

if __name__ == '__main__':
    prettyPrintingC(divisionC([0,3],[-1,-1]))
    prettyPrintingC(sumaC([-2,1],[1,2]))
    prettyPrintingC(multiplicacionC([3,-2],[1,2]))
    prettyPrintingC([moduloC([4,-3])])
    prettyPrintingC([moduloC([1,1])])
    prettyPrintingC(conjugadoC([5,7]))
    prettyPrintingC([faseC([1,1])])
    prettyPrintingCP(convertCartesianoPolarC([1,1]))
    prettyPrintingC(convertPolarCartesianoC([1.414213562373095,0.7853981633974483]))
    print("-----------------------------------------------------------------")
    prettyPrintingC(sumaC((3, 2), (-5, 5.2)))
    prettyPrintingC(multiplicacionC((3, 5), (-2.6, 6.8)))
    prettyPrintingC(divisionC((3, 5), (-2.6, 6.8)))
    prettyPrintingC([moduloC((-2.6, 6.8))])
    prettyPrintingC(conjugadoC((3, 2)))
    prettyPrintingC(convertPolarCartesianoC((4.24, math.pi/6)))
    prettyPrintingCP(convertCartesianoPolarC((-2.6, 6.8)))
    prettyPrintingC([faseC((-2.6, 6.8))])


