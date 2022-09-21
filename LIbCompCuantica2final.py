import math
import LibComputacionCuantica
import numpy as np
Complex_1 = (5, 2) # Variable para los casos Prueba
Complex_2 = (6, 3) # Variable para los casos Prueba
Vect_1 = [(5, 2), (2, 5)]
Vect_2 = [(6, 7), (8, 9)]
mat_1 = [[(5, 1), (0, 2), (5, 1)], [(1, 1), (4, 2), (5, 1)]]
mat_2 = [[(0, 0), (1, 5), (1, 1)], [(2, 0), (10, 0), (1, 1)]]
#Funciones adicionales
def InversoAdd(a):
    """"
    Permite conseguir el inverso aditivo de un complejo.
    (tuple) -> Tuple
    """
    negative_real = -a[0]
    negative_complex = -a[1]
    return (negative_real, negative_complex)
def ConjComplex(a):
    """"
    Permite conseguir el conjugado de un complejo.
    (tuple) -> Tuple
    """
    return(a[0],-a[1])
def goodprinting(a):
    """"
    Permite imprimir mejor las matrices y vectores
    """
    for i in range(len(a)):
        print((a[i]), "\n")
#Funciones pedidas
def SumVect(a, b):
    """"
    Permite sumar dos vectores complejos
    (tuple, tuple) -> Tuple
    """
    new_vect = []
    for i in range(len(a)):
        new_vect.append(LibComputacionCuantica.SumComplex(a[i], b[i]))
    return new_vect
#print(SumVect(Vect_1, Vect_2))
def InvAddVect(vect):
    """"
    Permite conseguir el inverso aditivo de un vector complejo.
    (tuple) -> Tuple
    """
    for i in range(len(vect)):
        vect[i] = InversoAdd(vect[i])
    return vect
#print(InvAddVect(Vect_1))
def EscProdVect(a, b):
    """"
    Permite conseguir el producto de un escalar por un vector complejo.
    list 1D) -> List 1D
    """
    new_vect = []
    for i in range(len(b)):
        new_vect.append(LibComputacionCuantica.ProductComplex(a, b[i]))
    return new_vect
#print(EscProdVect((3,2),Vect_1))
def SumMat(a,b):
    """"
    Permite sumar dos matrices complejas.
    (list 2D, list 2D ) -> LIST 2D
    """
    new_mat = [[] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            new_mat[i].append(LibComputacionCuantica.SumComplex(a[i][j], b[i][j]))
    return new_mat
#goodprinting(SumMat(mat_1, mat_2))
def InvMat(a):
    """"
    Permite conseguir el inverso aditivo de una matriz compleja
    (list 2D) -> LIST 2D
    """
    for i in range(len(a)):
        a[i] = InvAddVect(a[i])
    return a
#goodprinting(InvMat(mat_1))
def EscProdMat(a, b):
    """"
    Permite conseguir el producto escalar por una matriz compleja
    (list 2D) -> LIST 2D
    """
    for i in range(len(b)):
        b[i] = EscProdVect(a, b[i])
    return b
#goodprinting(EscProdMat((0,0), mat_2))
def TransVectMat(a):
    """"
    Permite conseguir la trasnpuesta de una matriz o un vector complejo.
    (list 2D) -> LIST 2D
    """
    len_mat = len(a)
    if len_mat == len(a[0]):
        new_mat = [[] for i in range(len_mat)]
        for i in range(len_mat):
            for j in range(len(a[i])):
                new_mat[i].append(a[j][i])
        return new_mat
    else:
        new_mat = [[] for i in range(len(a[0]))]
        for i in range(len(a[0])):
            for j in range(len_mat):
                new_mat[i].append(a[j][i])
        return new_mat
#goodprinting(TransVectMat(mat_2))
def ConjMatVect(a):
    """"
    Permite conseguir la conjugada de una matriz o un vector complejo.
    (list 2D) -> LIST 2D
    """
    len_a = len(a)
    if type(a[0]) == tuple:
        for i in range(len_a):
            a[i] = ConjComplex(a[i])
        return a
    for i in range(len_a):
        for j in range(len(a[i])):
            a[i][j] = ConjComplex(a[i][j])
    return a
#goodprinting(ConjMatVect(mat_1))
def AdjMatVect(a):
    """"
    Permite conseguir la adjunta de una matriz o un vector complejo.
    (list 2D) -> LIST 2D
    """
    a = TransVectMat(a)
    return ConjMatVect(a)
#goodprinting(AdjMatVect(mat_2))
def ProdMat(a,b):
    """"
    Permite conseguir el producto entre dos matrices complejas
    Tambien nos permite conocer la accion de una matriz sobre un vector.
    (list 2D, list 2D) -> LIST 2D
    """
    f_1, r_1 = len(a), len(a[0])
    f_2, r_2 = len(b), len(b[0])
    if r_1 == f_2:
        prod_mat = [[(0, 0) for i in range(r_2)] for i in range(f_1)]
        for i in range(f_1):
            for j in range(r_2):
                for k in range(r_1):
                    multi = (LibComputacionCuantica.ProductComplex(a[i][k], b[k][j]))
                    prod_mat[i][j] = LibComputacionCuantica.SumComplex(prod_mat[i][j], multi)
        return prod_mat
    return False
#goodprinting(ProdMat([[(1,1), (1,1)], [(1,1), (1,1)]], [[(1,1)], [(1,1)]]))
def InnVectProd(a, b):
    """"
     Permite conseguir el producto interno entre dos vectores complejos.
     (list 1D, list 1D) -> tuple
     """
    inner_prod = (0,0)
    for i in range(len(a)):
        multi = LibComputacionCuantica.ProductComplex(ConjComplex(a[i]),b[i])
        inner_prod = LibComputacionCuantica.SumComplex(inner_prod,multi)
    return inner_prod
#print(InnVectProd(Vect_1,Vect_2))
def VecNorm(a):
    """"
     Permite conseguir la norma de un vector complejo.
     (list 1D) -> float
     """
    res_1 = InnVectProd(a, a)
    return math.sqrt(res_1[0])
#print(VecNorm(Vect_1))

def DistanceVect(a,b):
    """"
    Permite conseguir la distancia entre dos vectores complejos.
    (list 1D, list 1D) -> float
    """
    new_vect = []
    for i in range(len(a)):
        new_vect.append(LibComputacionCuantica.SubComplex(a[i],b[i]))
    return VecNorm(new_vect)
#print(DistanceVect(Vect_1,Vect_2))
def MatUnitComp(a):
    f_1 = len(a)
    r_1 = len(a[0])
    if f_1 != r_1:
        return False
    b = ConjMatVect(a)
    result_mat = ProdMat(a, b)
    for i in range(f_1):
        for j in range(r_1):
            if i == j and b[i][j] != (1, 0):
                return False
            elif i != j and b[i][j] != (0, 0):
                return False
    return True
#print(MatUnitComp([[(1, 0), (0, 0)], [(0, 0), (1, 0)]]))
def Hermitian(a):
    if len(a) != len(a[0]):
        return False
    a = np.array(a)
    a_adjunt = np.array(AdjMatVect(a))
    return np.array_equal(a, a_conj)
#print(Hermitian([[(1, 0), (1, 0)], [(1, 0), (-1, 0)]]))
def ProdTensor(a, b):
    if type(a[0]) != tuple:
        f_1, r_1 = len(a), len(a[0])
    else:
        f_1, r_1 = len(a), 1
    if type(b[0]) != tuple:
        f_2, r_2 = len(b), len(b[0])
    else:
        f_2, r_2 = len(b), 1
    mat_tens = [[(0,0) for i in range(r_1 * r_2)] for i in range(f_1 * f_2)]
        #for i in range(f_1):
            #for j in range(r_2):
                #mat_tens[j][i]
    return mat_tens
def ProdTensor2(a, b):
    final_matrix = []
    aux_matrix = []
    count = len(b)
    for element_a in a:
        counter = 0
        check = 0
        while check < count:
            if type(b[0]) != tuple:
                for num_a in element_a:
                    for num_b in b[counter]:
                        aux_matrix.append(LibComputacionCuantica.ProductComplex(num_a, num_b))
            else:
                for num_b in b:
                    for num_a in element_a:
                        aux_matrix.append(LibComputacionCuantica.ProductComplex(num_a, num_b))
            counter += 1
            final_matrix.append(aux_matrix)
            aux_matrix = []
            check += 1
    return final_matrix
#goodprinting(ProdTensor2([[(1,2), (2,1)],[(1,2),(0,2)], [(1, 2), (2, 0)]], [[(1,1), (2,1)], [(1,1), (0,0)]]))
