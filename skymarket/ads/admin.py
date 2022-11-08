from django.contrib import admin



# TODO здесь можно подкючить ваши модели к стандартной джанго-админке
from ads.models import Comment, Ad

admin.site.register(Ad)
admin.site.register(Comment)
