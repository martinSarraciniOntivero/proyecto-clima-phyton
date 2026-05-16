
from traducciones import traducir_clima
from traducciones import obtener_emoji_clima
from traducciones import obtener_emoji_sensacion
import requests

def obtener_clima_dia(ciudad):

    api_key = "8b279de45d4431474c0678b930456ef0"

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={api_key}&units=metric"

    respuesta = requests.get(url)

    datos = respuesta.json()
    if respuesta.status_code != 200:
        print("❌ Ciudad no encontrada")
        return None
    return(datos)

def mostrar_clima_dia(datos, ciudad):
    for pronostico in datos["list"][:8]:
        horaCompleta = pronostico["dt_txt"]
        hora = horaCompleta.split(" ")[1]
        hora = hora[:5]
        temperatura = pronostico["main"]["temp"]
        climaIngles = pronostico["weather"][0]["description"]
        climaEspañol = traducir_clima(climaIngles)
        emojiClima = obtener_emoji_clima(climaIngles)
        print("==============================")
        print(f"Horario UTC: {hora}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Clima: {climaEspañol} {emojiClima}")