b= input('Kérem az elsőfokú tag együtthatóját: ')
c= input('Kérem a konstans tagot: ')
b= float(b)
c= float(c)
if b!=0:
    x=-c/b
    print("A megoldás: ",x)
else:
    if c==0:
        print("Az összes valós szám megoldás")
    else:
        print("Nincs megoldás")


