import pytest


@pytest.mark.django_db
def test_fixture(client):
    assert True
