import math

# Ex 1
def f1(x,y):
    return math.sin(x+y) - math.e**(x-y)

def f1dx(x,y):
    return math.cos(x+y) - math.e**(x-y)

def f1dy(x,y):
    return math.cos(x+y) + math.e**(x-y)

def f2(x,y):
    return math.cos(x+y) - (x**2)*(y**2)

def f2dx(x,y):
    return - math.sin(x+y) - 2*x*y**2

def f2dy(x,y):
    return - math.sin(x+y) - 2*y*x**2

def newton(x, y):
    
    for i in range(3):
        print("x:",x, "y:",y)
        
        x1 = x - (f1(x,y) * f2dy(x,y) - f2(x,y) * f1dy(x,y)) / (f1dx(x,y) * f2dy(x,y) - f2dx(x,y) * f1dy(x,y))
        y1 = y - (f2(x,y) * f1dx(x,y) - f1(x,y) * f2dx(x,y)) / (f1dx(x,y) * f2dy(x,y) - f2dx(x,y) * f1dy(x,y))

        x = x1
        y = y1
        
print("Ex 1:\n")
newton(0.5000,0.25000)        
   

# Ex 2
# É preciso ver a convergência: se pivot é maior que o módulo da soma dos outros coeficientes
# a) forma 1
# b) forma 3

# c)
# xn+1 = (1.2 - 61*y - 41*z)/103
# yn+1 = (0 - x - 13*z) / 5.5
# zn+1 = (13 - 2*x - 10*y) / 13


# Ex 3
# Aplicando a fórmula:
# Soma dos v.  vértices = 1.1+7.8+9.8+1.2=19.9
# Soma dos v. pontos médios das arestas = 4*(2.1+1.4+1.5+2.2)
# Ponto médio = 16*4
# Total = 112.7/9=12.52


# Ex 4
def dydx(x,y,z):
    return z
def dzdx(x,y,z):
    return -7*z - 4*y

def euler(x,y,z,h):
    
    for i in range(4):
        z1 = z + dzdx(x,y,z)*h
        y1 = y + dydx(x,y,z)*h
        

        print("x:",x,"y:",y, "z:",z)
        
        x += h
        y = y1
        z = z1

print("\nEx 4:")
euler(0.4,2,1,0.2)


# Ex 5
# Vários métodos para descobrir min, regra dos terços, secçao aurea, interpolação quadrática, da quadrática, 
# de levenberg-marquardt
# Nest ex, usarei o método da secção aurea 
def f5(x):
    return (x-5)**2 + x**4

def aurea(x1,x2):
    B = (math.sqrt(5) - 1) / 2
    A = B**2
    
    
    while(abs(x2-x1) > 0.0001):
        x3 = A*(x2-x1) + x1
        x4 = B*(x2-x1) + x1
        
            
        if f5(x3) < f5(x4):
            x2 = x4
            x4 = x3
        else:
            x1 = x3
            x4 = x4
    print("x1: ", x1,"x2: ", x2, "fx1: ", f5(x1), "fx2: ",f5(x2))
    
    
print("\nEx 5:\n")
aurea(0,2)    
     

# Ex 6
# 452.3         x 10^1
# 000.00002115  x 10^1
# 000.2583      x 10^1
# Soma: 452.55832115 = 0.4526 x 10^1

# Erro abs:    452.55832115 - 0.4526 x 10^1 ---> representar na notação
# Erro rel: (452.55832115 - 0.4526 x 10^1) / 452.55832115  ---> representar %
