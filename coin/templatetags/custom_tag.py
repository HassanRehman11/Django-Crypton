from django.template import Library

register = Library()


@register.filter(name='space2nill')
def space2nill(value):
    return value.replace(' ','')
