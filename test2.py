from math import pi,cos,tan 
chv ='\u2502'
chg ='\u2500'
u_ln ='\u2514'
u_lv ='\u250c'
u_pv ='\u2510'
u_pn ='\u2518'
T_v ='\u252c'
T_n ='\u2534'
T_l ='\u251c'
T_p = '\u2524'
krest = '\u253c'

def f1(x) :  
	return x**0.5 - 2*cos(x*pi/2)
def f2(x) :  
   	return tan(0.2*x+0.3) - x**2+3  
a= float(input("нач зн x : "))	
b= float(input("кон зн x : "))
step= float(input("шаг : "))
vra=a
print(u_lv+8*chg+T_v+8*chg+T_v+8*chg+u_pv)
y_masive =[]  			
ymax = f1(vra)
ymin = f1(vra)
while vra<=b : 
	if ymax < f1(vra) : ymax=f1(vra)
	if ymin > f1(vra) : ymin=f1(vra)
	y_masive.append(f1(vra))	
	print(chv+str(vra)+(8-len(str(vra)))*" "\
+chv+str("{:3.3}".format(f1(vra)))+(8-len(str("{:3.3}".format(f1(vra)))))*" "\
+chv+str("{:3.3}".format(f2(vra)))+(8-len(str("{:3.3}".format(f2(vra)))))*" "+chv)
	print(T_l+8*chg+krest+8*chg+krest+8*chg+T_p)  
	vra=vra+step	
   
print(y_masive)
y_print=[]
x_print=[]
for i in range(len(y_masive)) : 
	vrmax=ymin
	for j in range(len(y_masive)) : 
		if vrmax <= y_masive[j] and y_masive[j]<ymax+1 : 
			vrmax=y_masive[j]
			ix=j
	y_masive[ix]=ymax+1
	y_print.append (40-round((vrmax-ymin)/(ymax-ymin)*40))
	x_print.append (round((ix*step)/(b-a)*80))
	print(vrmax, ix , x_print , y_print) 

for i in range(40) : 
	vrmax=ymin
	for j in range(len(y_masive)) : 
		if vrmax <= y_masive[j] and y_masive[j]<ymax+1 : 
			vrmax=y_masive[j]
			ix=j
	y_masive[ix]=ymax+1
	y_print.append (40-round((vrmax-ymin)/(ymax-ymin)*40))
	x_print.append (round((ix*step)/(b-a)*80))
	print(vrmax, ix , x_print , y_print) 
	
