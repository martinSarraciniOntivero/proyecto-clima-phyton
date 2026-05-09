import requests

ciudad = input("Ingresá una ciudad: ")
print(ciudad)

api_key = "8b279de45d4431474c0678b930456ef0"
url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"


respuesta = requests.get(url)

datos = respuesta.json()

print(datos)