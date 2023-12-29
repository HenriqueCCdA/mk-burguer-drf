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
        assert e.nome == b["nome"]
        assert e.carne.tipo == b["carne"]
        assert e.pao.tipo == b["pao"]
        assert e.status.tipo == b["status"]
        assert list(e.opcionais.all().values_list("tipo", flat=True)) == b["opcionais"]


@pytest.mark.integration
def test_positive_create_burgers(client, bread, meat, status_burger, optional):
    data = {
        "nome": "Henrique",
        "pao": bread.id,
        "carne": meat.id,
        "status": status_burger.id,
        "opcionais": [optional.id],
    }

    resp = client.post(URL, data=data, format="json")

    assert resp.status_code == status.HTTP_201_CREATED

    body = resp.json()

    burger_db = Burger.objects.first()

    assert burger_db.id == body["id"]
    assert burger_db.nome == body["nome"]
    assert burger_db.carne.tipo == body["carne"]
    assert burger_db.pao.tipo == body["pao"]
    assert burger_db.status.tipo == body["status"]
    assert list(burger_db.opcionais.all().values_list("tipo", flat=True)) == body["opcionais"]


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
    assert body["nome"] == burger.nome
    assert body["pao"] == burger.pao.tipo
    assert body["carne"] == burger.carne.tipo
    assert body["status"] == burger.status.tipo
    assert body["opcionais"] == list(burger.opcionais.all().values_list("tipo", flat=True))


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
    assert body["nome"] == burger.nome
    assert body["pao"] == burger.pao.tipo
    assert body["carne"] == burger.carne.tipo
    assert body["status"] == new_status.tipo
    assert body["opcionais"] == list(burger.opcionais.all().values_list("tipo", flat=True))


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
