from django.contrib import admin



# TODO здесь можно подкючить ваши модели к стандартной джанго-админке
from skymarket.ads.models import Ad, Comment

admin.site.register(Ad)
admin.site.register(Comment)
