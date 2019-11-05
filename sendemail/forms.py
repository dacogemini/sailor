from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

STATES = (
    ('', 'Choose...'),
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AL', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District Of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT',  'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('MT', 'Montana'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VA', 'Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming')
)


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size': 25}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size': 25}))
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'size': 25}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'size': 25}))
    message = forms.CharField(widget=forms.Textarea, required=True)
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'size': 50})
    )

    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-lg-6col-md-8'),
                Column('last_name', css_class='form-group col-lg-6 col-md-8'),
                Column('from_email', css_class='form-group col-lg-12 col-md-8'),
                Column('subject', css_class='form-group col-lg-12 col-md-8'),
                css_class='form-row'
            ),
            'address_1',

            Row(
                Column('city', css_class='form-group col-md-12 mb-0'),
                Column('state', css_class='form-group col-lg-12 mb-0'),
                Column('zip_code', css_class='form-group col-md-12 mb-0'),
                Column('message', css_class='form-group col-lg-12 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'SEND')
        )
