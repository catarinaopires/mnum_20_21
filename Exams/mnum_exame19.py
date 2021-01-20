import math

# Ex 1
# a) 1 zero
# b) zero em ]-1,-0.5[ logo ]-1,0[ contém zero

# c)
def f(x):
    return math.sin(x) + x**5 -0.2*x+1

def bissec(a,b):
    for i in range(6):
        m = (a+b) / 2
        
        if(f(a)*f(m) < 0):
            b = m
        else:
            a = m
    
    print("x= ",m, "; erro abs: ", max(abs(a-m), abs(b-m)), ";erro rel: ", max(abs(a-m), abs(b-m))/m)
    
bissec(-1,0)    
print()


# Ex 2
def f1(x,y):
    return x**2-y-1.2
def f1_x(x,y):
    return 2*x
def f1_y(x,y):
    return -1
    
def f2(x,y):
    return -x+y**2-1.0
def f2_x(x,y):
    return -1
def f2_y(x,y):
    return 2*y

def newton(x,y):
    
    for i in range(2):
        x = x - ((f1(x,y) * f2_y(x,y) - f2(x,y) * f1_y(x,y)) / (f1_x(x,y) * f2_y(x,y) - f2_x(x,y) * f1_y(x,y)))
        y = y - ((f2(x,y) * f1_x(x,y) - f1(x,y) * f2_x(x,y)) / (f1_x(x,y) * f2_y(x,y) - f2_x(x,y) * f1_y(x,y)))
        print("x = ",x, "; y: ",y)
        
newton(1.00000, 1.00000)    
print()

# Ex 3
def f3(x,y):
    return math.sqrt(1+ (1.5*math.e**(1.5*x))**2)

def trap(a,b,h):
    solution = 0.0
    n = round(abs(b-a)/h)
    
    for i in range(n):
        if (i == 0):
            solution += f(a+i*h)
        else:
            solution += 2*f(a+h*i)
        
    solution += f(b)
    solution = solution*(h/2)

    #print("solution: ", solution)   
    return solution     
        
def simp(a,b,h):
    solution = 0.0
    n = round(abs(b-a)/h)
    
    for i in range(n):
        if (i == 0):
            solution += f(a+i*h)
            
        elif(i%2 == 0):
            solution += 2*f(a+h*i)
        else:
            solution += 4*f(a+h*i)
        
    solution += f(b)
    solution = solution*(h/3)

    #print("solution: ", solution)
    return solution 

S_trap = trap(0,2,0.25)
SS_trap =  trap(0,2,0.25/2)
SSS_trap = trap(0,2,0.25/4)
print("Trap::: S:", S_trap, "S':", SS_trap, "S'':", SSS_trap)

S_simp = simp(0,2,0.25)
SS_simp =  simp(0,2,0.25/2)
SSS_simp = simp(0,2,0.25/4)
print("SIMP::: S:", S_simp, "S':", SS_simp, "S'':", SSS_simp)

Qc_trap = (SS_trap - S_trap)/ (SSS_trap-SS_trap)
Qc_simp = (SS_simp - S_simp)/ (SSS_simp-SS_simp)
print("QC_trap: ",  Qc_trap, "QC_simp: ", Qc_simp)

E_trap = (SSS_trap - SS_trap)/ (2**2 - 1)
E_simp = (SSS_simp - SS_simp)/ (2**4 - 1)
print("E_trap: ",  E_trap, "E_simp: ", E_simp)
print()


# Ex 4
def df(t,T):
    return -0.25*(T-59)

def euler(t0,T, dx):
    
    for i in range(2):
        T += df(t0,T)*dx
        t0 += dx
        
    return T    
        
Tf = euler(2,2, 0.5)
print("Tf: ", Tf)    
print()

# Ex 5
def f5(x):
    return -5*math.cos(x) + math.sin(x) + 10

def aurea(x1, x2):

    B = (math.sqrt(5)-1)/2
    A = B**2

    for i in range(3):
        x3 = A*(x2-x1) + x1
        x4 = B*(x2-x1) + x1
        
        print("x1: ", x1,"x2: ", x2,"x3: ", x3, "x4: ", x4, "fx1: ", f5(x1), "fx2: ",f5(x2),"fx3: ", f5(x3),"fx4: ", f5(x4))
        if(f5(x3) > f5(x4)):
            x2 = x4
            x4 = x3
        else:
            x1 = x3
            x3 = x4
            
aurea(2,4)           
print()               


# Ex 6
def f6(x,y):
    return 3*x**2 - x*y + 11*y + y**2 - 8*x
def f6_x(x,y):
    return 6*x - y - 8
def f6_y(x,y):
    return -x + 11 +2*y

def gradiente(x,y,h):
    
    for i in range(2):
        x1 = x - h * f6_x(x,y)
        y1 = y - h * f6_y(x,y)
        
        if f6(x1, y1) < f6(x,y):
            h *= 2
            x = x1
            y = y1
        else:
            h /= 2
        print("x: ",x, "y: ",y)         
    
gradiente(2,2,0.5)


        