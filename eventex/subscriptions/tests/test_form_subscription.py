from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        form = SubscriptionForm()
        """Form must have 4 fields"""
        self.assertSequenceEqual(['name' ,'cpf' ,'email' ,'phone'] ,list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits"""
        # 12345678901 ABCD5678901
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_must_11_digits(self):
        """CPF must have 11 digits."""
        # 12345678901 1234
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        """Name must be capitalized"""
        # HENRIQUE bastos   ->   Henrique Bastos
        form = self.make_validated_form(name='HENRIQUE bastos')
        self.assertEqual('Henrique Bastos', form.cleaned_data['name'])

    def test_email_is_optional(self):
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        form = self.make_validated_form(phone='',email='')
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormErrorCode(self,form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception_code = errors_list[0].code
        self.assertEqual(code, exception_code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Henrique Bastos', cpf='12345678901',
                    email='henrique@bastos.net', phone='21-999999999')

        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
