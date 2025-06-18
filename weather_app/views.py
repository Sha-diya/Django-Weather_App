from django.shortcuts import render
import requests

def home(request):
    weather_data = None
    error = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'ba33775a684eda5d8552e2b07f23d261'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        if data.get('cod') != '404':
            weather_data = {
                'city': data['name'],
                'icon': data['weather'][0]['icon'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind': data['wind']['speed'],
            }
        else:
            error = 'City not found. Please try again.'
    return render(request, 'weather_app/home.html', {'weather_data': weather_data, 'error': error})


# Create your views here.
