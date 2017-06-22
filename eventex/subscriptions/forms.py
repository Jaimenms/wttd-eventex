from django import forms
from django.core.exceptions import ValidationError

from eventex.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name','cpf','email','phone']

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        self.cleaned_data = super().clean()

        phone= self.cleaned_data.get('phone')
        email = self.cleaned_data.get('email')
        if not phone and not email:
            raise ValidationError('Informe seu email ou telefone.', 'all')

        return self.cleaned_data