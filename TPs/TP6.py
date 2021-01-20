def f(x):
    return x**4    

def metodoSimpson(a, b, n):
    area = 0
    h = abs(a-b)/ n
    area += f(a+2*h)
    
    for i in range(0, n, 2):
       area += 2*f(a+i*h)
        
    area += f(a+h)
    for i in range(1, n, 2):
        area += 4*f(a+i*h)
        
        
    area += f(b)   
    area = area * (h/3)
    return area



def sucessao1():
    x1 = 0
    
    while(x1 <= 2):
        x1 = x1 + 0.1
        
    return x1

def sucessao2():
    x2 = 0
    
    for i in range(21):
        x2 = 0 + i*0.1
    return x2

    
#Integral duplo de s(0,2)s(0,2) x+y dydx  = 8 
def trapduplo():
    



# Soma dos vértices dos limites de integração
#sum0 = f(a, c) + f(b,c) + f(a,d) + f(b,d)
sum0 = f(0, 0) + f(2,0) + f(0, 2) + f(2,2)

#
#sum1 



                                                                                                                                                   