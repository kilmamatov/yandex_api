from django import forms
from core import models


class Adress(forms.Form):
    local = forms.CharField(max_length=255, label='Адрес', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите Адрес'
        }))
    count = forms.IntegerField(label='Прогноз', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Введите колличество дней'
                                                                              }))


class Searh_history(forms.Form):
    local = forms.CharField(max_length=255, label='Город', required=False,)
    now_dt = forms.DateTimeField(label='Дата', required=False, widget=forms.DateInput(
        attrs={
            'type': 'date',
            'format': '%Y-%m-%d'
        }))


# class Text(forms.Form):
#     text = forms.CharField(max_length=255, label='Текст', widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите содержание'
#         }))
#
#     name = forms.CharField(max_length=255, label='Файл', widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите имя файла'
#         }))





