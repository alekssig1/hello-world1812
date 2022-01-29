from django import template

register = template.Library()

censor_list = ['мат1', 'мат2', 'мат3']


@register.filter(name='censor')
def censor(value):
    for word in censor_list:
        value = value.replace(word, '*****')
    return value