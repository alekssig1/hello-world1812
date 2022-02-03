from django.apps import AppConfig


class AppointmentsConfig(AppConfig):
    name = 'appointments'

    def ready(self):

        # noinspection PyUnresolvedReferences
        import appointments.signals
