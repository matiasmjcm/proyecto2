import modulos
print ("MENÚ: \n\
1. Agregar una línea \n\
2. Agregar un elipse o círculo \n\
3. Agregar un rectángulo o cuadrado \n\
4. Agreagar un triángulo \n\
5. Mostrar un dibujo \n\
6. Leer un dibujo \n\
7. Grabar un dibujo \n\
\n\
0. Salir del programa\n")

ejey = 42
ejex = 82
matriz = []
for y in range(ejey):
    l = []
    for x in range(ejex):
        if y == 0 or y == ejey - 1 or x == 0 or x == ejex - 1:
            l.append(".")
        else:
            l.append(" ")
    matriz.append(l)

terminar = False
while not terminar:
    menu = input("=> SELECCIONE OPCIÓN: ")
    if menu == "0":
        print("   *ADIÓS! NOS VEMOS PRONTO.")
        terminar = True
    elif menu == "1":
        print(" - Siga las instrucciones y coloque las coordanadas de la línea a crear: \n\
 • Las coordenadas deben estar dentro del primer cuadrante del plano cartesiano\n\
 • Xmax = 82 ^ Ymax = 42")
        terminado = False
        while not terminado:
            x1 = int(input("   => Ingrese X1: "))
            y1 = int(input("   => Ingrese Y1: "))
            x2 = int(input("   => Ingrese X2: "))
            y2 = int(input("   => Ingrese Y2: "))
            if x1 >= 1 and x1 <= 81 and x2 >= 1 and x2 <= 81 and y1 >= 1 and y1 <= 41 and y2 >= 1 and y2 <= 41:
                modulos.linea(x1, y1, x2, y2, matriz)
                print("   *RECTA CREADA!")
                terminado = True
            else:
                print("   *Siga las instrucciones.")
    elif menu == "3":
        print(" - Siga las instrucciones y coloque la coordenada del punto inferior izquierdo, seguido de la base y la altura de su rectángulo: \n\
 • Si coloca las coordenadas indicadas, puede salir como resultado un cuadrado\n\
 • Las coordenadas deben estar dentro del primer cuadrante del plano cartesiano\n\
 • Xmax = 82 ^ Ymax = 42")
        terminado = False
        while not terminado:
            x1 = int(input("   => Ingrese X: "))
            y1 = int(input("   => Ingrese Y: "))
            base = int(input("   => Ingrese la base de su rectángulo: "))
            altura = int(input("   => Ingrese la altura de su rectángulo: "))
            if x1 >= 1 and x1 <= 81 and y1 >= 1 and y1 <= 41:
                modulos.rectangulo(x1, y1, base, altura, matriz)
                print("   *RECTÁNGULO CREADO!")
                terminado = True
            else:
                print("   *Siga las instrucciones.")
    elif menu == "4":
       print(" - Siga las instrucciones y coloque la coordenada del punto inferior izquierdo, seguido de la base y la altura de su triángulo: \n\
 • Las coordenadas deben estar dentro del primer cuadrante del plano cartesiano\n\
 • Xmax = 82 ^ Ymax = 42")
       terminado = False
       while not terminado:
           x1 = int(input("   => Ingrese X: "))
           y1 = int(input("   => Ingrese Y: "))
           base = int(input("   => Ingrese la base de su triángulo: "))
           altura = int(input("   => Ingrese la altura de su triángulo: "))
           if x1 >= 1 and x1 <= 81 and y1 >= 1 and y1 <= 41:
               modulos.triangulo(x1, y1, base, altura, matriz)
               print("   *TRIÁNGULO CREADO!")
               terminado = True
           else:
               print("   *Siga las instrucciones.")
    elif menu == "5":
        for y in range(ejey):
            for x in range(ejex):
                print(matriz[ejey - 1 - y][x], end=" ")
            print()
    elif menu == "6":
        lectura = open("Dibujo.txt", "r")
        for item, i in enumerate(lectura):
            for caracter, j in enumerate(i):
                matriz[item][caracter]
        lectura.close()
        print("   *DIBUJO LEIDO.")
    elif menu == "7":
        archivo = open(" Dibujo.txt", "w")
        for i in matriz:
            for j in i:
                archivo.write(j)
            archivo.write("\n")
        archivo.close()
        print("   *DIBUJO GRABADO.")
