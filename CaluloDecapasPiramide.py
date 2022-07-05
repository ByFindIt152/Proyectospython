blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#	
height = 0
 
inlayer = 1
 
while inlayer <= blocks:
 
    height += 1
    blocks -= inlayer       #Esta línea de código funciona distinto a la de arriba y abajo?
    inlayer += 1
 
print("The height of the pyramid: ", height)
