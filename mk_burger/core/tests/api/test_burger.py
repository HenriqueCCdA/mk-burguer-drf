import pytest
from django.shortcuts import resolve_url
from rest_framework import status

from mk_burger.core.models import Burger

URL = resolve_url("core:burger-list-create")


@pytest.mark.integration
def test_positive_list_burgers(client, burger_list):
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
def test_positive_create_burgers(client, bread, meat, status_burger, optional):
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


@pytest.mark.integration
def test_positive_delete_burgers(client, burger):
    url = resolve_url("core:burger-retrieve-update-destroy", pk=burger.id)

    resp = client.delete(url, id=burger.id)

    assert resp.status_code == status.HTTP_204_NO_CONTENT

    assert not Burger.objects.exists()


@pytest.mark.integration
def test_negative_delete_burgers_wrong_id(client, db):
    url = resolve_url("core:burger-retrieve-update-destroy", pk=404)
    resp = client.delete(url)

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    assert resp.json() == {"detail": "Não encontrado."}


@pytest.mark.integration
def test_positive_get_burgers(client, burger):
    url = resolve_url("core:burger-retrieve-update-destroy", pk=burger.id)

    resp = client.get(url, id=burger.id)

    assert resp.status_code == status.HTTP_200_OK

    body = resp.json()

    assert body["id"] == burger.pk
    assert body["name"] == burger.name
    assert body["bread"] == burger.bread.pk
    assert body["meat"] == burger.meat.pk
    assert body["status"] == burger.status.pk
    assert body["optionais"] == list(burger.optionais.all().values_list("id", flat=True))


@pytest.mark.integration
def test_negative_get_burgers_wrong_id(client, db):
    url = resolve_url("core:burger-retrieve-update-destroy", pk=404)
    resp = client.get(url)

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    assert resp.json() == {"detail": "Não encontrado."}


@pytest.mark.integration
def test_positive_patch_burger(client, burger, status_list):
    new_status = status_list[1]

    url = resolve_url("core:burger-retrieve-update-destroy", pk=burger.id)
    resp = client.patch(url, data={"status": new_status.pk}, format="json")

    assert resp.status_code == status.HTTP_200_OK

    body = resp.json()

    assert body["id"] == burger.pk
    assert body["name"] == burger.name
    assert body["bread"] == burger.bread.pk
    assert body["meat"] == burger.meat.pk
    assert body["status"] == new_status.pk
    assert body["optionais"] == list(burger.optionais.all().values_list("id", flat=True))


@pytest.mark.integration
def test_negative_patch_burgers_wrong_id(client, db):
    url = resolve_url("core:burger-retrieve-update-destroy", pk=404)
    resp = client.patch(url, data={"status": 1}, format="json")

    assert resp.status_code == status.HTTP_404_NOT_FOUND

    assert resp.json() == {"detail": "Não encontrado."}


@pytest.mark.integration
def test_negative_patch_wrong_status_id(client, burger):
    url = resolve_url("core:burger-retrieve-update-destroy", pk=burger.id)
    resp = client.patch(url, data={"status": 404}, format="json")

    assert resp.status_code == status.HTTP_400_BAD_REQUEST

    assert resp.json() == {"status": ['Pk inválido "404" - objeto não existe.']}
