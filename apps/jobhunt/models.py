from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Company(BaseModel):
    name = models.CharField(_('Name'), max_length=40)
    about = models.TextField(_('About'))

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.name
    

class Vacancy(BaseModel):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name=_('Company'),
        related_name='vacancies'
    )
    description = models.TextField(_('Description'))

    class Meta:
        verbose_name = _('Vacancy')
        verbose_name_plural = _('Vacancies')

    def __str__(self):
        return self.description
    

class JobHunter(BaseModel):
    full_name = models.CharField(_('Full name'), max_length=100)
    cv = models.FileField(_('CV'), upload_to='cv/')

    class Meta:
        verbose_name = 'Job hunter'
        verbose_name_plural = 'Job hunters'

    def __str__(self):
        return self.full_name