from WeatherAPI.celery import app
from .models import WeatherForecast
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import render_to_string
from user.models import UserAPI
from weather.models import Weather
from city.models import City


@app.task(name='Send_mail')
def send_mail_every_evening():
    users = WeatherForecast.objects.all()
    if not users:
        return 'Users not found'
    users = [[user.user.pk, user.city.pk] for user in users]
    send_email.delay(users)
    return 'Success'


@app.task(name='Send mail')
def send_email(users):
    subject = 'The Weather Forecast For Tomorrow'
    connection = get_connection()
    connection.open()
    email_list = []
    for element in users:
        user = UserAPI.objects.get(pk=element[0])
        city = City.objects.get(pk=element[1])
        weather = Weather.objects.get(city=city)

        context = {
            'city': city.name,
            'icon': weather.icon,
            'wind': weather.wind,
            'temp': weather.temp,
            'pressure': weather.pressure,
            'clouds': weather.clouds,
        }
        message = render_to_string('body.html', context)
        msg = EmailMultiAlternatives(subject=subject, body=message,  to=[user.email], connection=connection)
        msg.attach_alternative(message, 'text/html')
        email_list.append(msg)
    connection.send_messages(email_list)
    connection.close()
    return 'Success'

