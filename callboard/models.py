from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """Категории объявлений"""
    name = models.CharField('Имя', max_length=50, unique=True)
    slug = models.SlugField('url', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# TODO: Контакты и геолокацию в базе или на фронте? при регистрации пользователя
# class City(models.Model):
#     """Города Узбекистана"""
#     name = models.CharField('Город', max_length=20)
#
#     def __str__(self):
#         return self.name
#
#
# class District(models.Model):
#     """Районы Ташкента"""
#     name = models.CharField('Город', max_length=20)
#
#     def __str__(self):
#         return self.name


class FilterAdvert(models.Model):
    """Фильтры объявлений - купить/продать"""
    name = models.CharField('Имя', max_length=50, unique=True)
    slug = models.SlugField('url', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'


class Advert(models.Model):
    """Объявления"""
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Объявление', max_length=10000)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Дата создания', auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    # city = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE)
    # district = models.ForeignKey(District, verbose_name='Район', on_delete=models.CASCADE)
    filter_advert = models.ForeignKey(FilterAdvert, verbose_name='Фильтр', on_delete=models.CASCADE)
    moderation = models.BooleanField('Модерация', default=False)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    # TODO: активная или архиваная? какое время продумать
    active_or_archive = models.BooleanField('Активное/Архивное', default=True)
    # TODO: как генерировать ссылку на объявление?
    # slug = models.SlugField('url', max_length=50, unique=True)
    # TODO: платные объявления
    is_paid = models.BooleanField('Платное объявление', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
