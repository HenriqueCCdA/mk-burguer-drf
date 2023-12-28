from datetime import datetime

import pytest


@pytest.mark.unity
def test_model_fiels(optional):
    assert optional._meta.get_field("tipo")
    assert optional._meta.get_field("is_active")
    assert optional._meta.get_field("created_at")
    assert optional._meta.get_field("modified_at")


@pytest.mark.unity
def test_create_at_and_modified_at(optional):
    assert isinstance(optional.created_at, datetime)
    assert isinstance(optional.modified_at, datetime)


@pytest.mark.unity
def test_str(optional):
    assert str(optional) == optional.tipo


@pytest.mark.unity
def test_default(optional):
    assert optional.is_active
