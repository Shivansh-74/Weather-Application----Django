from django.shortcuts import render,HttpResponse
import requests
# Create your views here.
def Home(request):
   try:
    city = request.GET.get('city','jaipur')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e3b82e2e56b3c13d40900d0158685549'
    data = requests.get(url).json()
    payload = {
        'city':data['name'],
        'weather':data['weather'][0]['main'],
        'decs':data['weather'][0]['description'],
        'icon':data['weather'][0]['icon'],
        'kelvin_temperature':data['main']['temp'],
        'celcius_temperature':int(data['main']['temp']-273),
        'pressure':data['main']['pressure'],
        'humidity':data['main']['humidity'],
        }
    context = {'data':payload}
    return render(request,'home.html',context)
    
   except Exception as e:
       return HttpResponse("Enter valid name")