from django.db import models
from base.models import BaseModel


class Tarea(BaseModel):
    title = models.CharField('Titulo', max_length=200, default='', blank=True)
    description = models.TextField('Descripcion',blank=True, null=True)
    completed = models.BooleanField('Completada', default=False)

    def __str__(self):
        return f"{self.id} {self.title}"
