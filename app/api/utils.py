"""вспомогательный модуль, в него вынесена вся основная логика работы с базой данных
и полготовке ответа на рест запрос. данные функции вызываются из модуля views."""
import requests
from datetime import datetime
from .models import Currency, Rate

# список загружаемых валют
curr = ["BTC", "ETH", "XRP", "EOS", "BCH"]


# функция запрашивает по апи данные валют на бирже, обрабатывает полученные данные и записывает их в локальную базу данных
def update_base():
    now = datetime.strftime(datetime.now(), "%d.%m.%Y")
    for val in curr:
        Currency.objects.update_or_create(name=val)
        url = f"https://api-pub.bitfinex.com/v2/candles/trade:1D:t{val}USD/hist?limit=10"
        data = requests.get(url).json()
        for item in data:
            currency_id = Currency.objects.filter(name=val).first()
            date = datetime.fromtimestamp(item[0]/1000.0)
            rate_close = item[2]
            volume = item[5]
            obj = {"currency_id": currency_id, "date": date, "rate": rate_close, "volume": volume}
            updated = Rate.objects.filter(currency_id=currency_id, date=date).first()
            if updated:
                continue
            Rate.objects.create(**obj)
    return {"updated": "success", "date": now}



# функция принимает ид запрашиваемой валюты. берет из базы последний курс валюты
# и высчитывает средний объем продаж за 10 дней
def get_rate(cur_id):
    if cur_id == "":
        return {"error": "currencie_id is must send"}
    cur = Currency.objects.filter(id=cur_id).first()
    if cur is None:
        return {"error": "currencie id not found."}
    objs = Rate.objects.filter(currency_id=cur_id).order_by("-date")[:10]
    name = cur.name
    rate = objs[0].rate
    vol = 0
    for obj in objs:
        vol += obj.volume
    vol = vol / 10.0
    return {"name": name, "last_rate": rate, "avg_volume": vol}




