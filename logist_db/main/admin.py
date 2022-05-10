from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Lego, City, Regularity, Shop, Delivery, Options, Transactions])
