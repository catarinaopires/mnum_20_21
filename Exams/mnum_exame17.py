import math

# Ex 1
def f1(x):
    return (x-5)**2 + x**4

def aurea(x1,x2):
    
    B = (math.sqrt(5) - 1)/2
    A = B**2
    
    while(abs(x2-x1) > 0.0001):
        x3 = A*(x2-x1) + x1
        x4 = B*(x2-x1) + x1
        
        print("x1: ", x1,"x2: ", x2,"x3: ", x3, "x4: ", x4, "fx1: ", f1(x1), "fx2: ",f1(x2),"fx3: ", f1(x3),"fx4: ", f1(x4)) 
        
        if(f1(x3) < f1(x4)):
            x2 = x4
            x4 = x4
        else:
            x1 = x3
            x3 = x4
            

print("EXERCISE 1: \n");    
aurea(0,2)
print(); print("############################\n");



# Ex 2
def f2(x):
    return math.sqrt(1 + (2.5*math.e**(2.5*x))**2)
     
     
def trap(a,b,h):
    
    n = round(abs(b-a)/h)
    area = 0.0
    
    for i in range(n):
        if(i == 0):
            area += f2(a+i*h)
        else:
            area += 2*f2(a+i*h)
            
    area+= f2(b)
    area *= h/2
    return area

def simp(a,b,h):
    
    n = round(abs(b-a)/h)
    area = 0.0
    
    for i in range(n):
        if(i == 0):
            area += f2(a+i*h)
        elif(i%2 == 0):
            area += 2*f2(a+i*h)
        else:
            area += 4*f2(a+i*h)
            
    area+= f2(b)
    area *= h/3
    return area

print("EXERCISE 2: \n");

print("h:", 0.125, "h':",0.125/2, "h'':", 0.125/4)
print()

S_trap = trap(0,1,0.125)
SS_trap =  trap(0,1,0.125/2)
SSS_trap = trap(0,1,0.125/4)
print("Trap::: S:", S_trap, "S':", SS_trap, "S'':", SSS_trap)

S_simp = simp(0,1,0.125)
SS_simp =  simp(0,1,0.125/2)
SSS_simp = simp(0,1,0.125/4)
print("SIMP::: S:", S_simp, "S':", SS_simp, "S'':", SSS_simp)

Qc_trap = (SS_trap - S_trap)/ (SSS_trap-SS_trap)
Qc_simp = (SS_simp - S_simp)/ (SSS_simp-SS_simp)
print("QC_trap: ",  Qc_trap, "QC_simp: ", Qc_simp)

E_trap = (SSS_trap - SS_trap)/ (2**2 - 1)
E_simp = (SSS_simp - SS_simp)/ (2**4 - 1)
print("E_trap: ",  E_trap, "E_simp: ", E_simp)      
            
print(); print("############################\n");            
            



# Ex 3
def f3(x):
    return math.e**x - x - 5
def f3dx(x):
    return  math.e**x - 1

def newton(x, n):
    
    for i in range(n):
        x1 = x - f3(x)/f3dx(x)
        x=x1
         
    return x
 
    
def pic1(guess,n):
    x = guess
    
    for i in range(n):
        x1 = math.e ** x - 5
        x = x1
        
    return x

def pic2(guess,n):
    x = guess
    
    for i in range(n):
        x1 = math.log(5+x)
        x = x1
        
    return x     
  
print("EXERCISE 3: \n");

# Pelo gráfico 2 zeros
print("Newton: ", newton(1, 5), f3(newton(1,5)))
print("Newton: ", newton(-5,5), f3(newton(1,5)))

# Pic1 - converge para solução negativa
print("Pic 1: ", pic1(1, 5), f3(pic1(1, 5)))
print("Pic 1: ", pic1(-5,5), f3(pic1(1, 5)))

# Pic2 - converge para soluão positiva
print("Pic 2: ", pic2(1, 5), f3(pic2(1, 5)))
#print("Pic 2: ", pic2(-5,5), f3(pic2(1, 5)))        Fora domínio
print(); print("############################\n");   



# Ex 4
def dCdt(T,C):
    return  (- math.e ** (-0.5000/(T+273)))*C

def dTdt(T, C):
    return 30.0000 *  (math.e **(-0.5000/(T+273)))*C - 0.5000*(T-20)

def euler(t0, T, C, n):
    t = 0.0
    
    for i in range(n):
        C1 = C + dCdt(T, C)*t0
        T1 = T + dTdt(T, C)*t0
        C = C1
        T = T1
        t += t0
        print("C:", C1, "## T:", T1, "## t: ",t)
    return T

print("EXERCISE 4: \nEuler:\n");
euler(0.25,25.000,2.500,2)

def rk4(t0, T, C):
    t = t0
    for i in range(2):
        d1t = t0*dTdt(T,C) 
        d1 = t0*dCdt(T,C) 
        
        d2t = t0*dTdt(T + d1t/2, C+d1/2) 
        d2 = t0*dCdt(T + d1t/2, C+d1/2)
        
        d3t = t0*dTdt(T + d2t/2, C+d2/2) 
        d3 = t0*dCdt(T + d2t/2, C+d2/2) 
        
        d4t = t0*dTdt(T + d3t, C+d3) 
        d4 = t0*dCdt(T + d3t, C+d3) 
        
        dt = d1t/6.0 + d2t/3.0 + d3t/3.0 + d4t/6.0 
        dc = d1/6.0 + d2/3.0 + d3/3.0 + d4/6.0
        
        C = C + dc
        T = T + dt
              
        print("C:", C, "## T:", T, "## t: ",t)
        t += t0
    
    
    
print();print("RK4:\n")
print("b)\n")
rk4(0.25, 25.000, 2.500)
print()

print("c)\n")
print("h:", 0.2500, "h':",0.2500/2, "h'':", 0.2500/4)
T_euler = euler(0.25,25.000,2.500,2)
TT_euler =  euler(0.25/2,25.000,2.500,4)
TTT_euler = euler(0.25/4,25.000,2.500,8)
print()
print("Euler::: T:", T_euler, "T':", TT_euler, "T'':", TTT_euler)


Qc_euler = (TT_euler - T_euler)/ (TTT_euler-TT_euler)
print("QC: ",  Qc_euler)

E_euler = (TTT_euler - TT_euler)/ (2**1 - 1)
print("E_euler: ",  E_euler) 


print(); print("############################\n");   
     
     
     
     
# Ex 5
def w(x,y):
    return -1.1*x*y + 12*y + 7*x**2 - 8*x

def wdx(x,y):
    return -1.1*y + 14*x - 8

def wdy(x,y):
    return -1.1*x + 12

def gradiente(x,y,h):
    
    for i in range(1):
        x1 = x - h*wdx(x,y)
        y1 = y - h*wdy(x,y)
        
        if(w(x1,y1) < w(x,y)):
            h *= 2.0
            x = x1
            y = y1
        else:
            h /= 2.0
    print("x: ",x, "## y: ", y, "## min: ", w(x,y))    
 

print("EXERCISE 5: \nGradient:\n");   
gradiente(3,1,0.1)     


            