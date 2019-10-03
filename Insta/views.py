from django.views.generic import TemplateView

# Create your views here.
class HelloWorld(TemplateView):
    template_name = 'test.html'
