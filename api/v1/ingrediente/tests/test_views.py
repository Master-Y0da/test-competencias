import pytest
from rest_framework.test import APIClient


client = APIClient()

@pytest.mark.django_db
def test_create_ingrediente():
    response = client.post(
        '/api/v1/ingredientes/',
        {
            'nombre': 'Papa',
            'is_vegan': True,
            'is_gluten_free': True,
            'is_kosher': True
        },
        format='json'
    )
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_ingredientes():
    response = client.get('/api/v1/ingredientes/')
    assert response.status_code == 200
    assert isinstance(response.data, list)