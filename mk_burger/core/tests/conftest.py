import pytest
from rest_framework.test import APIClient

from mk_burger.core.models import Bread, Burger, Meat, Optional, Status


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def bread(db):
    return Bread.objects.create(tipo="Italiano Branco")


@pytest.fixture
def meat(db):
    return Meat.objects.create(tipo="Maminha")


@pytest.fixture
def optional(db):
    return Optional.objects.create(tipo="Maminha")


@pytest.fixture
def status_burger(db):
    return Status.objects.create(tipo="Solicitado")


@pytest.fixture
def bread_list(db):
    Bread.objects.create(tipo="Italiano Branco")
    Bread.objects.create(tipo="3 Queijos")
    return Bread.objects.all()


@pytest.fixture
def meat_list(db):
    Meat.objects.create(tipo="Maminha")
    Meat.objects.create(tipo="Alcatra")
    Meat.objects.create(tipo="Picanha")
    return Meat.objects.all()


@pytest.fixture
def optionais(db):  # TODO: chamar de optional_list
    Optional.objects.create(tipo="Bacon")
    Optional.objects.create(tipo="Cebola roxa")
    return Optional.objects.all()


@pytest.fixture
def status_list(db):
    Status.objects.create(tipo="Solicitado")
    Status.objects.create(tipo="Em produção")
    Status.objects.create(tipo="Finalizado")
    return Status.objects.all()


@pytest.fixture
def burger(bread_list, meat_list, optionais, status_list):
    burger = Burger.objects.create(name="Henrique", bread=bread_list[0], meat=meat_list[0], status=status_list[0])
    burger.optionais.add(*optionais)

    return burger


@pytest.fixture
def burger_list(bread_list, meat_list, optionais, status_list):
    burger = Burger.objects.create(name="Henrique", bread=bread_list[0], meat=meat_list[0], status=status_list[0])
    burger.optionais.add(*optionais)

    burger = Burger.objects.create(name="Joao", bread=bread_list[1], meat=meat_list[1], status=status_list[1])
    burger.optionais.add(optionais[0])

    return Burger.objects.all()
