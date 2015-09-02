from django.shortcuts import render
from cards.widget import widget
from django_widgets.widgets import custom_card

__author__ = 'bmitchem'

def hello_world(request):
    context = {'Text': "Hello World!"}
    fancyWidget = widget(template='django-widgets/hello_world.html', context=context)
    custom_widget = custom_card()


    return render(request, 'demo/hello_world.html', {'widget': fancyWidget, 'custom_widget': custom_widget})