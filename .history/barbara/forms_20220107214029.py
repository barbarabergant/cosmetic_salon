from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _

OPTIONS = (
    ('', _('Izberi...')),
    ('Google', 'Google'),
    ('Facebook', 'Facebook'),
    ('MojaDejavnost.si', 'MojaDejavnost.si'),
    ('prijatelj/znanec', _('prijatelj/znanec')),
    ('drugo', _('drugo'))
)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label =  _('Ime in priimek'))
    number = forms.CharField(max_length=15, required=True, label = _('Telefonska številka'))
    email = forms.EmailField(max_length=100, required=True, label = _("E-pošta"))
    reputation = forms.ChoiceField(choices=OPTIONS, required=False, label= _("Kako si slišal zame"))
    message = forms.CharField(widget=forms.Textarea, max_length=2000, required=True, label= _("Sporočilo"))
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Row(
                    Column('name', css_class='form-group col-md-6 mb-0'),
                    Column('number', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                 Row(
                    Column('email', css_class='form-group col-md-6 mb-0'),
                    Column('reputation', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                'message',
                Submit('submit', _('Pošlji'))
            )