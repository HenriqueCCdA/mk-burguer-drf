import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from mk_burger.core.models import Bread, Meat, Optional

URL = resolve_url("core:ingredientes")


@pytest.fixture
def breads(db):
    Bread.objects.create(tipo="Italiano Branco")
    Bread.objects.create(tipo="3 Queijos")
    return Bread.objects.all()


@pytest.fixture
def meats(db):
    Meat.objects.create(tipo="Maminha")
    Meat.objects.create(tipo="Alcatra")
    Meat.objects.create(tipo="Picanha")
    return Meat.objects.all()


@pytest.fixture
def optionais(db):
    Optional.objects.create(tipo="Bacon")
    return Optional.objects.all()


def test_ingredientes_list(client, breads, meats, optionais):
    resp = client.get(URL)

    assert resp.status_code == status.HTTP_200_OK

    body = resp.json()

    # paes

    assert len(body["paes"]) == 2

    for r, e in zip(body["paes"], breads):
        assert r["id"] == e.id
        assert r["tipo"] == e.tipo

    # meat

    assert len(body["carnes"]) == 3

    for r, e in zip(body["carnes"], meats):
        assert r["id"] == e.id
        assert r["tipo"] == e.tipo

    # optianal

    assert len(body["opcionais"]) == 1

    for r, e in zip(body["opcionais"], optionais):
        assert r["id"] == e.id
        assert r["tipo"] == e.tipo
