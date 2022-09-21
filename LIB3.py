import LIbCompCuantica2final
def goodprinting(a):
    """"
    Permite imprimir mejor las matrices y vectores
    """
    for i in range(len(a)):
        print((a[i]), "\n")
def SumComplex(a,b):
    '''
    Esta funcion permite sumar dos numeros complejos.
    (Tuple, Tuple) -> Tuple
    '''
    Sum_RealPart = a[0] + b[0]
    Sum_ComplexPart = a[1] + b[1]
    return (Sum_RealPart,Sum_ComplexPart)

def accionMatrizVector(matriz, vector):
    vector_resultante = []
    for i in range(len(vector)):
        vector_resultante.append(0)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            vector_resultante[i] += matriz[i][j]*vector[j]
    return vector_resultante
def canicas_1(mat, vect, cantidad):
    for i in range(cantidad):
        res = accionMatrizVector(mat, vect)
    return res
#print(canicas_1([[1,0,0,0],[0,0,0,0], [0,0,1,0]], [1,0,0,0], 2))
#Funcion 2
def multiplesRendijas(matriz, estado):
    matriz_transpuesta = LIbCompCuantica2final.TransVectMat(matriz)
    #print(goodprinting(matriz_transpuesta))
    for i in range(len(matriz_transpuesta)):
        if sum(matriz_transpuesta[i]) != 1:
            estocastica = False
            break
        else:
            estocastica = True
    if estocastica == True:
        res = list(map(float, canicas_1(matriz, estado, 1)))
        return res
    else:
        return False
#matriz = [[1/3,0,0],[1/3,0,1],[1/3,1,0]]
#estado = [1,0,0]
#print(multiplesRendijas(matriz, estado))
def clicksCuantico(matriz, estado, cantidadClicks):
    for i in range(cantidadClicks):
        estado_nuevo = LIbCompCuantica2final.ProdMat(matriz, estado)
    return estado_nuevo
def multiplesRendijasCuantico(matriz, estado):
    matriz_transpuesta = LIbCompCuantica2final.TransVectMat(matriz)
    #print(matriz_transpuesta)
    for i in range(0, len(matriz_transpuesta)):
        if SumComplex(matriz_transpuesta[i], matriz_transpuesta[i+1]) != (0,1):
            estocastica = False
            break
        else:
            estocastica = True
    if estocastica == True:
        res = clicksCuantico(matriz, estado, 2)
        return res
    else:
        return "False"
#matriz = [[(0,1),(0,0)],[(0,0),(0,1)]]
#vector = [(0,1),(0,0)]
#print(multiplesRendijasCuantico(matriz,vector))