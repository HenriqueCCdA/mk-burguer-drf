from django.shortcuts import resolve_url
from rest_framework import status


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

    assert len(body["opcionais"]) == 1

    for r, e in zip(body["opcionais"], optionais):
        assert r["id"] == e.id
        assert r["tipo"] == e.tipo


def test_status_list(client, status_list):
    resp = client.get(resolve_url("core:status"))

    assert resp.status_code == status.HTTP_200_OK

    body = resp.json()

    assert len(body) == 3

    for r, e in zip(body, status_list):
        assert r["id"] == e.id
        assert r["tipo"] == e.tipo
