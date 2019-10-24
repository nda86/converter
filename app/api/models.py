from django.db import models


# модель ВАЛЮТА, содержит поле имя, а также ключевое поле id, которо джанго добавляет по умолчангию всем моделям
class Currency(models.Model):
    name = models.CharField(max_length=64, unique=True)

# модель для хранения курсов валют
class Rate(models.Model):
    currency_id = models.ForeignKey(Currency, on_delete=models.PROTECT)
    date = models.DateTimeField()
    rate = models.FloatField()
    volume = models.FloatField()