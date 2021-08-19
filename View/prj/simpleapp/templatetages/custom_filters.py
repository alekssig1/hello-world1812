from django import template

register = template.Library()

censor = ['мат1', 'мат2', 'мат3']


@register.filter(name='censor')
def censor(value):
    words_list = value.split()
    for index, word in enumerate(words_list):
        if word.lower() in censor:
            words_list[index] = "*******"
    return "".join(words_list)
