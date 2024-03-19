num=int(input("ingrese numero: "))
c=num%10
d=(num//10)%10
u=((num//10)//10)%10

c2=c*1
d2=d*10
u2=u*100

c3=c*100
d3=d*10
u3=u*1

if c2+d2+u2==num:
    if (c3+d3+u3)==num:
        print("numero capicua")
    else:
        print("numero NO capicua")

