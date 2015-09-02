__author__ = 'bmitchem'
from cards.widget import widget

class custom_card(widget):

    def __init__(self):
        self.template = 'demo/custom_card.html'
        self.context = {}
        super(widget, self).__init__()

    def custom_function(self):
        return 'Hola Amigos!'