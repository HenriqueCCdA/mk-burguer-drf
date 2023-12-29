import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from mk_burger.core.models import Burger


@pytest.mark.integration
def test_ingredientes_list(client, bread_list, meat_list, optionais):
    resp = client.get(resolve_url("core:ingredientes"))

    assert resp.status_code == status.HTTP_200_OK

    body = resp.json()

    # paes

    assert len(body["paes"]) == 2

    for r, e in zip(body["paes"], bread_list):
        assert r["id"] == e.id
        assert r["tipo"] == e.tipo

    # meat

    assert len(body["carnes"]) == 3

    for r, e in zip(body["carnes"], meat_list):
        assert r["id"] == e.id
        assert r["tipo"] == e.tipo

    # optianal

    assert len(body["opcionais"]) == 2

    for r, e in zip(body["opcionais"], optionais):
        assert r["id"] == e.id
        assert r["tipo"] == e.tipo


@pytest.mark.integration
def test_status_list(client, status_list):
    resp = client.get(resolve_url("core:status"))

    assert resp.status_code == status.HTTP_200_OK

    body = resp.json()

    assert len(body) == 3

    for r, e in zip(body, status_list):
        assert r["id"] == e.id
        assert r["tipo"] == e.tipo


@pytest.mark.integration
def test_list_burgers(client, burger_list):
    resp = client.get(resolve_url("core:burger_lc"))

    assert resp.status_code == status.HTTP_200_OK

    body = resp.json()

    assert len(body) == 2

    for e, b in zip(burger_list, body):
        assert e.id == b["id"]
        assert e.name == b["name"]
        assert e.meat.id == b["meat"]
        assert e.bread.id == b["bread"]
        assert e.status.id == b["status"]
        assert list(e.optionais.all().values_list("id", flat=True)) == b["optionais"]


@pytest.mark.integration
def test_create_burgers(client, bread, meat, status_burger, optional):
    data = {
        "name": "Henrique",
        "bread": bread.id,
        "meat": meat.id,
        "status": status_burger.id,
        "optionais": [optional.id],
    }

    resp = client.post(resolve_url("core:burger_lc"), data=data, format="json")

    assert resp.status_code == status.HTTP_201_CREATED

    body = resp.json()

    burger_db = Burger.objects.first()

    assert burger_db.id == body["id"]
    assert burger_db.name == body["name"]
    assert burger_db.meat.id == body["meat"]
    assert burger_db.bread.id == body["bread"]
    assert burger_db.status.id == body["status"]
    assert list(burger_db.optionais.all().values_list("id", flat=True)) == body["optionais"]
