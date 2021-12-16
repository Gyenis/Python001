#Elsőfokú egynelet
import math, cmath

a= input('Kérem a másodfokú egyenlet főegyütthatóját: ')
a= float(a)
b= input('Kérem az elsőfokú tag együtthatóját: ')
c= input('Kérem a konstans tagot: ')
b= float(b)
c= float(c)
if a==0:
    pass
else:
    d= b*b-4*a*c
    #print('A diszkrimináns értéke', d)

    if d>=0:
        print('Van valós megoldás.')
        x1= (-b-math.sqrt(d))/(2*a)
        x2= (-b+math.sqrt(d))/(2*a)
        print('Az egyik megoldás', x1)
        print('A másik megoldás', x2)
    else:
        print('Nincs valós megoldás.')
