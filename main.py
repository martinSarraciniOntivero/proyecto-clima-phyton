
from pronosticoActual import obtener_clima
from pronosticoActual import mostrar_clima
from pronosticoDia import obtener_clima_dia
from pronosticoDia import mostrar_clima_dia

print("================================")
print("🌤️ Hola! ¿Qué pronóstico buscás?")
print("1 - Pronóstico actual")
print("2 - Pronóstico del día")
print("================================")
opcion = input("Elegí una opción: ")

if opcion == "1":
    print("¡Genial! Vamos a mostrarte el pronóstico actual.")
    ciudad = input("🌍 Ingresá una ciudad: ")
    datosClima = obtener_clima(ciudad)

    if datosClima:
        mostrar_clima(datosClima, ciudad)
elif opcion == "2":
    print("¡Genial! Vamos a mostrarte el pronóstico del día.")
    ciudad = input("🌍 Ingresá una ciudad: ")
    datosClimaDia = obtener_clima_dia(ciudad)
    if datosClimaDia:
        mostrar_clima_dia(datosClimaDia, ciudad)    
else:
    print("❌ Opción no válida. Por favor, elige 1 o 2.")


