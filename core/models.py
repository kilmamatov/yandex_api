from django.db import models


class Weather(models.Model):
    local = models.CharField('Город', max_length=255)
    now_dt = models.DateField('Дата запроса', auto_now_add=True)
    data = models.JSONField(blank=True, null=True)

    class Meta:
        ordering = ('now_dt',)
        verbose_name = 'Погода'
        verbose_name_plural = 'Список прогноза погоды'

    def __str__(self):
        return f'{self.local}'


class SearchWeather(models.Model):
    local = models.CharField('Город', max_length=255)
    count = models.IntegerField()

    class Meta:
        verbose_name = 'Запрос к апи'
        verbose_name_plural = 'Список'



