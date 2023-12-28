from datetime import datetime

import pytest


@pytest.mark.unity
def test_model_fiels(status_burger):
    assert status_burger._meta.get_field("tipo")
    assert status_burger._meta.get_field("is_active")
    assert status_burger._meta.get_field("created_at")
    assert status_burger._meta.get_field("modified_at")


@pytest.mark.unity
def test_create_at_and_modified_at(status_burger):
    assert isinstance(status_burger.created_at, datetime)
    assert isinstance(status_burger.modified_at, datetime)


@pytest.mark.unity
def test_str(status_burger):
    assert str(status_burger) == status_burger.tipo


@pytest.mark.unity
def test_default(status_burger):
    assert status_burger.is_active
