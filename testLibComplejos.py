import libComplejos as lc
import unittest
import math

class TestComplexOperations(unittest.TestCase):

    def test_suma1(self):
        
        # a = -5 + 2i
        # b = 3 - 10i
        # (a1,a2) + (b1,b2) = ((a1+b1) , (a2+b2))
        # Resultado esperado: -2 - 8i
        a = [-5, 2]
        b = [3, -10]
        resultado = lc.sumaC(a, b)
        self.assertEqual((-2, -8), resultado) 
        self.assertNotEqual((2, 8), resultado) 
     
    def test_suma2(self):
        # a = 2i
        # b = 4 - 10i
        # (a1,a2) + (b1,b2) = ((a1+b1) , (a2+b2))
        # Resultado esperado: 4 - 8i
        a = [0, 2]
        b = [4, -10]
        resultado = lc.sumaC(a, b)
        self.assertEqual((4, -8), resultado) 
        self.assertNotEqual((2, 8), resultado) 
    
    def test_multiplicacion1(self):
        # a = 2i
        # b = 4 - 10i
        # (a1,a2) * (b1,b2) = ((a1*b1 - (a2*b2)) , ((a1*b2) + (a2*b1)))
        # Resultado esperado:  20 + 8i

        a = [0, 2]
        b = [4, -10]
        resultado = lc.multiplicacionC(a, b)
        self.assertEqual((20, 8), resultado) 
        self.assertNotEqual((2, 8), resultado) 
    
    def test_multiplicacion2(self):
        # a = 2
        # b = 4 - 10i
        # (a1,a2) * (b1,b2) = ((a1*b1 - (a2*b2)) , ((a1*b2) + (a2*b1)))
        # Resultado esperado:  20 - 20i

        a = [2, 0]
        b = [4, -10]
        resultado = lc.multiplicacionC(a, b)
        self.assertEqual((8, -20), resultado) 
        self.assertNotEqual((2, 8), resultado) 

    def test_division1(self):
        # a = 10 + 2i
        # b =  0 + 0i
        # (a1,a2) * (b1,b2) = (((a1*b1) + (a2*b2))/(b1**2 + b2**2)) , ((b1*a2) - (a1*b2))/(b1**2 + b2**2))
        # Resultado esperado: "La divion no se puede realizar"

        a = [10, 2]
        b = [0, 0]
        resultado = lc.divisionC(a, b)
        self.assertEqual(["La division no se puede realizar"], resultado) 
        self.assertNotEqual((2, 8), resultado) 
    
    def test_division2(self):
        # a = 3i
        # b = -1 - i
        # (a1,a2) * (b1,b2) = (((a1*b1) + (a2*b2))/(b1**2 + b2**2)) , ((b1*a2) - (a1*b2))/(b1**2 + b2**2))
        # Resultado esperado: -1.5 - 1.5i 
        
        a = [0, 3]
        b = [-1, -1]
        resultado = lc.divisionC(a, b)
        self.assertEqual((-1.5,-1.5), resultado) 
        self.assertNotEqual((2, 8), resultado) 
    
    def test_modulo1(self):
        # a = 4 + 6i
        # |(a1,a2)| = sqrt(a1**2 + a2**2)
        # Resultado esperado: 7.2111 

        a = [4, 6]
        resultado = lc.moduloC(a)
        self.assertAlmostEqual(resultado, 7.211102551, places=4)
        self.assertNotAlmostEqual(resultado, 7.211212551, places=4) 
    
    def test_modulo2(self):
        # a = 4 + 3i
        # |(a1,a2)| = sqrt(a1**2 + a2**2)
        # Resultado esperado: 5 

        a = [4, 3]
        resultado = lc.moduloC(a)
        self.assertEqual(5, resultado) 
        self.assertNotEqual(5.001, resultado)  

    def test_conjugado1(self):
        # a = 3 - 9i
        # (a1,a2) = a1 + (-1* a2)
        # Resultado esperado: 3 + 9i 
        
        a = [3,-9]
        resultado = lc.conjugadoC(a)
        self.assertEqual((3,9), resultado) 
        self.assertNotEqual((3, -9), resultado)
    
    def test_conjugado2(self):
        # a = 2i
        # (a1,a2) = a1 + (-1* a2)
        # Resultado esperado: 3 + 9i 
        
        a = [0,2]
        resultado = lc.conjugadoC(a)
        self.assertEqual((0,-2), resultado) 
        self.assertNotEqual((0, 2), resultado)
    
    def test_fase1(self):
        # Número complejo: 1 + 1i
        # Resultado esperado: π/4
        
        a = (1, 1)
        resultado = lc.faseC(a)
        esperado = math.pi / 4 
        self.assertAlmostEqual(esperado, resultado, places=9)

    def test_fase2(self):
        # Número complejo: -1 - 1i
        # Resultado esperado: -3π/4

        a = (-1, -1)
        resultado = lc.faseC(a)
        esperado = -3 * math.pi / 4 
        self.assertAlmostEqual(esperado, resultado, places=9)
    
    def test_cartesianoPolar1(self):
        # Número complejo en coordenadas cartesianas: 1 + i
        # (a1,a2) = (√(a1**2)+(a2**2), arcotan(a2/a1))
        # Resultado esperado: (√2,π/4)
        a = (1, 1)
        resultado = lc.convertCartesianoPolarC(a)
        esperado = (math.sqrt(2), math.pi / 4)  
        self.assertAlmostEqual(esperado[0], resultado[0], places=9)
        self.assertAlmostEqual(esperado[1], resultado[1], places=9)

    def test_cartesianoPolar2(self):
        # Número complejo en coordenadas cartesianas: -1 - i
        # (a1,a2) = (√(a1**2)+(a2**2), arcotan(a2/a1))
        # Resultado esperado: (√2,-3π/4)
        a = (-1, -1)
        resultado = lc.convertCartesianoPolarC(a)
        esperado = (math.sqrt(2), -3 * math.pi / 4)  
        self.assertAlmostEqual(esperado[0], resultado[0], places=9)
        self.assertAlmostEqual(esperado[1], resultado[1], places=9)

    def test_polarCartesiano1(self):
        #Número complejo en coordenadas polares: (√2, π/4) 
        # (a1,a2) = (a1*cos(a2), a1*sin(a2))
        # Resultado esperado: 1 + i

        a = (math.sqrt(2), math.pi / 4)
        resultado = lc.convertPolarCartesianoC(a)
        esperado = (1, 1) 
        self.assertAlmostEqual(esperado[0], resultado[0], places=9)
        self.assertAlmostEqual(esperado[1], resultado[1], places=9)

    def test_polarCartesiano2(self):
        #Número complejo en coordenadas polares: (2, π/2)
        # (a1,a2) = (a1*cos(a2), a1*sin(a2))
        # Resultado esperado: 2i

        a = (2, math.pi / 2)
        resultado = lc.convertPolarCartesianoC(a)
        esperado = (0, 2) 
        self.assertAlmostEqual(esperado[0], resultado[0], places=9)
        self.assertAlmostEqual(esperado[1], resultado[1], places=9)

if __name__ == '__main__':
    unittest.main()

