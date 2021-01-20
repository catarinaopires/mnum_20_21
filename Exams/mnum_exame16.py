import math

# Ex 1
# 1: + calulos simples (pouca complexidade)
#    - pouco preciso pois o erro causado pela tuncação vai-se acumular e provocar um erro final muito grande  

# 2: + mais preciso que 1 por utilizar arredondamentos em vez de truncação
#    - calculos mais complexos

# 3: +
#    - pouco preciso pois perdem-se algarismos significativos da multiplicação, ao multiplicar um float por int

# 4: + 1/2^m em que m é inteiro faz com que os cálculos estejam sempre dentro das possibilidades da máquina
# que trabalha em binário; Reduz muito o erro
#    -

# Conclusão: 4 melhor opção   


# Ex 2
def f2_1(x,y):
    return x**2 - y - 1.2

def f2_1x(x,y):
    return 2*x

def f2_1y(x,y):
    return -1

def f2_2(x,y):
    return -x + y**2 - 1.0

def f2_2x(x,y):
    return -1.0

def f2_2y(x,y):
    return 2*y

def newton(x,y):
    
    for i in range(2):
        x1 = x - (f2_1(x,y)*f2_2y(x,y) - f2_2(x,y) * f2_1y(x,y)) / (f2_1x(x,y) * f2_2y(x,y) - f2_2x(x,y) * f2_1y(x,y))
        y1 = y - (f2_2(x,y)*f2_1x(x,y) - f2_1(x,y) * f2_2x(x,y)) / (f2_1x(x,y) * f2_2y(x,y) - f2_2x(x,y) * f2_1y(x,y))
        
        print("x:",x1, "  y:", y1)
        x=x1
        y=y1

print("EXERCISE 2:"); print()      
newton(1.0,1.0)        
print() 


# Ex 3





# Ex 4
def f4(x):
    return 1*x**7 + 0.5*x - 0.5

def corda(a,b):
    
    for i in range(4):
        w = (a*f4(b) - b*f4(a))/(f4(b)-f4(a))
        
        print("a:",a, "   b:", b, "   w: ", w)
        print("fa:",f4(a), "   fb:", f4(b), "   fw: ", f4(w))
        print()
        
        if f4(a)*f4(w) < 0:
            b = w
        else:
            a = w
            


print("EXERCISE 4:"); print()  
corda(0.0,0.8)


# Ex 5
# y'' = A + t^2 + t.y'
def dy(t,z):
    return z

def dz(t,z):
    return 0.5 + t**2 + t*z

def euler(t,y,z,h):
    
    for i in range(3):
        z1 = z + dz(t,z)*h
        y1 = y + dy(t,z)*h
        
        
        print("n: ",i,"  t:",t, "    y:", y)
        z=z1
        y=y1
        t += h

print("EXERCISE 5:"); print() 
print("Euler:\n");euler(0,0,1,0.25)
print()

def rk4(t,y,z,h):
    
    for i in range(3):
        d1y = h*dy(t,z)
        d1z = h*dz(t,z)
        
        d2y = h*dy(t+h/2, z+d1z/2)
        d2z = h*dz(t+h/2, z+d1z/2)
        
        d3y = h*dy(t+h/2, z+d2z/2)
        d3z = h*dz(t+h/2, z+d2z/2)
        
        d4y = h*dy(t+h,z+d3z)
        d4z = h*dz(t+h,z+d3z)
        
        dy_ = d1y/6.0 + d2y/3.0 + d3y/3.0 + d4y/6.0
        dz_ = d1z/6.0 + d2z/3.0 + d3z/3.0 + d4z/6.0
        
        print("n: ",i,"  t:",t, "    y:", y)
        z += dz_
        y += dy_
        t += h

print("RK4:\n");rk4(0,0,1,0.25)
print()




# Ex 6
def f6(x):
    return math.sqrt(1 + (1.5*math.e**(1.5*x))**2)

def trap(a,b,h):
    
    n = round(abs(b-a)/h)
    area = 0.0
    
    for i in range(n):
        if(i==0):
            area += f6(a+i*h)
        else:
            area += 2*f6(a+i*h)
            
    area += f6(b)
    area *= h/2  
    return area
          
def simp(a,b,h):
    
    n = round(abs(b-a)/h)
    area = 0.0
    
    for i in range(n):
        if(i==0):
            area += f6(a+i*h)
        elif(i%2==0):
            area += 2*f6(a+i*h)
        else:
            area += 4*f6(a+i*h)    
            
    area += f6(b)
    area *= h/3 
    return area


print("EXERCISE 6: \n");
print("h:", 0.5, "h':",0.5/2, "h'':", 0.5/4)
print()

S_trap = trap(0,2,0.5)
SS_trap =  trap(0,2,0.5/2)
SSS_trap = trap(0,2,0.5/4)
print("Trap::: S:", S_trap, "S':", SS_trap, "S'':", SSS_trap)

S_simp = simp(0,2,0.5)
SS_simp =  simp(0,2,0.5/2)
SSS_simp = simp(0,2,0.5/4)
print("SIMP::: S:", S_simp, "S':", SS_simp, "S'':", SSS_simp)

Qc_trap = (SS_trap - S_trap)/ (SSS_trap-SS_trap)
Qc_simp = (SS_simp - S_simp)/ (SSS_simp-SS_simp)
print("QC_trap: ",  Qc_trap, "QC_simp: ", Qc_simp)

E_trap = (SSS_trap - SS_trap)/ (2**2 - 1)
E_simp = (SSS_simp - SS_simp)/ (2**4 - 1)
print("E_trap: ",  E_trap, "E_simp: ", E_simp)      













