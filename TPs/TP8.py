## MNUM - 4/12/2020


# RK4

# Função que dá valor da solução 
def df(x,y):
    return x**2

# Função da solução particular para ponto (0, 1)
def sp(x,y):
    return x**3/3 + 1

def runga_kuta_4ordem(x0,y0,xf,n):
    x = x0
    y = y0
    h = (xf-x0)/n
        
    for i in range(n):
       d1 = df(x, y)*h              # Delta y = incremento em y
       d2 = df(x+h/2, y+d1/2)*h
       d3 = df(x+h/2, y+d2/2)*h
       d4 = df(x+h, y+d3)*h
       
       dy = d1/6.0 + d2/3.0 + d3/3.0 + d4/6.0
       
       y = y + dy
       x = x + h
    
    print("x:",x, "y:", y, "erro:", abs(y-sp(x,y)))
    
    
# runga_kuta_4ordem(0,1,5,10)
# x: 5.0 y: 42.666666666666664 erro: 0.0 


# runga_kuta_4ordem(0,1,5,20)
# x: 5.0 y: 42.666666666666664 erro: 0.0
    
    
# runga_kuta_4ordem(0,1,5,1)
# x: 5.0 y: 42.666666666666664 erro: 0.0   
    
    
# ---------------------------------------------------    
  
# Sistemas de Equações Diferenciais Ordinárias   
    
# z' = dz/dx = f1(x,y,z)
# y' = dy/dx = f2(x,y,z)
    
# EXERCÍCIO    
# z' = x + y + z
# y' = 2x - y - z
# (0,1,1)           h = 0.5   
# x pertence [0,5]    
    
# Usando RK2 em 3d
    
 
def df_(x,y,z):
    return 2*x-y-z

def dg(x,y,z):
    return x+y+z
    
def runga_kuta_2ordem_3d(x0,y0,z0,xf,n):
    x = x0
    y = y0
    z = z0
    h = (xf-x0)/n
        
    for i in range(n):
       dy = df_(x + h/2, y + df_(x,y,z)*(h/2), z + dg(x,y,z)*(h/2))*h
       dz = dg(x + h/2, y + df_(x,y,z)*(h/2), z + dg(x,y,z)*(h/2))*h
       y = y + dy
       x = x + h
       z = z + dz
        
    
    print("x:",x, "y:", y, "z:", z)
 
    
# runga_kuta_2ordem_3d(0,1,1,5,10)
# x: 5.0 y: -45.875 z: 85.375
    
    
# ---------------------------------------------------

# Otimização

# EXERCÍCIO:
# min(x^4)
    
def f(x):
    return x**4
    
def min_algoritmo(x0, h):
    
    ymin = f(x0)
    xmin = x0
    
    while(f(xmin+h) < ymin):
        ymin = f(xmin+h)
        xmin += h
     
    while(f(xmin-h) < ymin):
        ymin = f(xmin-h)
        xmin -= h
        
        
    print("xmin:", xmin, "ymin:", ymin, "intervalo: [", xmin-h, ",", xmin+h, "]")

    # Método por redução intervalar por terços    
    # reduzir intervalo em 3 e eliminar a porção de intervalo inválida
    # ...
    
    p1 = xmin-h
    p2 = ((xmin-h) +  (xmin+h))/3
    p3 = xmin
    p4 = xmin+h
    
    # ...
    
    if(f(p2) > f(p3)):
        p1 = p2
    else:
        p4 = p3
        
        
        
    
    





    
    
    