# cakecommerce/views.py

from django.views.generic import TemplateView

class MenuView(TemplateView):
    template_name = 'app/menu.html'

