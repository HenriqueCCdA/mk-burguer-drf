from datetime import datetime

import pytest


@pytest.mark.unity
def test_model_fiels(burger):
    assert burger._meta.get_field("name")
    assert burger._meta.get_field("meat")
    assert burger._meta.get_field("bread")
    assert burger._meta.get_field("optionais")
    assert burger._meta.get_field("status")
    assert burger._meta.get_field("is_active")
    assert burger._meta.get_field("created_at")
    assert burger._meta.get_field("modified_at")


@pytest.mark.unity
def test_create_at_and_modified_at(burger):
    assert isinstance(burger.created_at, datetime)
    assert isinstance(burger.modified_at, datetime)


@pytest.mark.unity
def test_str(burger):
    assert str(burger) == burger.name


@pytest.mark.unity
def test_default(burger):
    assert burger.is_active
