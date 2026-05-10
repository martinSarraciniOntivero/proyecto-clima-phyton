import requests

ciudad = input("Ingresá una ciudad: ")


def obtener_clima(ciudad):
    api_key = "8b279de45d4431474c0678b930456ef0"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"

    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos
datosClima = obtener_clima(ciudad)

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


def mostrar_clima(datosClima):
    climaIngles = datosClima["weather"][0]["description"]
    climaEspañol = traducir_clima(climaIngles)

    print("ciudad:", datosClima["name"])
    print("temperatura:", datosClima["main"]["temp"], "°C")
    print("humedad:", datosClima["main"]["humidity"], "%")
    print("descripción:", climaEspañol)

mostrar_clima(datosClima)