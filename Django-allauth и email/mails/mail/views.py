from django.shortcuts import render, reverse, redirect
from django.views import View
from django.core.mail import mail_admins  # импортируем функцию для массовой отправки писем админам
from datetime import datetime

from django.template.loader import render_to_string

from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.core.mail import mail_managers
from .models import Appointment


def notify_managers_appointment(sender, instance, created, **kwargs):
    subject = f'{instance.client_name} {instance.date.strftime("%d %m %Y")}'

    mail_admins(
        subject=f'{instance.client_name} {instance.date.strftime("%d %m %Y")}',
        message=instance.message,
    )
    print(f'{instance.client_name} {instance.date.strftime("%d %m %Y")}')

post_save.connect(notify_managers_appointment, sender=Appointment)


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()



        return redirect('make_appointment')


