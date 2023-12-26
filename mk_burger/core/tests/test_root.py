import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


def test_root(client):
    resp = client.get("/")

    assert resp.status_code == status.HTTP_200_OK
