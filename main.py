import requests

ciudad = input("Ingresá una ciudad: ")


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

def obtener_emoji(clima):
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

def mostrar_clima(datosClima):
    climaIngles = datosClima["weather"][0]["description"]

    climaEspañol = traducir_clima(climaIngles)

    emoji = obtener_emoji(climaIngles)

    print("==============================")
    print(f"🌤️ Ciudad:       {datosClima['name']}")
    print(f"🌡️ Temperatura:  {datosClima['main']['temp']} °C")
    print(f"💧 Humedad:      {datosClima['main']['humidity']} %")
    print(f"{emoji} Estado:       {climaEspañol}")
    print("==============================")

datosClima = obtener_clima(ciudad)

if datosClima:
    mostrar_clima(datosClima)
