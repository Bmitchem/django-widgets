from urlparse import urljoin
from django.template import Context
from django.template.backends.django import Template
from django.template.loader import get_template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

__author__ = 'bmitchem'

from django.forms.widgets import Media
from django.forms import forms
from django.conf import settings

class widget(object):

    def __init__(self, css=None, js=None, template=None, context={}):
        self._css = css
        self._js = js
        self.template = template
        self.context = context

    def render(self):
        return self.render_html()

    def __str__(self):
        return self.render()

    def render_css(self):
        if self._css:
            return format_html(
                    '<link href="{}" type="text/css" rel="stylesheet" />',
                    self.absolute_path(self._css)
                )
        else:
            return "<!-- no css -->"


    def render_js(self):
        if self._js:
            return format_html(
                '<script type="text/javascript" src="{}"></script>',
                self.absolute_path(self._js)
            )
        else:
            return "<!-- no js -->"


    def render_html(self):
        template = get_template(self.template)
        context = Context(self.context)
        return mark_safe(template.render(context))

    def absolute_path(self, path, prefix=None):
        if path.startswith(('http://', 'https://', '/')):
            return path
        if prefix is None:
            if settings.STATIC_URL is None:
                # backwards compatibility
                prefix = settings.MEDIA_URL
            else:
                prefix = settings.STATIC_URL
        return urljoin(prefix, path)











