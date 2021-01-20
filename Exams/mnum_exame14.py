import math

# Ex 1
# passo integração: 0.5/5 = 0.1
# x(0) = 1
# k = 20 porque x dá o valor mais próximo de 0.0

def dydx(x,y,z):
    return z
def dzdx(x,y,z):
    return (-z-20*y)/20

def euler(x,y,z,h):
    
    for i in range(17):
        z1 = z + dzdx(x,y,z)*h
        y1 = y + dydx(x,y,z)*h
        

        print("t:",x,"x:",y, "x':",z)
        
        x += h
        y = y1
        z = z1

print("\nEx 1:")
euler(0,1,0,0.1)


# Ex 2
# 2.1. 3 zeros

# 2.2
def f2(x):
    return -x + 40*math.cos(math.sqrt(x)) + 3
def f2dx(x):
    return -(20*math.sin(math.sqrt(x)))/math.sqrt(x) - 1

def newton(x):
    
    for i in range(3):
        print("x", x, "g(x)", f2(x))
        x = x - f2(x)/f2dx(x)
        
 
print("\nEx 2:")    
newton(1.700)  

# 2.3: 0 casas exatas porque 0.7677 não tem casas exatas



# Ex 3
# feita no Maxima


# Ex 4
# TODO: ???


# Ex 5
def f5(x):
    return 5*math.cos(x) - math.sin(x)

def aurea(x1,x2):
    
    B = (math.sqrt(5) - 1)/2
    A = B**2
    
    for i in range(3):
       x3 = A*(x2-x1) + x1
       x4 = B*(x2-x1) + x1
       
       print("x1:",x1,"x2:",x2, "x3:",x3, "x4:",x4)
       print("f1:", f5(x1), "f2", f5(x2), "f3", f5(x3), "f4", f5(x4))
       
       if(f5(x3) < f5(x4)):
           x2 = x4
           x4 = x3
    
       else:
           x1 = x3
           x3 = x4
           
print("\nEx 5:")
aurea(2,4)            
print("amplitude: (x1-x4)", 2.944271909999159 - 2.4721359549995796)


# Ex 6
# Para cálculo de integrais definidos tempos o método dos Trapézios e o método de Simpson.
# Descobrir Qc, se QC de acordo com a ordem, então podemos analisar os erros absolutos



# Ex 7
# a)  2 raízes reais (x=-0.9271729230378577,x=3.98443722420693)
# b) x=3.98443722420693

# c) Sim/Sim/Não

# d)

def pic(x):
    
    for i in range(3):
        print("x:",x)
        x = (4*x**3 - x + 3)**(1/4)
        
        

print("\nEx 7:")
pic(3.5000)
       