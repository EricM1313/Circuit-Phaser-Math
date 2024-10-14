import numpy as np
import math

def ptc(r,theta):
    if r==0 and theta==0:
        return([0,0])
    return ([r*np.cos(np.deg2rad(theta)),r*np.sin(np.deg2rad(theta))])
    
    
    
def ctp(x,y):
    if x==0 and y==0:
        return([0,0])
    if x ==0 and y>0:
        return([y,90])
    if x ==0 and y<0:
        return([y,270])
    if x>0 and y==0:
        return ([x,0])
    if x<0 and y==0:
        return ([x,180])
    r = np.sqrt(x**2 + y**2)
    if x>0 and y>0:
        theta = np.rad2deg(np.arctan(y/x))
    if x < 0 and y>0:
        theta = 180 - np.rad2deg(np.arctan(y/-x))
    if x<0 and y<0:
        theta = 180 + np.rad2deg(np.arctan(y/x))
    if x>0 and y<0:
        theta = 360 - np.rad2deg(np.arctan(-y/x))
    return([r,theta])
        
        
def add(p1,p2):
    pc1 = ptc(p1[0],p1[1])
    pc2 = ptc(p2[0],p2[1])
    pol = ([pc1[0]+pc2[0],pc1[1]+pc2[1]])
    return(ctp(pol[0],pol[1]))
    
def subtract(p1,p2):
    pc1 = ptc(p1[0],p1[1])
    pc2 = ptc(p2[0],p2[1])
    pol = ([pc1[0]-pc2[0],pc1[1]-pc2[1]])
    return(ctp(pol[0],pol[1]))
    


def mult(c1,c2):
    pp1 = ctp(c1[0],c1[1])
    pp2 = ctp(c2[0],c2[1])
    pha = ([pp1[0]*pp2[0],pp1[1]+pp2[1]])
    return(ptc(pha[0],pha[1]))

def divide(c1,c2):
    pp1 = ctp(c1[0],c1[1])
    pp2 = ctp(c2[0],c2[1])
    pha = ([pp1[0]/pp2[0],pp1[1]-pp2[1]])
    return(ptc(pha[0],pha[1]))
  

def parallelCart(c1,c2):
    num = mult(c1,c2)
    denom = [c1[0]+c2[0],c1[1]+c2[1]]
    return(divide(num,denom))

def parallelPol(p1,p2):
    num = ptc(p1[0]*p2[0],p1[1]+p2[1])
    denom = ptc(add(p1,p2)[0],add(p1,p2)[1])
    return ctp(divide(num,denom)[0],divide(num,denom)[1])



print(parallelCart([0,20],[20,0 ]))
#print(parallelPol([40,0],[25,270]))
print(ctp(55,  56.66666  ))
print(ptc(.07,306.9))
print(mult([20,-10],[40,40]))
print(divide([1200,400],[60,30]))
#print(subtract([.12,45],[.25,-60]))
#print(add([40,0],[12.4,321]))
  



