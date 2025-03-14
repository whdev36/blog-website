from django import forms
from .models import Blogger
from django.contrib.auth.forms import UserCreationForm
from .form_attrs import field_attrs
from django.utils.safestring import mark_safe

class BloggerCreationForm(UserCreationForm):
    class Meta:
        model = Blogger
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field, attrs in field_attrs.items():
            if field in self.fields:
                self.fields[field].widget.attrs.update({
                    'placeholder': attrs['placeholder'],
                    'class': 'form-control',
                })
            self.fields[field].label = attrs['label']
            self.fields[field].label_suffix = ' *'
            self.fields[field].help_text = attrs['help_text']
            self.fields[field].error_messages = attrs['error_messages']

    def as_div(self):
        return mark_safe(
            '\n'.join(
                f'<div class="form-group mb-3">'
                f'{field.label_tag()}{field}'
                f'{"".join(f"<div class=\"text-danger\">{error}</div>" for error in field.errors)}'
                f'</div>'
                if not field.is_hidden else str(field)
                for field in self
            )
        )