
import requests
from traducciones import traducir_clima
from traducciones import obtener_emoji_clima
from traducciones import obtener_emoji_sensacion



def obtener_clima(ciudad):
    api_key = "8b279de45d4431474c0678b930456ef0"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"

    respuesta = requests.get(url)
    datos = respuesta.json()
    if respuesta.status_code != 200:
        print("❌ Ciudad no encontrada")
        return None 
    return datos



def mostrar_clima(datosClima, ciudad):
    climaIngles = datosClima["weather"][0]["description"]

    climaEspañol = traducir_clima(climaIngles)
    sensacion = datosClima['main']['feels_like']
    emojiClima = obtener_emoji_clima(climaIngles)
    emojiSensacion = obtener_emoji_sensacion(sensacion)

    print("==============================")
    print(f"🌍 Ciudad:       {ciudad}")
    print(f"🌡️ Temperatura:         {datosClima['main']['temp']: .1f} °C")
    print(f"{emojiSensacion} Sensación térmica: {sensacion: .1f} °C")
    print(f"🔺 Máxima:              {datosClima['main']['temp_max']: .1f} °C")
    print(f"🔻 Mínima:              {datosClima['main']['temp_min']: .1f} °C")
    print(f"💨 Viento:              {datosClima['wind']['speed']: .1f} m/s")
    print(f"💧 Humedad:             {datosClima['main']['humidity']} %")
    print(f"{emojiClima} Estado:            {climaEspañol}")
    print("==============================")