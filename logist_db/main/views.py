from django.views.generic import DeleteView
from django.views.generic.list import *
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
    info = {'title': 'Фильтры:',
            'data': list(data),
            'form': form}
    return render(request, 'main/index.html', info)


def clean_form(form, range_date):
    cleaned_form, order_list = {}, []
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
    if data:
        return redirect('add')
    else:
        info = {
            'title': 'Отправленные данные',
            'form': form
        }
        return render(request, 'main/moderator.html', info)


def add(request):
    if request.method == 'POST':
        if 'b_lego' in request.POST:
            form_lego = LegoFrom(request.POST)
            if form_lego.is_valid():
                form_lego.save()
        else:
            form_lego = LegoFrom()

        if 'b_city' in request.POST:
            form_city = CityFrom(request.POST)
            if form_city.is_valid():
                form_city.save()
        else:
            form_city = CityFrom()

        if 'b_regularity' in request.POST:
            form_regularity = RegularityFrom(request.POST)
            if form_regularity.is_valid():
                form_regularity.save()
        else:
            form_regularity = RegularityFrom()

        if 'b_shop' in request.POST:
            form_shop = ShopFrom(request.POST)
            if form_shop.is_valid():
                form_shop.save()
        else:
            form_shop = ShopFrom()

        if 'b_delivery' in request.POST:
            form_delivery = DeliveryFrom(request.POST)
            if form_delivery.is_valid():
                form_delivery.save()
        else:
            form_delivery = DeliveryFrom()

        if 'b_options' in request.POST:
            form_option = OptionsFrom(request.POST)
            if form_option.is_valid():
                form_option.save()
        else:
            form_option = OptionsFrom()

        if 'b_transactions' in request.POST:
            form_transactions = TransactionsFrom(request.POST)
            if form_transactions.is_valid():
                form_transactions.save()
        else:
            form_transactions = TransactionsFrom()

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
    return render(request, 'main/moder_create.html', info)


def edit(request):
    if 'edit_lego' in request.POST:
        print(request.POST.get(request.POST.get('edit_lego')))
        lego_data = Lego.objects.get(id=request.POST['edit_lego'])
        lego_data.title = request.POST[request.POST['edit_lego']]
        lego_data.age = request.POST[request.POST['edit_lego']]
        lego_data.size = request.POST[request.POST['edit_lego']]
        lego_data.exclusive = request.POST[request.POST['edit_lego']]
        lego_data.new = request.POST[request.POST['edit_lego']]
        lego_data.quantity = request.POST[request.POST['edit_lego']]
        lego_data.price = request.POST[request.POST['edit_lego']]
        lego_data.save()
    if 'edit_city' in request.POST:
        city_data = City.objects.get(id=request.POST['edit_city'])
        city_data.city = request.POST[request.POST['edit_city']]
        city_data.save()
    if 'edit_regularity' in request.POST:
        regularity_data = Regularity.objects.get(id=request.POST['edit_regularity'])
        regularity_data.regularity = request.POST[request.POST['edit_regularity']]
        regularity_data.save()
    if 'edit_shop' in request.POST:
        shop_data = Shop.objects.get(id=request.POST['edit_shop'])
        shop_data.city = request.POST[request.POST['edit_shop']]
        shop_data.address = request.POST[request.POST['edit_shop']]
        shop_data.telephone = request.POST[request.POST['edit_shop']]
        shop_data.save()
    if 'edit_delivery' in request.POST:
        delivery_data = Delivery.objects.get(id=request.POST['edit_delivery'])
        delivery_data.shop = request.POST[request.POST['edit_delivery']]
        delivery_data.lego = request.POST[request.POST['edit_delivery']]
        delivery_data.logistic_company = request.POST[request.POST['edit_delivery']]
        delivery_data.deadlines = request.POST[request.POST['edit_delivery']]
        delivery_data.regularity = request.POST[request.POST['edit_delivery']]
        delivery_data.save()
    if 'edit_options' in request.POST:
        options_data = Options.objects.get(id=request.POST['edit_options'])
        options_data.options = request.POST[request.POST['edit_options']]
        options_data.save()
    if 'edit_transactions' in request.POST:
        transactions_data = Transactions.objects.get(id=request.POST['edit_transactions'])
        transactions_data.option = request.POST[request.POST['edit_transactions']]
        transactions_data.number = request.POST[request.POST['edit_transactions']]
        transactions_data.save()
    lego_data = Lego.objects.all()
    city_data = City.objects.all()
    regularity_data = Regularity.objects.all()
    shop_data = Shop.objects.all()
    delivery_data = Delivery.objects.all()
    options_data = Options.objects.all()
    transactions_data = Transactions.objects.all()
    info = {
        'title': 'Удаление данных',
        'lego_data': lego_data,
        'city_data': city_data,
        'regularity_data': regularity_data,
        'shop_data': shop_data,
        'delivery_data': delivery_data,
        'options_data': options_data,
        'transactions_data': transactions_data,
    }
    return render(request, 'main/moder_edit.html', info)


def delete(request):
    if 'delete_lego' in request.POST:
        lego_data = Lego.objects.get(id=request.POST['delete_lego'])
        lego_data.delete()
    if 'delete_city' in request.POST:
        city_data = City.objects.get(id=request.POST['delete_city'])
        city_data.delete()
    if 'delete_regularity' in request.POST:
        regularity_data = Regularity.objects.get(id=request.POST['delete_regularity'])
        regularity_data.delete()
    if 'delete_shop' in request.POST:
        shop_data = Shop.objects.get(id=request.POST['delete_shop'])
        shop_data.delete()
    if 'delete_delivery' in request.POST:
        delivery_data = Delivery.objects.get(id=request.POST['delete_delivery'])
        delivery_data.delete()
    if 'delete_options' in request.POST:
        options_data = Options.objects.get(id=request.POST['delete_options'])
        options_data.delete()
    if 'delete_transactions' in request.POST:
        transactions_data = Transactions.objects.get(id=request.POST['delete_transactions'])
        transactions_data.delete()
    lego_data = Lego.objects.all()
    city_data = City.objects.all()
    regularity_data = Regularity.objects.all()
    shop_data = Shop.objects.all()
    delivery_data = Delivery.objects.all()
    options_data = Options.objects.all()
    transactions_data = Transactions.objects.all()
    info = {
        'title': 'Удаление данных',
        'lego_data': lego_data,
        'city_data': city_data,
        'regularity_data': regularity_data,
        'shop_data': shop_data,
        'delivery_data': delivery_data,
        'options_data': options_data,
        'transactions_data': transactions_data,
    }
    return render(request, 'main/moder_delete.html', info)

#
# class LegoViews(DeleteView):
#     model = Lego
#     success_url = 'main/moder_create.html'
#     template_name = 'main/moder_delete.html'
