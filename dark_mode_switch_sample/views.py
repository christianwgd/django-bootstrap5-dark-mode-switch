from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "dark_mode_switch_sample/index.html"
