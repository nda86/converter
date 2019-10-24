from rest_framework import serializers
from .models import Currency


# класс для сериализации джанго объектов, нужен для того чтобы мы могли отправлять в объекты джанго моделей в формате json
# в списке fields указаны поля модели, которые будут конвертирроваться в json
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name',)
        model = Currency
