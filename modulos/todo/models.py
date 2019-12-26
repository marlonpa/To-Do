from django.db import models
from django.db.models import ForeignKey

from agenda import settings
from modulos.users.models import Users


class Task(models.Model):
    task_name = models.CharField(max_length=250)
    userid = ForeignKey(Users,
                        verbose_name='Usuario creador',
                        null=True,
                        on_delete=models.SET_NULL)
    estado = models.IntegerField(verbose_name='Estado', default=1)

    def __str__(self):
        return '{},{}'.format(self.task_name, self.userid)
