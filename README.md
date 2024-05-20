# Django Bootstrap 5 Dark Mode Switch

[![image](https://img.shields.io/pypi/v/django-bootstrap5-dark-mode-switch)](https://pypi.python.org/pypi/django-bootstrap5-dark-mode-switch)

[![PyPI - Downloads](https://img.shields.io/pypi/dm/django-bootstrap5-dark-mode-switch)](https://pypi.python.org/pypi/django-bootstrap5-dark-mode-switch)

Use of bootstrap 5 dark mode made easy.

## What is this for?

django-bootstrap5-dark-mode-switch enables you to use the 
[Bootstrap 5 dark mode](https://getbootstrap.com/docs/5.3/customize/color-modes/) 
in your Django projects. With this library installed you get a menu from which 
you can select light mode, dark mode and an auto mode that automatically adapts 
your theme to the theme selected with your browser or operating system.

The dark mode switch is fully compatible with the django admin dark mode. So if 
you select dark mode in your django admin it will also be enabled with your 
frontend templates and vice versa.

## Installing

`django-bootstrap5-dark-mode-switch` can be found on pypi. Run 
`pip install django-bootstrap5-dark-mode-switch` to install the 
package on your machine or in your virtual environment.

## Getting Started

You need to have [django-bootstrap5](https://django-bootstrap5.readthedocs.io/en/latest/) >= 24.2 installed.

Add the app to your settings.py:

```
INSTALLED_APPS = [
    ...,
    'dark_mode_switch',
    ...,
]
```

Include the css file in your base template:

```
{% block bootstrap5_extra_head %}
{{ block.super }}
<link href="{% static 'dark_mode_switch/dark-mode-switch.css' %}" rel="stylesheet" type="text/css">
{% endblock %}
```

Include the javascript file in your base template:

```
{% block bootstrap5_extra_script %}
{{ block.super }}
<script src="{% static 'dark_mode_switch/dark-mode-switch.js' %}"></script>
{% endblock %}
```

Finally include the html for the switch into your navbar:

```
<nav class="navbar navbar-expand">
    <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'home' %}">
            Your app name
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                {% include 'dark_mode_switch/dark_mode_switch.html' %}
            </ul>
        </div>
    </div>
</nav>
```

If you like to have the switch outside the navbar you can create your own
template by overriding it in `templates/dark_mode_switch/dark_mode_switch.html`.
Please pay attention to the classes and ids of the options.

## Colors

As long as you stick with the standard bootstrap themes you don't have to 
worry about colors. If you like to use your own color definitions you should 
define also the dark mode color set 
(see [Bootstrap 5 dark mode](https://getbootstrap.com/docs/5.3/customize/color-modes/)).

