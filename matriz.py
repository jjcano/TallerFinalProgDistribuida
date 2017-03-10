# -*- coding: utf-8 -*-
import random

class Matriz(object):
    def __init__(self, filas=None, columnas=None):

        if filas:

            self.filas =filas

        else:

            self.filas=int(raw_input(" Ingrese número de filas: "))

        if columnas:

            self.columnas = columnas

        else:

            self.columnas = int(raw_input(" Ingrese número de columnas: "))


    def CrearMatriz(self):

      self.matriz=[]

      for f in range(self.filas):
          self.matriz.append([0]*self.columnas)

    def LlenarMatriz(self):

        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = random.randint(-10, 10)

    def FillM(self):

        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = int(raw_input("ingrese %d,%d: " % (f, c)))

    def PrintM(self):

        print self.matriz

    def DatosM(self):

        return self.matriz

    def valida_m(self, ColsA, FilasB):
        
        if ColsA != FilasB:
            print "No se puede realizar esta operación"
            exit()

    def MulMatriz(self, matrizA, matrizB, filaB):
        
        for f in range(self.filas):
            for c in range(self.columnas):
                for k in range(filaB):
                    self.matriz[f][c]+=matrizA[f][k] * matrizB[k][c]

    def Multi(self, NR):
        
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = self.matriz[f][c] * NR

    def ValidarM(self, FilasA, ColsA, FilasB, ColsB):
        
        if (ColsA != ColsB) or (FilasA != FilasB):
            print "Las Matrices deben ser de igual Tamaño"


    def SumarM(self, matrizA, matrizB):
        
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = matrizA[f][c] + matrizB[f][c]

    def RestaM(self, matrizA, matrizB):
        
        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = matrizA[f][c] - matrizB[f][c]

    def Copiar(self,m):
        
        self.result = []
        for f in m:
            self.result.append(f[:])
        return self.result

    def Combinar(self, m, i, j, e):
        
        n = len(m)
        for c in range(n):
            m[j][c] = m[j][c] + e * m[i][c]

    def ChangeRow(self, m, i, j):

        m[i], m[j] = m[j], m[i]

    def MultRows(self, m, f, e):

        n = len(m)
        for c in range(n):
            m[f][c] = m[f][c] * e

    def FirstNulo(self,m, i):

        result = i
        while result < len(m) and m[result][i] == 0:
            result = result + 1
        return result

    def determinante(self, matr):

        m = self.Copiar(matr)
        n = len(m)
        det = 1
        for i in range(n):
            j = self.FirstNulo(m, i)
            if j == n:
                return 0
            if i != j:
                det = -1 * det
                self.ChangeRow(m, i, j)
            det = det * m[i][i]
            self.MultRows(m, i, 1. / m[i][i])
            for k in range(i + 1, n):
                self.Combinar(m, i, k, -m[k][i])
        print int(det)

    def Square(self):
        if self.filas == self.columnas:
            return True
        else:
            return False

    def Transp(self,mA):

        for f in range(self.filas):
            for c in range(self.columnas):
                self.matriz[f][c] = mA[c][f]

    def Simet(self):
        band = True
        for f in range(self.filas):
            for c in range(self.columnas):
                if (self.matriz[f][c] != self.matriz[c][f]):
                    band = False
                    break
        if (band):
            print"La Matriz es Simétrica"
        else:
            print"La Matriz No es Simétrica"

    def Ident(self):
        for f in range(self.filas):
            self.matriz[f][f] = 1

    def Multiplicar(self,matriz1, matriz2,fila):
        res = []
        for f in range(fila):
            res.append([0] * fila)

        for i, row in enumerate(res):
            for j in range(0, len(row)):
                for k in range(0, len(row)):
                    res[i][j] += matriz1[i][k] * matriz2[k][j]
        return res

    def Exponente(self, pow):

        powerhash = {}
        if pow in powerhash.keys():
           return powerhash[pow]
        if pow == 1:
            return self.matriz
        if pow == 2:
            powerhash[pow] = self.Multiplicar(self.matriz, self.matriz,self.filas)
            return powerhash[pow]
        if pow % 2 == 0:
            powerhash[pow] = self.Multiplicar(self.Exponente(pow / 2), self.Exponente(pow / 2),self.filas)
        else:
            powerhash[pow / 2 + 1] = self.Multiplicar(self.Exponente(pow / 2), self.matriz,self.filas)
            powerhash[pow] = self.Multiplicar(self.Exponente(pow / 2), powerhash[pow / 2 + 1],self.filas)
        return powerhash[pow]

    def TransMatriz(self,m):

        t = []
        for r in range(len(m)):
            tRow = []
            for c in range(len(m[r])):
                if c == r:
                    tRow.append(m[r][c])
                else:
                    tRow.append(m[c][r])
            t.append(tRow)
        return t

    def ObtenerMatMenor(self,m, i, j):

        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def ObtenerMatrizDet(self,m):

        # base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * self.ObtenerMatrizDet(self.ObtenerMatMenor(m, 0, c))
        return determinant

    def ObtenerMInv(self,m):

        determinant = float(self.ObtenerMatrizDet(m))
        # special case for 2x2 matrix:
        if (determinant != 0):
            if len(m) == 2:
                return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                        [-1 * m[1][0] / determinant, m[0][0] / determinant]]

            # find matrix of cofactors
            cofactors = []
            for r in range(len(m)):
                cofactorRow = []
                for c in range(len(m)):
                    minor = self.ObtenerMatMenor(m, r, c)
                    cofactorRow.append(((-1) ** (r + c)) * float(self.ObtenerMatrizDet(minor)))
                cofactors.append(cofactorRow)
            cofactors = self.TransMatriz(cofactors)
            for r in range(len(cofactors)):
                for c in range(len(cofactors)):
                    cofactors[r][c] = round(float(cofactors[r][c] / determinant),2)
            return cofactors
        else:
            print "No Permitido"