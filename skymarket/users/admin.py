from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# TODO Aдмика для пользователя - как реализовать ее можно подсмотреть в документаци django
# TODO Обычно её всегда оформляют, но в текущей задачи делать её не обязательно
from skymarket.ads.views import User

admin.site.register(User)