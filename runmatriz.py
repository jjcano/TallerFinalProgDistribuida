# -*- coding: utf-8 -*-
import matriz

def main():
    op = " "

    while op != "s" and op != "S":
        print"------------------------------------------"
        print("\t\tCALCULADORA DE MATRICES\t\t")
        print("(a). Determinante ")
        print("(b). Transpuesta ")
        print("(c). Inversa ")
        print("(d). Multiplicar por un Número la Matriz")
        print("(e). Matriz Elevada a Una Potencia ")
        print("(f). Matriz Simétrica ")
        print("(g). Matriz Identidad ")
        print "-----------------------------"
        print "Operaciones con Dos Matrices:"
        print("(h). A * B")
        print("(i). A - B")
        print("(j). A + B")
        print("(s). Salir")

        op = raw_input("Digite una Opción: ")

        if op == "a" or op == "A":

            matrizA 	= matriz.Matriz()
            matrizA.CrearMatriz()
            Validacion	=	matrizA.Square()

            if Validacion:

                print "1. Matriz Manual"
                print "2. Matriz Automática"
                Select = raw_input("Seleccione Matriz: ")

                if Select == "1":

                    matrizA.FillM()

                else:

                    matrizA.LlenarMatriz()

                print "Matriz Creada: "

                matrizA.PrintM()

                print "El Determinante de la Matriz es: "
                print matrizA.ObtenerMatrizDet(matrizA.DatosM())

            else:

                print "La Matriz Debe Ser Cuadrada"

        elif op == "b" or op == "B":

            matrizA = matriz.Matriz()
            matrizA.CrearMatriz()
            matrizA.LlenarMatriz()
            matrizA.PrintM()
            matrizC = matriz.Matriz(matrizA.columnas, matrizA.filas)
            matrizC.CrearMatriz()
            matrizC.Transp(matrizA.DatosM())
            matrizC.PrintM()

        elif op == "c" or op == "C":

            matrizA = matriz.Matriz()
            matrizA.CrearMatriz()
            matrizA.LlenarMatriz()
            matrizA.PrintM()
            print matrizA.ObtenerMInv(matrizA.DatosM())

        elif op == "d" or op == "D":

            matrizA = matriz.Matriz()
            matrizA.CrearMatriz()
            matrizA.LlenarMatriz()
            print "matriz:"
            matrizA.PrintM()
            Valor = int(raw_input('Ingrese número por el que se multiplicara la matriz: \n'))
            matrizA.Multi(Valor)
            matrizA.PrintM()

        elif op == "E" or op == "e":

            matrizA = matriz.Matriz()
            matrizA.CrearMatriz()
            matrizA.LlenarMatriz()
            matrizA.PrintM()
            Potencia = int(raw_input("Ingrese Potencia: "))
            print matrizA.Exponente(Potencia)

        elif op == "f" or op == "F":

            matrizA = matriz.Matriz()
            matrizA.CrearMatriz()
            matrizA.FillM()
            matrizA.PrintM()
            matrizA.Simet()

        elif op == "g" or op == "G":

            matrizA = matriz.Matriz()
            matrizA.CrearMatriz()
            matrizA.Ident()
            matrizA.PrintM()

        elif op == "h" or op == "H":

            matrizA = matriz.Matriz()
            matrizA.CrearMatriz()
            matrizA.LlenarMatriz()
            matrizA.PrintM()
            matrizB = matriz.Matriz()
            matrizB.CrearMatriz()
            matrizB.LlenarMatriz()
            matrizB.PrintM()

            matrizC = matriz.Matriz(matrizA.filas, matrizB.columnas)
            matrizC.CrearMatriz()
            matrizC.MulMatriz(matrizA.DatosM(),matrizB.DatosM(),matrizB.filas)
            matrizC.PrintM()

        elif op == "i" or op == "I":

            matrizA = matriz.Matriz()
            matrizA.CrearMatriz()
            matrizA.LlenarMatriz()
            matrizA.PrintM()

            matrizB = matriz.Matriz()
            matrizB.CrearMatriz()
            matrizB.LlenarMatriz()
            matrizB.PrintM()

            matrizB.ValidarM(matrizA.filas, matrizA.columnas, matrizB.filas, matrizB.columnas)
            matrizC = matriz.Matriz(matrizA.filas, matrizB.columnas)
            matrizC.CrearMatriz()
            matrizC.SumarM(matrizA.DatosM(), matrizB.DatosM())
            matrizC.PrintM()

        elif op == "j" or op == "J":

            matrizA = matriz.Matriz()
            matrizA.CrearMatriz()
            matrizA.LlenarMatriz()
            matrizA.PrintM()

            matrizB = matriz.Matriz()
            matrizB.CrearMatriz()
            matrizB.LlenarMatriz()
            matrizB.PrintM()

            matrizB.ValidarM(matrizA.filas, matrizA.columnas, matrizB.filas, matrizB.columnas)
            matrizC = matriz.Matriz(matrizA.filas, matrizB.columnas)
            matrizC.CrearMatriz()
            matrizC.RestaM(matrizA.DatosM(), matrizB.DatosM())
            matrizC.PrintM()

        elif op == "S" or op == "s":
            print "Hasta Pronto."
            exit()
        else:
            print("Digite una Opción \n")


if __name__ == '__main__':
    main()