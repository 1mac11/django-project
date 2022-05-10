from typing import (
    Dict,
    Any,
)
import json
import pytest
from django.core.management import call_command
from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        print(settings.BASE_DIR)
        call_command('loaddata', settings.BASE_DIR / 'tests' / 'fixture.json')


def get_json(path: str) -> Dict[Any, Any]:
    try:
        with open(f'{path}.json', encoding='utf-8') as f:
            return json.loads(f.read())
    except (json.JSONDecoder, FileNotFoundError):
        return {}
