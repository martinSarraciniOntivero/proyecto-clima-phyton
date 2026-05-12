
from traducciones import traducir_clima
from traducciones import obtener_emoji_clima
from traducciones import obtener_emoji_sensacion
import requests

def obtener_clima_dia(ciudad):

    api_key = "TU_API_KEY"

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid={api_key}&units=metric"

    respuesta = requests.get(url)

    datos = respuesta.json()

    print(datos)
