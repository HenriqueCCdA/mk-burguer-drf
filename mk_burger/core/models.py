from django.db import models

TYPE_NAME_LENGTH = 100


class BaseModel(models.Model):
    created_at = models.DateTimeField("Creation Date and Time", auto_now_add=True)
    modified_at = models.DateTimeField("Modificatioin Date and Time", auto_now=True)

    is_active = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True


class IngredientsBaseModel(BaseModel):
    tipo = models.CharField("Tipo", max_length=TYPE_NAME_LENGTH)

    class Meta:
        ordering = ("tipo",)
        abstract = True

    def __str__(self):
        return self.tipo


class Bread(IngredientsBaseModel):
    ...


class Meat(IngredientsBaseModel):
    ...


class Optional(IngredientsBaseModel):
    ...
