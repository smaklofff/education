from django.db import models


# Create your models here.
class Lego(models.Model):
    title = models.CharField('Название', max_length=50)
    series = models.CharField('Серия', max_length=50)
    year = models.IntegerField('Год выпуска')
    age = models.IntegerField('Возрастная группа')
    size = models.CharField('Размер', max_length=50)
    exclusive = models.BooleanField('Эксклюзив')
    new = models.BooleanField('Новинка')
    quantity = models.IntegerField('Количество деталей')
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.title


class City(models.Model):
    city = models.CharField('Город', max_length=50, unique=True)

    def __str__(self):
        return self.city


class Regularity(models.Model):
    regularity = models.CharField('Регулярность', max_length=50, unique=True)

    def __str__(self):
        return self.regularity


class Shop(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField('Адрес', max_length=50)
    telephone = models.CharField('Телефон', max_length=50)

    def __str__(self):
        return self.address


class Delivery(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    lego = models.ForeignKey(Lego, on_delete=models.CASCADE)
    logistic_company = models.CharField('Транспортная компания', max_length=50)
    deadlines = models.DateTimeField('Сроки поставки')
    regularity = models.ForeignKey(Regularity, on_delete=models.CASCADE)

    def __str__(self):
        return self.logistic_company


class Options(models.Model):
    options = models.CharField('Вариант оплаты', max_length=50, unique=True)

    def __str__(self):
        return self.options


class Transactions(models.Model):
    option = models.ForeignKey(Options, on_delete=models.CASCADE)
    number = models.ForeignKey(Delivery, on_delete=models.CASCADE)


class Users(models.Model):
    login = models.CharField('Логин', max_length=100, unique=True)
    password = models.CharField('Логин', max_length=100)

    def __str__(self):
        return self.login
