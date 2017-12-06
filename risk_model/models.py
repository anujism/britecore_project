# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class RiskType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class RiskField(models.Model):
    """
    A field abstract -- it describe what the field is.
    It has relationship with risk type - each risk type has multiple fields.
    """
    name = models.CharField(max_length=150)
    label = models.CharField(max_length=150)
    risk_type = models.ForeignKey(RiskType)
    field_type = models.CharField(
        max_length=1,
        choices=(
            ('t', 'Text'),
            ('i', 'Integer'),
            ('b', 'Boolean (Yes/No)'),
            ('s', 'Dropdown Choices'),
            ('d', 'Date'),
        ),
        default='t')
    default_value = models.CharField(
        max_length=5000,
        blank=True,
        help_text="You may leave blank. For Boolean use True or False")
    is_required = models.BooleanField(default=False)
    field_choices = models.CharField(
        max_length=2000,
        blank=True,
        help_text="List the choices you want displayed, seperated by commas. "
        "This is only valid for Dropdown, Multiple, and Checkbox field types",
    )

    def __str__(self):
        return self.name

    def get_form_field(self):
        field_kwargs = {
            'initial': self.default_value,
            'required': self.is_required,
        }
        if self.field_type == "b":
            return forms.BooleanField(**field_kwargs)
        elif self.field_type == "i":
            return forms.IntegerField(**field_kwargs)
        elif self.field_type == "s":
            choices = self.field_choices.split(',')
            if self.is_required is True:
                select_choices = ()
            else:
                select_choices = (('', '---------'),)
            for choice in choices:
                select_choices = select_choices + ((choice, choice),)
            return forms.ChoiceField(
                choices=select_choices, **field_kwargs)
        elif self.field_type == "d":
            return forms.DateField(**field_kwargs)
        return forms.CharField(**field_kwargs)

    class Meta:
        unique_together = ('name', 'risk_type')
