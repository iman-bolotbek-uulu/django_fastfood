from django.db import models
from django.utils import timezone
from datetime import datetime


class User(models.Model):
    email = models.CharField(max_length=255, verbose_name='Email')
    password = models.CharField(max_length=255, verbose_name='Password')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Client')
    card_number = models.CharField(max_length=16, verbose_name='Card')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Worker')
    position = models.CharField(max_length=255, verbose_name='Position')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Worker'
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'


class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ingredient')
    extra_price = models.IntegerField(verbose_name='Price for extra ingredients')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Ingredient'
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'


class Food(models.Model):
    name = models.CharField(max_length=255, verbose_name='Food')
    start_price = models.IntegerField(verbose_name='Basic price')
    booking = models.ManyToManyField(Ingredient, related_name='meal', through='Order')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Food'
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'


class Order(models.Model):
    eat = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(verbose_name='Time of oder', auto_now_add=True)

    def __str__(self):
        return f'{self.ingredient} - {self.eat} - {self.client} - {self.worker} - {self.order_date_time}'

    class Meta:
        db_table = 'Order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'








