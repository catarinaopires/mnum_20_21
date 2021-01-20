## MNUM - 11/12/2020

# f(x,y) = x^2+y^2

def f(x,y):
    return (x**2)+(y**2)

def dfdx(x,y):
    return 2*x

def dfdy(x,y):
    return 2*y 
    
def metodo_gradiente(x0, y0, h, n):

    x = x0
    y = y0

    for i in range(n):
        x1 = x - h * dfdx(x,y)
        y1 = y - h * dfdy(x,y)
        
        
        if(f(x1,y1) < f(x,y)):
            h*= 2
            x = x1
            y = y1
        else:
            h /= 2
        
        
    print("x:",x, "y:", y)   
    
    
def metodo_pesquisa_direçoes_coordenadas(x0, y0, h, n, k):
    
    x = x0
    y = y0

    for i in range(n):
        x1 = x - h * dfdx(x,k)
        y1 = y - h * dfdy(k,y)
        
        
        if(f(x1,y1) < f(x,y)):
            h*= 2
            x = x1
            y = y1
        else:
            h /= 2
        
        
    print("x:",x, "y:", y)
    
    
    ## TODO: ACABAR
    # + TECNICA DE AJUSTE QUÁDRICA