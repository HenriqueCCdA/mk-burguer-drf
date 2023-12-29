from django.db import models

TYPE_NAME_LENGTH = 100


class BaseModel(models.Model):
    created_at = models.DateTimeField("Creation Date and Time", auto_now_add=True)
    modified_at = models.DateTimeField("Modificatioin Date and Time", auto_now=True)

    is_active = models.BooleanField("Ativo", default=True)

    class Meta:
        abstract = True


class AbastracBaseModel(BaseModel):
    tipo = models.CharField("Tipo", max_length=TYPE_NAME_LENGTH)

    class Meta:
        ordering = ("tipo",)
        abstract = True

    def __str__(self):
        return self.tipo


class Bread(AbastracBaseModel):
    ...


class Meat(AbastracBaseModel):
    ...


class Optional(AbastracBaseModel):
    class Meta:
        ordering = ("tipo",)
        verbose_name_plural = "Optional"


class Status(AbastracBaseModel):
    class Meta:
        ordering = ("tipo",)
        verbose_name_plural = "status"


class Burger(BaseModel):
    name = models.CharField("nome", max_length=50)

    meat = models.ForeignKey(Meat, verbose_name="carne", on_delete=models.CASCADE)
    bread = models.ForeignKey(Bread, verbose_name="pao", on_delete=models.CASCADE)
    status = models.ForeignKey(Status, verbose_name="status", on_delete=models.CASCADE)

    optionais = models.ManyToManyField(Optional, verbose_name="opcionais")

    def __str__(self):
        return self.name
