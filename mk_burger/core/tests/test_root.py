import pytest
from rest_framework import status


@pytest.mark.integration
def test_root(client):
    resp = client.get("/")

    assert resp.status_code == status.HTTP_200_OK
