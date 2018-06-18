import numpy as np
import sys
from math import acos,pi  
#print(sys.version)
def gradys(vx1,vy1,vx2,vy2,x4,y4):
	print('gradus',dlina(vx1,vy1,x4,y4)**2+dlina(vx2,vy2,x4,y4)**2-dlina(vx1,vy1,vx2,vy2)**2)
	return (acos ((dlina(vx1,vy1,x4,y4)**2+dlina(vx2,vy2,x4,y4)**2-dlina(vx1,vy1,vx2,vy2)**2)/2/dlina(vx1,vy1,x4,y4)/dlina(vx2,vy2,x4,y4)))/pi*180  



def dlina(xx1,yy1,xx2,yy2) :
	return ((yy1-yy2)**2+(xx1-xx2)**2)**0.5

def test():
	x1=int(input())
	y1=int(input())
	x2=int(input())
	y2=int(input())
	x3=int(input())
	y3=int(input())
	x4=int(input('x4 : '))
	y4=int(input('y4 : '))
	

	if (y2-y1)*(x3-x2)-(y3-y2)*(x2-x1)==0:
		print("нельзя постоить треугольник")
	else: 
		print("можно постоить треугольник")  
		l1=((x2-x1)**2+(y2-y1)**2)**0.5
		l2=((x3-x2)**2+(y3-y2)**2)**0.5
		l3=((x1-x3)**2+(y1-y3)**2)**0.5
		if l1>=l2 and l1>=l3 : l1,l3=l3,l1 
		if l2>=l1 and l2>=l3 : l2,l3=l3,l2

		if abs (l3**2-l2**2-l1**2)<0.000001 : print("прямоугольный")
		elif l3**2>l2**2+l1**2 : print("тупоугольный")
		else : print("остроугольный")
		print(l1,l2,l3)
		print(l1**2+l2**2,l3**2)
		 
		if l1==l2==l3 : print("равносторонний")
		elif l1==l2 or l1==l3 or l2==l3 : print("равнобедренный")
		else : print("разносторонний")	

		ygol1 =gradys(x1,y1,x2,y2,x4,y4) 
		ygol2 =gradys(x1,y1,x3,y3,x4,y4)
		ygol3 =gradys(x3,y3,x2,y2,x4,y4)
		print('ygol1 : ',ygol )
		print('ygol2 : ',ygo2 )
		print('ygol3 : ',ygo3 )
		
test()
