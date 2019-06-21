def pendiente(x1, y1, x2, y2):
   m1 = float(y2 - y1)
   m2 = float(x2 - x1)
   m = (m1 / m2)
   return m

def intercepto(x, y, m):
   b = float(y - (m * x))
   return b

def linea(x1, y1, x2, y2, matriz):
   if x1 == x2:
       for y in range(y1, y2 + 1):
           matriz[y][x1] = "X"
       return matriz
   elif x2 > x1:
       z = pendiente(x1, y1, x2, y2)
       b = intercepto(x1, y1, z)
       for x in range(x1, x2 + 1):
           y = int(z * x + b)
           matriz[y][x] = "X"
       return matriz
   elif x2 < x1:
       z = pendiente(x1, y1, x2, y2)
       b = intercepto(x1, y1, z)
       for x in range(x2, x1 + 1):
           y = int(z * x + b)
           matriz[y][x] = "X"
       return matriz

def triangulo(x1, y1, base, altura, matriz):
   for i in range(base):
       matriz[y1][x1 + i] = "X"
   x2 = x1 + int(base / 2)
   y2 = y1 + altura
   linea(x1, y1, x2, y2, matriz)
   x3 = x1 + base
   y3 = y1
   linea(x2, y2, x3, y3, matriz)
   return matriz

def rectangulo(x1, y1, base, altura, matriz):
   x2 = x1 + base
   y2 = y1
   linea(x1, y1, x2, y2, matriz)
   x3 = x2
   y3 = y2 + altura
   linea(x2, y2, x3, y3, matriz)
   x4 = x1
   y4 = y3
   linea(x3, y3, x4, y4, matriz)
   linea(x1, y1, x4, y4, matriz)
