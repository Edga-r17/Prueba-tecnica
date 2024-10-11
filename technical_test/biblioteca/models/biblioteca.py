from django.db import models
from base.models import BaseModel

class Author(BaseModel):
    name = models.CharField('Nommbre',max_length=200, default='', blank=True)
    birth_date = models.DateField('Fecha de Nacimiento')

    def __str__(self):
        return f"{self.id} {self.name}"


class Book(BaseModel):
    title = models.CharField('Titulo', max_length=200, default='', blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, verbose_name='Autor')
    publication_date = models.DateField('Fecha de Publicacion')

    def __str__(self):
        return f"{self.id} {self.title}"
