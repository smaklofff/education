from .models import *
from django.forms import Form, CharField, DateField, ModelChoiceField, SelectDateWidget, BooleanField, ModelForm
import datetime


class Filters(Form):
    search_city = CharField(label='Название города:', max_length=100, required=False)
    search_title = CharField(label='Название набора:', max_length=100, required=False)

    from_day = DateField(widget=SelectDateWidget(years=range(2000, datetime.date.today().year + 10)),
                         label="От:",
                         required=False)
    to_day = DateField(widget=SelectDateWidget(years=range(2000, datetime.date.today().year + 10)),
                       label="До:",
                       required=False)

    filter_on_options = ModelChoiceField(label='Способ оплаты:',
                                         required=False,
                                         queryset=Options.objects.all(),
                                         empty_label='Не выбрано')
    filter_on_regularity = ModelChoiceField(label='Регулярность:',
                                            required=False,
                                            queryset=Regularity.objects.all(),
                                            empty_label='Не выбрано')

    order_by_title = BooleanField(label='Сортировка по наборам:', required=False, initial=False)
    order_by_city = BooleanField(label='Сортировка по городам:', required=False, initial=False)
    order_by_company = BooleanField(label='Сортировка по компаниям:', required=False, initial=False)


class Enter(Form):
    login = CharField(label='Логин:', max_length=100, required=False)
    password = CharField(label='Пароль:', max_length=100, required=False)


class LegoFrom(ModelForm):
    class Meta:
        model = Lego
        fields = '__all__'


class CityFrom(ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class RegularityFrom(ModelForm):
    class Meta:
        model = Regularity
        fields = '__all__'


class ShopFrom(ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'


class DeliveryFrom(ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'


class OptionsFrom(ModelForm):
    class Meta:
        model = Options
        fields = '__all__'


class TransactionsFrom(ModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'


