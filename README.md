# converter
Сервис курсов валют написан на Python 3.7
Подготовка:
 - создайте бд "demo" в postgres
 - python manage.py makemigrations
 - python manage.py migrate
 - python manage.py createsuperuser
 Работа с сервисом:
  - обновите бд, с биржи bitfinex.com будут загружены данные по 5 валютам за последние 10 дней
   для этого нужно послать REST запрос вида /api/v1/update
  - запросите список валют из локальной бд /api/v1/currencies
  - запросите последний курс и средний объем продаж за 10 дней по конкретной валюте /api/v1/rate/<id_currencie>
  
  Все REST запросы зашишены Basic авторизацией.
  
