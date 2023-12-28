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
