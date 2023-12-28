from datetime import datetime

import pytest


@pytest.mark.unity
def test_model_fiels(bread):
    assert bread._meta.get_field("tipo")
    assert bread._meta.get_field("is_active")
    assert bread._meta.get_field("created_at")
    assert bread._meta.get_field("modified_at")


@pytest.mark.unity
def test_create_at_and_modified_at(bread):
    assert isinstance(bread.created_at, datetime)
    assert isinstance(bread.modified_at, datetime)


@pytest.mark.unity
def test_str(bread):
    assert str(bread) == bread.tipo


@pytest.mark.unity
def test_default(bread):
    assert bread.is_active
