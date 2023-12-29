import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from mk_burger.core.models import Burger

URL = resolve_url("core:burger_lc")


@pytest.mark.integration
def test_list_burgers(client, burger_list):
    resp = client.get(URL)

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

    resp = client.post(URL, data=data, format="json")

    assert resp.status_code == status.HTTP_201_CREATED

    body = resp.json()

    burger_db = Burger.objects.first()

    assert burger_db.id == body["id"]
    assert burger_db.name == body["name"]
    assert burger_db.meat.id == body["meat"]
    assert burger_db.bread.id == body["bread"]
    assert burger_db.status.id == body["status"]
    assert list(burger_db.optionais.all().values_list("id", flat=True)) == body["optionais"]
