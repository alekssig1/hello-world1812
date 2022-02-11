from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from .models import Appointment


class AppointmentView(View):
    # получаем шаблон для ввода данных
    def get(self, request):
        return render(request, 'make_appointment.html', {})

    # отправляем на сервер нашу информацию и сохраняем в БД
    def post(self, request):
        appointments = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointments.save()

        return redirect('make_appointment')
