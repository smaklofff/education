from django.shortcuts import render, redirect
from .models import *
from .forms import *

DEFINITIONS = {
    'search_city': 'number__shop__city__city',
    'order_by_city': 'number__shop__city__city',
    'search_title': 'number__lego__title',
    'order_by_title': 'number__lego__title',
    'order_by_company': 'number__logistic_company',
    'filter_on_options': 'option__options',
    'filter_on_regularity': 'number__regularity__regularity',
    'from_day': 'number__deadlines',
    'to_day': 'number__deadlines'
}


# Create your views here.
def index(request):
    cleaned_form, order_list, range_date = {}, [], [datetime.date(2010, 1, 1), datetime.date(2028, 1, 1)]
    if request.method == 'POST':
        form = Filters(request.POST)
        if form.is_valid():
            cleaned_form, order_list, range_date = clean_form(form.cleaned_data, range_date)
    else:
        form = Filters()
    data = Transactions.objects.values_list(
        'number', 'number__lego__title',
        'number__shop__city__city', 'option__options',
        'number__logistic_company', 'number__deadlines',
        'number__shop__telephone', 'number__regularity__regularity'
    ).filter(**cleaned_form,
             number__deadlines__range=[i.strftime('%Y-%m-%d') for i in range_date]) \
        .order_by(*order_list)
    # .filter(status=9, lego=1, regularity=1)
    # data = ZhanrKino.objects.values_list('zhanr__name', 'kino__title')
    info = {'title': 'Фильтры:',
            'data': list(data),
            'form': form}
    data = {
        'kinos': data
    }
    return render(request, 'main/index.html', info)


def clean_form(form, range_date):
    cleaned_form = {}
    order_list = []
    for key in form:
        if form[key]:
            if key in ['search_city', 'search_title', 'filter_on_options', 'filter_on_regularity']:
                cleaned_form[DEFINITIONS[key]] = form[key]
            if key in ['order_by_title', 'order_by_city', 'order_by_company']:
                order_list.append(DEFINITIONS[key])
            if 'from_day' in key:
                range_date[0] = form[key]
            if 'to_day' in key:
                range_date[1] = form[key]
    return cleaned_form, order_list, range_date


def login(request):
    login_of_user, password_of_user = '', ''
    if request.method == 'POST':
        form = Enter(request.POST)
        if form.is_valid():
            login_of_user = form.cleaned_data['login']
            password_of_user = form.cleaned_data['password']
    else:
        form = Enter()
    data = Users.objects.values_list(
        'login', 'password').filter(login=login_of_user, password=password_of_user)
    info = {
        'title': 'Отправленные данные',
        'form': form
    }
    if data:
        return redirect('add')
        # return render(request, 'main/moder_edit.html')
    else:
        return render(request, 'main/moderator.html', info)


def add(request):
    if request.method == 'POST':
        form_lego = LegoFrom(request.POST)
        form_city = CityFrom(request.POST)
        form_regularity = RegularityFrom(request.POST)
        form_shop = ShopFrom(request.POST)
        form_delivery = DeliveryFrom(request.POST)
        form_option = OptionsFrom(request.POST)
        form_transactions = TransactionsFrom(request.POST)
        if form_lego.is_valid():
            form_lego.save()
        if form_city.is_valid():
            form_city.save()
        if form_regularity.is_valid():
            form_regularity.save()
        if form_shop.is_valid():
            form_shop.save()
        if form_delivery.is_valid():
            form_delivery.save()
        if form_option.is_valid():
            form_option.save()
        if form_transactions.is_valid():
            form_transactions.save()
    else:
        form_lego = LegoFrom()
        form_city = CityFrom()
        form_regularity = RegularityFrom()
        form_shop = ShopFrom()
        form_delivery = DeliveryFrom()
        form_option = OptionsFrom()
        form_transactions = TransactionsFrom()
    info = {
        'title': 'Добавить данные',
        'form_lego': form_lego,
        'form_city': form_city,
        'form_regularity': form_regularity,
        'form_shop': form_shop,
        'form_delivery': form_delivery,
        'form_option': form_option,
        'form_transactions': form_transactions,
    }
    return render(request, 'main/moder_edit.html', info)
