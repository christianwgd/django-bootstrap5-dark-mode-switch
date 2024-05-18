from django.template import Library

register = Library()


@register.inclusion_tag('dark_mode_switch/dark_mode_switch.html')
def dark_mode_switch():
    pass
