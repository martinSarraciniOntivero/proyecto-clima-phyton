

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