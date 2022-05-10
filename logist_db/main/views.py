from django.shortcuts import render
from .models import *
from .forms import Filters
from itertools import chain


# Create your views here.
def index(request):
    # if request.method == 'POST':
    #     form = Filters(request.POST)
    #     if form.is_valid():
    #         form.save()
    # form = Filters()
    # context = {
    #     'from': form
    # }
    data = Delivery.objects.select_related('lego', 'regularity')
    transactions = Transactions.objects.select_related('option')
    shop = Shop.objects.select_related('city')
    final_queryset = list(chain(data, transactions, shop))
    # print(final_queryset)
    # data = Delivery.objects.all()
    # print(str(data.query))
    for el in final_queryset:
        print(el)
        # print(el.shop.city,
        #       el.shop.telephone,
        #       # el.transactions.option,
        #       el.regularity,
        #       el.logistic_company,
        #       el.lego.title, sep='-')

        # print(f'{el.logistic_company} и {i.deadlines}')
    info = {'title': 'А ведь тут могли быть фильтры', 'data': data}
    # return render(request, 'main/index.html', info)
