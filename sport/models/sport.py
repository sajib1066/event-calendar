from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Trainer(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    direction = models.ManyToManyField('Direction', related_name='trainers')
    qualification = models.TextField(verbose_name="Квалификация", **NULLABLE)
    achievements = models.TextField(verbose_name="Достижения", **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'


class Direction(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'
