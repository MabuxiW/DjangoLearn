from django import template


register = template.Library()

@register.filter(name='Nextract')

def Nextract(value1,value2):
    try:
        value = value1[value2]
    except:
        value = None
    return value