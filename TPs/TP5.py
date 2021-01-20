
# É preciso ver a convergência: se pivot é maior que o módulo da soma dos outros coeficientes

def metodoGaussSeidel(a1,b1,c1,i1,a2,b2,c2,i2,a3,b3,c3,i3, x, y, z):
    
    for i in range(20):
        x = (i1 - b1*y - c1*z)/a1
        y = (i2 - a2*x - c2*z)/b2
        z = (i3 - a3*x - b3*y)/c3
    
    print("x: ", x)
    print("y: ", y)
    print("z: ", z)
    
def metodoGaussJacobi(a1,b1,c1,i1,a2,b2,c2,i2,a3,b3,c3,i3, x, y, z):
    xant = x
    yant = y
    
    for i in range(20):
        x = (i1 - b1*y - c1*z)/a1
        y = (i2 - a2*xant - c2*z)/b2
        z = (i3 - a3*xant - b3*yant)/c3
        
        xant = x
        yant = y
    
    print("x: ", x)
    print("y: ", y)
    print("z: ", z)
    
    
# Metodo de gauss Jacobi conta com x, y, z anterior
# Metodo de gauss Seidel conta com x, y, z atuais (nova variante do método gauss-jacobi)
    
    
#------------------------------------------------------------------------------
# Método trapézio: (h/2)* (y0 + 2y1 + 2y2 + 2y3 + ... + yn)  -> 2 ordem
    
# Método de Simpson: (h/3) * (y0 + 4y1 + 2y2 + 4y3 + 2y4 + ... + yn)  -> 4 ordem
# - pontos y com índice par *2
# - pontos y com índice ímpar *4
    
# Exercício: integrate(x^4, 0, 10)
    
def f(x):
    return x**4    
    
def metodoTrapezio(a, b, n):
    area = 0
    h = abs(a-b)/ n
    
    for i in range(n):
        if (i == 0):
            area += f(a+i*h)
        else:
            area += 2*f(a+i*h)
    
    area += f(b)   
    area = area * (h/2)
    return area

def errorTrapezio(a,b,n):
    return abs(20000 - metodoTrapezio(0,10,10))
            
    
def metodoSimpson(a, b, n):
    area = 0
    h = abs(a-b)/ n
    
    for i in range(n):
        if (i == 0):
            area += f(a+i*h)
        elif (i % 2 == 0):
            area += 2*f(a+i*h)
        else:
            area += 4*f(a+i*h)
       
    area += f(b)   
    area = area * (h/3)
    return area
    
def errorSimpson(a,b,n):
    return abs(20000 - metodoSimpson(0,10,10))   


# Cálculo de erros:
    
#                   TRAP        |   SIMPSON
# n = 10 -> s = 20333.0         |   20001.3333
# n = 20 -> s'= 20083.3125      |  20000.083333333332
# n = 40 -> s''= 20020.83203125 | 20000.005208333332
    
# Qc = (s' - s)/ (s'' - s')
#               3.9962468290105 | 16.00249

# E'' = (s'' - s)/ 2^ordem-1
#               104.08          | 0.885
    
    
    
    
    


