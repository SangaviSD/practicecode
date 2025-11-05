from django import template

register = template.Library()

@register.filter(name='greet')
@register.filter(name='age')

def greet(name):
    return f"hello {name}"

# def age(name):
#     return f"{name} your age is 22"