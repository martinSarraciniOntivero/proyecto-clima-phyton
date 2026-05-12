import requests

ciudad = input("🌍 Ingresá una ciudad: ")


def obtener_clima(ciudad):
    api_key = "8b279de45d4431474c0678b930456ef0"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"

    respuesta = requests.get(url)
    datos = respuesta.json()
    if respuesta.status_code != 200:
        print("ciudad no encontrada")
        return None 
    return datos


def traducir_clima(clima):
    traducciones = {
    "clear sky": "cielo despejado",
    "few clouds": "pocas nubes",
    "scattered clouds": "nubes dispersas",
    "broken clouds": "nubes rotas",
    "shower rain": "lluvia de ducha",
    "rain": "lluvia",
    "thunderstorm": "tormenta eléctrica",
    "snow": "nieve",
    "mist": "niebla",
    "overcast clouds": "Muy nublado",
    }
    return traducciones.get(clima, clima)

def obtener_emoji_clima(clima):
    emojis = {
        "clear sky": "☀️",
        "few clouds": "🌤️",
        "scattered clouds": "☁️",
        "broken clouds": "☁️",
        "overcast clouds": "☁️",
        "rain": "🌧️",
        "shower rain": "🌦️",
        "thunderstorm": "⛈️",
        "snow": "❄️",
        "mist": "🌫️"
    }
    return emojis.get(clima,  "🌍")

def obtener_emoji_sensacion(sensacionTermica):
    
    emoji = "🌡️"
    if sensacionTermica >= 30:
        emoji = "🥵"

    elif sensacionTermica >= 20:
        emoji = "😎"

    elif sensacionTermica >= 10:
        emoji = "🙂"

    else:
        emoji = "🥶"
    return emoji

def mostrar_clima(datosClima):
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
    
datosClima = obtener_clima(ciudad)

if datosClima:
    mostrar_clima(datosClima)
