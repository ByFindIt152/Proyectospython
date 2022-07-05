#SOLUCION no mia

num = int(input("Por favor ingrese un número: "))
c0 = 0
cont = 0

if(num>0):
    c0=num

while c0 != 1:
    if c0%2 == 0:
        c0 /= 2
    else:
        c0=3*c0+1
    cont += 1
    print(c0)
print('Pasos necesarios: ', cont)
