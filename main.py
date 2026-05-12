
from pronosticoActual import obtener_clima
from pronosticoActual import mostrar_clima

ciudad = input("🌍 Ingresá una ciudad: ")



    
datosClima = obtener_clima(ciudad)

if datosClima:
    mostrar_clima(datosClima, ciudad)
