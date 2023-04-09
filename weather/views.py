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
        'temp': res['main': {'temp'}],
        'icon': res['weather']['icon']
    }
    print(city_info)
    print(res)
    return render(request, 'weather/index.html')
