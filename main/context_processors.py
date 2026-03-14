import requests
import datetime
from .models import Category


def get_weather(request):
    weather = requests.get('https://api.weatherapi.com/v1/current.json?q=fergana&key=9f0849df46a14a0a9bb91058261003').json()
    weather_time = weather['location']['localtime']
    weather_temp = weather['current']['temp_c']
    weather_icon = weather['current']['condition']['icon']
    categories  = Category.objects.all()

    return {
        'time': datetime.datetime.today().strftime('%d.%m.%Y'),
        'temp': weather_temp,
        'icon': weather_icon,
        'categories': categories
    }



