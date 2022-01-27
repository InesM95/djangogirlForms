from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_email(value):
    if "@" in value:
        domain = value.split('@')[1]
        domain_list = ["softcatalyst.com", ]
        if domain not in domain_list:
            raise ValidationError(
                _('%(value)s Email is invalid. The email should be a softcatalyst email'),
                params={'value': value},
            )
