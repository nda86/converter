import os
import logging.handlers
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from .utils import update_base, get_rate
from .serializer import CurrencySerializer
from .models import Currency


# файл лог журнала, в него записываются ошибки возникаемые в процессе выполнения программы
logger = logging.getLogger(__name__)
file_handler = logging.handlers.RotatingFileHandler(filename=os.path.join("main.log"))
logger.addHandler(file_handler)

# вью класс, принимает рест запрос на обновление бд с клиента
class Update(APIView):
    @staticmethod
    def get(request):
        try:
            data = update_base()
            return JsonResponse(data, safe=False)
        except Exception as er:
            logger.exception(er)
            return JsonResponse({"error": "server error. please update base and repeat later"})

# класс для обработки рест запроса на вывод всех валют из бд
class ListCurrencies(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


# класс для обработки рест запроса /rate
class Rate(APIView):
    @staticmethod
    def get(request, cur_id):
        try:
            data = get_rate(cur_id)
            return JsonResponse(data, safe=False)
        except Exception as er:
            logger.exception(er)
            return JsonResponse({"error": "server error. please update base and repeat later"})

