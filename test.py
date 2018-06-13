import numpy as np
import sys
#print(sys.version)

def test():
	x1=int(input())
	y1=int(input())
	x2=int(input())
	y2=int(input())
	x3=int(input())
	y3=int(input())
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



test()
