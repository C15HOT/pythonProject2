from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, db_index=True, verbose_name='Заголовок')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None,
                               null=True, on_delete=models.CASCADE,
                               related_name='advertisements', verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']

class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Authors(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='ФИО')
    email = models.EmailField()
    phone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return self.name


