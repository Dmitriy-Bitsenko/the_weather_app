from django.shortcuts import render
import requests
# Create your views here.


def index(request):
    appid = '7b9bb19a3d3ab365e49c4d9de6991d0e'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Asha'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
        'sky': res['weather'][0]['description'],
        'wind': res['wind']['speed']
    }
    context = {'info': city_info}
    print(city_info)
    print(res)
    print(context)
    return render(request, 'weather/index.html', context)
