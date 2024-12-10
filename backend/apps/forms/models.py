from django.db import models
# from phonenumber_field import modelfields


class MyForm(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256, verbose_name='Имя формы', null=True)
    date = models.CharField(max_length=256,verbose_name='Дата',blank=True, null=True)
    phone = models.CharField(max_length=256,verbose_name='Телефон',blank=True, null=True)
    email = models.CharField(max_length=256,verbose_name='Почта',blank=True, null=True)
    text = models.CharField(max_length=256,verbose_name='Текст',blank=True, null=True)