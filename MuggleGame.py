secret_number = 777
answer = 0
while answer != secret_number:
    answer = int(input(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
"""))
    if answer == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora")
        break
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
        
