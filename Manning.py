from math import *
from sympy import *
from scipy.misc import derivative
from sympy.parsing.sympy_parser import parse_expr

print("\n               FÓRMULA DE MANNING \n")
print("----------------------------------------------------------------")
print("Introduzca los datos ")

def Manning(n=float(input("n: ")),B=float(input("B: ")),H=float(input("H: ")),S=float(input("S: "))):
    En=n*0.10
    EB=B*0.10
    EH=H*0.10
    ES=S*0.10
    print("En= "+str(En)+" EB= "+str(EB)+" EH= "+str(EH)+" ES= "+str(ES))
    Q=(1/n)*(((B*H)**(5/3))/((B+2*H)**(2/3)))*S**(1/2)
    print("\nQ= "+str(Q))
    print("\n |  Derivadas  |")
    dn=(-(1/n**2))*(((B*H)**(5/3))/((B+2*H)**(2/3)))*S**(1/2)
    dB=(n**(-1))*(H**(5/3))*(S**(1/2))*(((5*B**(2/3))/(3*(B+2*H)**(2/3)))-((2*B**(5/3))/(3*(B+2*H)**(5/3))))
    dH=(n**(-1))*(B**(5/3))*(S**(1/2))*(((5*H**(2/3))/(3*(B+2*H)**(2/3)))-((4*H**(5/3))/(3*(B+2*H)**(5/3))))
    dS=(n**(-1))*(((B*H)**(5/3))/((B+2*H)**(2/3)))*((1/2)*(S**(-(1/2))))
    print("d/dn= "+str(dn)+"   d/dB= "+str(dB)+"   d/dH= "+str(dH)+"   d/dS= "+str(dS))

    EQ=dn*En+dB*EB+dH*EH+dS*ES
    print("\nEQ= "+str(EQ))
    Q1=Q-EQ
    Q2=Q+EQ
    print("\nQ - EQ= "+str(Q1)+"\nQ - EQ= "+str(Q2))

Manning()