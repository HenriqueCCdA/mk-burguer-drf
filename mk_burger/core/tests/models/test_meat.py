from datetime import datetime

import pytest


@pytest.mark.unity
def test_model_fiels(meat):
    assert meat._meta.get_field("tipo")
    assert meat._meta.get_field("is_active")
    assert meat._meta.get_field("created_at")
    assert meat._meta.get_field("modified_at")


@pytest.mark.unity
def test_create_at_and_modified_at(meat):
    assert isinstance(meat.created_at, datetime)
    assert isinstance(meat.modified_at, datetime)


@pytest.mark.unity
def test_str(meat):
    assert str(meat) == meat.tipo


@pytest.mark.unity
def test_default(meat):
    assert meat.is_active
