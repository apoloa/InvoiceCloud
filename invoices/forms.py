# -*- coding: utf-8 -*-

from django import forms


class EFacturaForm(forms.Form):
    file = forms.FileField(label="E-Factura")