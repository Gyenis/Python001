print("Kezdőképernyő")
print("Én egy egyenleteket megoldó program vagyok")
print("1. Elsőfokú egyenlet")
print("2. Másodfokú egyenlet")
választás= input("Kérem a választásodat!(1,2)")

if választás == 1:
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
elif választás == 2:
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

