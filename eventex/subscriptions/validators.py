from django.core.exceptions import ValidationError

from brcpftester import BrazilianCpfValidationTests


def validate_cpf(value):

    cpf = BrazilianCpfValidationTests()

    cpf(value)

    for test in cpf.tests:
        raise ValidationError(cpf.GetMessage(test), test)
