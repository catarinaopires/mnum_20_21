## MNUM - 27/11/2020

# Função que dá valor da solução 
def df(x,y):
    return x**2

# Função da solução particular para ponto (0, 1)
def sp(x,y):
    return x**3/3 + 1

def euler(x0,y0,xf,n):
    x = x0
    y = y0
    h = (xf-x0)/n
        
    for i in range(n):
       dy = df(x,y)*h
       y = y + dy
       x = x + h
    
    print("x: ",x, "y: ", y, "erro: ", abs(y-sp(x,y)))
    

# h = 0.5    
# euler(0,1,5,10)
# x:  5.0 y:  36.625 erro:  6.041666666666664

# h = 0.25    
# euler(0,1,5,20)
# x:  5.0 y:  39.59375 erro:  3.0729166666666643
    
# h = 0.125
# euler(0,1,5,40)
# x:  5.0 y:  41.1171875 erro:  1.5494791666666643
    
    
# QC = (s' - s)/ (s'' - s')    
# QC(X=5) = (39.59375 - 36.625) / (41.1171875 - 39.59375) =  1.948717948717949

# E'' = (s'' - s)/ 2^ordem-1
# E'' =  (41.1171875 - 39.59375) = 1.5234375
 
    
#-----------------------------------------------------------
    
    
def runga_kuta_2ordem(x0,y0,xf,n):
    x = x0
    y = y0
    h = (xf-x0)/n
        
    for i in range(n):
       dy = df(x + h/2, y + df(x,y)*(h/2))*h
       y = y + dy
       x = x + h
    
    print("x: ",x, "y: ", y, "erro: ", abs(y-sp(x,y)))
    
    
# h = 0.5    
# runga_kuta_2ordem(0,1,5,10)
# x:  5.0 y:  42.5625 erro:  0.1041666666666643

# h = 0.25    
# runga_kuta_2ordem(0,1,5,20)
# x:  5.0 y:  42.640625 erro:  0.026041666666664298
    
# h = 0.125
# runga_kuta_2ordem(0,1,5,40)
# x:  5.0 y:  42.66015625 erro:  0.006510416666664298
    
    
# QC = (s' - s)/ (s'' - s')    
# QC(X=5) = (42.640625 - 42.5625) / (42.66015625 - 42.640625) =  4.0

# E'' = (s'' - s)/ 2^ordem-1
# E'' =  (42.66015625 - 42.5625)/2^2-1 = 0.03255208333333334
       