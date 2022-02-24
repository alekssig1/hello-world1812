from django.apps import AppConfig
import redis


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):

        import news.signals


red = redis.Redis(
    host='redis-15160.c10.us-east-1-3.ec2.cloud.redislabs.com',
    port=15160,
    password='qYuEsEMNkdOzRnS5pkkwLVS28y111yJl'
)