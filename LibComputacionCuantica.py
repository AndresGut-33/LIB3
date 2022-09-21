import math
Complex_1 = (5,2) # Variable para los casos Prueba
Complex_2 = (6,3) # Variable para los casos Prueba
def SumComplex(a,b):
    '''
    Esta funcion permite sumar dos numeros complejos.
    (Tuple, Tuple) -> Tuple
    '''
    Sum_RealPart = a[0] + b[0]
    Sum_ComplexPart = a[1] + b[1]
    return (Sum_RealPart,Sum_ComplexPart)

#print("La suma de los numeros complejos", str(Complex_1[0]), "+" , str(Complex_1[1]) + "i", \
#"y", str(Complex_2[0]) ,"+", str(Complex_2[1]) + "i" , "es igual a" , "=", SumComplex(Complex_1,Complex_2))

def ProductComplex(a,b):
    '''
    Esta funcion permite multiplicar dos numeros complejos.
    (Tuple, Tuple) -> Tuple
    '''
    Product_RealPart = (a[0] * b[0]) - (a[1] * b[1])
    Product_ComplexPart = (a[0] * b[1]) + (a[1] * b[0])
    return (Product_RealPart,Product_ComplexPart)
#print("El producto de los numeros complejos", str(Complex_1[0]), "+" , str(Complex_1[1]) + "i", \
#"y", str(Complex_2[0]) ,"+", str(Complex_2[1]) + "i" , "es igual a" , "=", ProductComplex(Complex_1,Complex_2))

def SubComplex(a,b):
    '''
    Esta funcion permite restar dos numeros complejos.
    (Tuple, Tuple) -> Tuple
    '''
    Sub_RealPart = a[0] - b[0]
    Sub_ComplexPart = a[1] - b[1]
    return (Sub_RealPart, Sub_ComplexPart)

#print("La resta de los numeros complejos", str(Complex_1[0]), "+" , str(Complex_1[1]) + "i", \
#"y", str(Complex_2[0]) ,"+", str(Complex_2[1]) + "i" , "es igual a" , "=", SubComplex(Complex_1,Complex_2))


def DivComplex(a,b):
    '''
    Esta funcion permite multiplicar dos numeros complejos.
    (Tuple, Tuple) -> Tuple
    '''
    Denominator_Div =(a[1] ** 2) + (b[1] ** 2)
    Div_RealPart = (a[0] * a[1]) + (b[0] * b[1]) / Denominator_Div
    Div_ComplexPart = (a[1] * b[0]) - (a[0] * b[1]) / Denominator_Div
    return (Div_RealPart,Div_ComplexPart)

#print("La división de los numeros complejos", str(Complex_1[0]), "+" , str(Complex_1[1]) + "i", \
#"y", str(Complex_2[0]) ,"+", str(Complex_2[1]) + "i" , "es igual a" , "=", DivComplex(Complex_1,Complex_2))

def MoDComplex(a):
    '''
    Esta funcion permite obtener el modulo de un número complejo.
    (Tuple) -> Float
    '''
    Mod_Com = math.sqrt((a[0] ** 2) + (a[1] ** 2))
    return Mod_Com

#print("El modulo del numero complejo " + str(Complex_1[0]), "+" , str(Complex_1[1]) + "i" + " es = " +\
    #" " + str(MoDComplex(Complex_1)))

def ConjComplex(a):
    '''
    Esta funcion permite obtener el conjugado de un número complejo.
    (Tuple) -> tuple
    '''
    Conj_part = -(a[1])
    return (a[0],Conj_part)

#print("El conjugado del complejo", str(Complex_1[0]), "+" , str(Complex_1[1]) + "i", \
      #"es = " + str(ConjComplex(Complex_1)))

def ComplexPhase(a):
    '''
    Esta funcion permite obtener la fase de un número complejo.
    (Tuple) -> Real
    '''
    Phase_Com = math.atan2(a[1],a[0])
    return Phase_Com
#print("La fase del complejo", str(Complex_1[0]), "+" , str(Complex_1[1]) + "i", \
      #"es = " + str(ComplexPhase(Complex_1)))

def PolarComplex(a):
    '''
    Esta funcion permite obtener la representacion polar de un complejo.
    (Tuple) -> tuple
    '''
    Theta = ComplexPhase(a)
    Rho = MoDComplex(a)
    return (Rho, Theta)

#print("La representacion polar del complejo", str(Complex_1[0]), "+" , str(Complex_1[1]) + "i", \
      #"es = " + str(PolarComplex(Complex_1)))


