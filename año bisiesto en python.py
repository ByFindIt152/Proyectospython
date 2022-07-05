year = int(input("Introduce un año:"))

#
# Escribe tu código aquí.
#	
if year < 1582:
    print("No dentro del período del calendario Gregoriano")
else:
    print("Año Bisiesto" if not year % 4 and (year % 100 or not year % 400) else "Año Común")
