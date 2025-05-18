from django import forms
from django.forms import Widget
from django.utils.safestring import mark_safe


class TextInputWidget(Widget):
    """Виджет для всех input с текстом или числами"""
        
    def __init__(
            self, 
            base_widget, 
            label: str,
            id: str,
            help_text: str = None,
            required: bool = False,
            *args, **kwargs
            ):
        u"""Initialise widget and get base instance"""
        super(TextInputWidget, self).__init__(*args, **kwargs)
        self.base_widget = base_widget(*args, **kwargs)
        self.label = label
        self.help_text = help_text
        self.required = required
        self.id = id

    def render(self, name, value, attrs=None, renderer=None):
        u"""Render base widget and add bootstrap spans"""
        field = self.base_widget.render(name, value, {'class': 'form-control', 'id': self.id})
        help_text = f'<small id="emailHelp" class="form-text text-muted">{self.help_text}</small>' if self.help_text else ''
        label = f'<label for="{self.id}">{self.label} *</label>' if self.required else f'<label for="{self.id}">{self.label}</label>'
        return mark_safe((
            u'<div class="form-group mb-3">'
            u'  %(label)s'
            u'  %(field)s'
            u'  %(help_text)s'
            u'</div>'
        ) % {
            'label': label,
            'field': field, 
            'help_text': help_text
            })