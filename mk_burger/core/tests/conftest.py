import pytest
from rest_framework.test import APIClient

from mk_burger.core.models import Bread, Meat, Optional


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
def optionais(db):
    Optional.objects.create(tipo="Bacon")
    return Optional.objects.all()
