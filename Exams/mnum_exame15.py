import math

# Ex 1
def f1(t, T):
    return -0.25*(T-37)

def euler(t, T, h):
    
    for i in range(2):
        dy = f1(t,T)*h
        T = T + dy
        t = t + h
        
    print("T: ", T)

print("EXERCISE 1:\n")
euler(5,3,0.4)
print()



# Ex 3
# Feito no máxima
# d) x3



# Ex 4

# Maxima
# a) x1 e x2
# b) Nenhuma
# c) x1 e x2

def f4(x):
    return 2 * math.log(2*x)

def pic(x):
    
    for i in range(2):
        print("x: ",x)
        x = f4(x)
        

print("EXERCISE 4:\n")
pic(1.1)
print("REsiduo:", 1.5769147207285406 - 1.1 )
print()



# Ex 5
def f5(x):
    return math.sqrt(1 + (2.5*math.e**(2.5*x))**2)


def trap(a,b,h):
    
    n = round(abs(b-a)/h)
    area = 0.0
    
    for i in range(n):
        if (i == 0):
          area += f5(a+h*i)
        else:
            area += 2*f5(a+h*i)
            

    area += f5(b)
    area *= h/2
    
    return area

def simp(a,b,h):
    
    n = round(abs(b-a)/h)
    area = 0.0
    
    for i in range(n):
        if (i == 0):
          area += f5(a+h*i)
        elif (i%2 == 0):
            area += 2*f5(a+h*i)
        else:
            area += 4*f5(a+h*i)
            

    area += f5(b)
    area *= h/3
    
    return area

print("EXERCISE 5:\n")
print("h:", 0.125, "h'", 0.125/2, "h'':", 0.125/4)
I_t = trap(0,1,0.125)
II_t = trap(0,1,0.125/2)
III_t = trap(0,1,0.125/4)

print("I_t = ", I_t, "II_t=",II_t, "III_t=",III_t)
print("QC_trap = ", (II_t-I_t)/(III_t-II_t))
print("E_trap = ", (III_t-II_t)/ (2**2 - 1 ))

I_s = simp(0,1,0.125)
II_s = simp(0,1,0.125/2)
III_s = simp(0,1,0.125/4)

print("I_s = ", I_s, "II_t=",II_s, "III_t=",III_s)
print("QC_simp = ", (II_s-I_s)/(III_s-II_s))
print("E_simp = ", (III_s-II_s)/ (2**4 - 1 ))
print()


# Ex 6




# Ex 7
def f7(x):
    return x**3 - 10 * math.sin(x) + 2.8

def bissec(a,b):
    
    for i in range(2):
        m = (a+b)/2
        
        if(f7(a)*f7(m) < 0):
            b = m
        else:
            a = m

    return b
print("EXERCISE 7:\n")           
print("b(iter 2):",bissec(1.5,4.2))  







