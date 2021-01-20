import math
# 1
def f1(t,y):
    return y/(t-1)

def euler(t, y,h):
    
    for i in range(3):
        y += f1(t,y)*h
        t += h
        
        print("t:",t, "y",y)

euler(2, 2,0.25)
    
def rk4(t,y,h):
    
    for i in range(3):
        d1 = h*f1(t,y)
        d2 = h*f1(t+h/2,y+d1/2)
        d3 = h*f1(t+h/2, y+d2/2)
        d4 = h*f1(t+h,y+d3)
        
        dy = d1/6.0 + d2/3.0 + d3/3.0 + d3/6.0
        
        print("t:",t, "y",y)
        print("d1:",d1, "d2",d2, "d3",d3, "d4",d4)
        y += dy
        t += h
print()
rk4(2, 2,0.25)  


# Ex 3
def w(x,y):
    return -1.7*x*y + 12*y+7*x**2 - 8*x

def wdx(x,y):
    return -1.7*y + 14*x - 8

def wdy(x,y):
    return -1.7*x + 12

def gradient(x,y,h):
    
    for i in range(1):
        x1 = x - h*wdx(x,y)
        y1 = y - h*wdy(x,y)
        
        if(w(x1,y1) < w(x,y)):
            h *= 2
            x = x1
            y = y1
        else:
            h /= 2
    
        print("x:",x,"y:",y)
        return w(x,y)
    
    
print()
print("gradient:",gradient(2.4,4.3,0.1))


# Ex 5
def f2(x,y):
    return x**2 - y - 2

def f2dx(x,y):
    return 2*x

def f2dy(x,y):
    return -1

def f3(x,y):
    return -x + y**2 - 2

def f3dx(x,y):
    return -1

def f3dy(x,y):
    return 2*y

def newton(x,y):
    for i in range(3):
        print("x:",x,"y:",y)
        x = x - (f2(x,y) * f3dy(x,y) - f3(x,y) * f2dy(x,y))/ (f2dx(x,y) * f3dy(x,y) - f3dx(x,y) * f2dy(x,y))
        y = y - (f3(x,y) * f2dx(x,y) - f2(x,y) * f3dx(x,y))/(f2dx(x,y) * f3dy(x,y) - f3dx(x,y) * f2dy(x,y))
        

        
print();newton(1.500,0.800)   

# Ex 6
# opção 6     

# Ex 7
def f7(x):
    return math.e ** (1.5*x)
    
def simp(a,b,h):
    solution = 0.0
    n = round(abs(b-a)/h)
    
    for i in range(n):
        if (i == 0):
            solution += f7(a+i*h)
            
        elif(i%2 == 0):
            solution += 2*f7(a+h*i)
        else:
            solution += 4*f7(a+h*i)
        
    solution += f7(b)
    solution = solution*(h/3)

    print("solution: ", solution)
    return solution 

print()
S_simp = simp(2.5,3,0.125)
SS_simp =  simp(2.5,3,0.125/2)
SSS_simp = simp(2.5,3,0.125/4)
print("SIMP::: S:", S_simp, "S':", SS_simp, "S'':", SSS_simp)

Qc_simp = (SS_simp - S_simp)/ (SSS_simp-SS_simp)
print("QC_simp: ", Qc_simp)

E_simp = (SSS_simp - SS_simp)/ (2**4 - 1)
print("E_simp abs: ", E_simp)
print("E_simp rel: ", E_simp/SSS_simp)
print("Eabs normal:",31.66403286697275-SSS_simp)
print("Erel normal:", (31.66403286697275-SSS_simp) /31.66403286697275 )
    