# Exame 5/01/2021
import math

# Ex 2
def F(x):
    return x*0.1
def f(x):
    return math.cos(0.04*x)

def trap(a, b, h):
    area = 0.0
    n = round(abs(b-a)/h)
        
    for i in range(n):
        if (i==0):
            area += F(a+h*i)*f(a+h*i)
        else:
            area += 2*F(a+h*i)*f(a+h*i)
            
    area += F(b)*f(b)
    area = area * (h/2)
    
    return area

print("W_trap:", 2*math.pi * trap(0.0, 8.0, 1))
S = 2*math.pi * trap(0.0, 8.0, 1)
SS = 2*math.pi * trap(0.0, 8.0, 1/2)
SSS = 2*math.pi * trap(0.0, 8.0, 1/4)

QC = (S-SS)/(SSS-SS)
print("QC:", QC)

E = (SSS-SS)/ (2**2 - 1)
print("E:", E)



def simp(a, b, h):
    area = 0.0
    n = round(abs(b-a)/h)
    
    #f = [0.0,0.04, 0.08, 0.1,0.12,0.14,0.16,0.18,0.2,0.22, 0.24, 0.28, 0.32]
    
    for i in range(n):
        if (i==0):
            area += F(a+h*i)*f(a+h*i)
        if(i%2 == 0):
            area += 2*F(a+h*i)*f(a+h*i)
        else:
            area += 4*F(a+h*i)*f(a+h*i)
            
    area += F(b)*f(b)
    area = area * (h/3)
    
    return area

print("W_simp:", 2*math.pi * simp(0.0, 8.0, 1))
print("\nSIMP:\n")
Ss = 2*math.pi * simp(0.0, 8.0, 1)
SSs = 2*math.pi * simp(0.0, 8.0, 1/2)
SSSs = 2*math.pi * simp(0.0, 8.0, 1/4)

QCs = (Ss-SSs)/(SSSs-SSs)
print("QC:", QCs)

Es = (SSSs-SSs)/ (2**4 - 1)
print("E:", Es)



# Ex 3
def gaussSeidel(x,y,z,t):
    
    for i in range(1):
        x = (19 - 0.5*y - 3.0*z - 0.25*t)/6.0
        y = (-2.2 - 1.2*x - 0.25*z - 0.2*t)/3.0
        z = (9 - 0.25*y - (-1.0*x) - 2.0*t)/4.0
        t = (15 - 4.0*y - 1.0*z - 2.0*x)/8.0
        
        print("x:",x, "y:", y, "z:", z, "t:", t)
        
gaussSeidel(1.67969, -1.78160, 1.93752, 2.10369)


# Ex 4
# a. [-0.6, 3.4]

# Ex 5
def f5(x):
    return x**3 + 2*x**2 + 10*x - 41

def dx(x):
    return 3*x**2 + 4*x + 10 

def newton(x):
    for i in range(3):
        print("x:", x)
        x = x - f5(x)/dx(x)
newton(0)

# resposta f. 0; 4.100; 2.7654
