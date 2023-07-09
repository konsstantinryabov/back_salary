from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Salary(models.Model):
    user = models.ForeignKey(User,
                             related_name='salary',
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')

    salar = models.IntegerField('Текущая зарплата')

    date = models.DateField('Дата следующего повышения',
                            auto_now_add=False,
                            auto_now=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Следующее повывшение'
        verbose_name_plural = 'Следующие повывшения'

    # def __str__(self):
    #     return f'{self.salar} {self.date}'
