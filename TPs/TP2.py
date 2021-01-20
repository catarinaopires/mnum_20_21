## MNUM - TP2
import math

def f(x):
    return x**2 - 3


def bissec(a, b, precision):
    
    while abs(b-a) > precision:
        m = (a + b)/2
        
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
            
     
    return (a + b)/2
    

def metodo_corda(a, b, precision):
    s = (a * f(b) - b * f(a))/ (f(b)- f(a))
    
    while abs(f(s)) > precision:
        
        if f(a) * f(s) < 0.0:
            b = s
        else:
            a = s
            
        s = (a * f(b) - b * f(a))/ (f(b)- f(a))
        print("s= ", s, "; a= ", a, "; b= ", b);
            
    return s


## QUAL O MÉTODO + EFICIENTE (METODO CORDA MODIFICADO)