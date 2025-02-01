import pytest
from rest_framework.test import APIClient
from api.v1.plato.models import Plato
from api.v1.ingrediente.models import Ingrediente


client = APIClient()


@pytest.fixture
def create_dos_ingredientes():
    ing1 = client.post(
        '/api/v1/ingredientes/',
        {
            'nombre': 'Papa',
            'is_vegan': True,
            'is_gluten_free': True,
            'is_kosher': True
        },
        format='json'
    )
    ing2 = client.post(
        '/api/v1/ingredientes/',
        {
            'nombre': 'Carne',
            'is_vegan': False,
            'is_gluten_free': True,
            'is_kosher': False
        },
        format='json'
    )

    return [ing1, ing2]



@pytest.mark.django_db
def test_create_plato(create_dos_ingredientes):

    ingredientes = create_dos_ingredientes

    response = client.post(
        '/api/v1/platos/',
        {
            'name': 'Papa Rellena',
            'ingredients': [ingredientes[0].data['id'], ingredientes[1].data['id']]
        },
        format='json'
    )

    assert response.status_code == 201
    assert [1, 2] == response.data['ingredients']
    assert all(key in response.data for key in ['is_vegan', 'is_gluten_free', 'is_kosher'])


@pytest.mark.django_db
def test_get_single_plato(create_dos_ingredientes):
    ingredientes = create_dos_ingredientes

    plato = client.post(
        '/api/v1/platos/',
        {
            'name': 'Papa Rellena',
            'ingredients': [ingredientes[0].data['id'], ingredientes[1].data['id']]
        },
        format='json'
    )
    platos = client.get('/api/v1/platos/{}/'.format(plato.data['id']))
    assert platos.status_code == 200
    assert platos.data['ingredients'] == [1, 2]
    assert all(key in platos.data for key in ['is_vegan', 'is_gluten_free', 'is_kosher'])


@pytest.mark.django_db
def test_check_n_plus_one_problem(django_assert_num_queries, create_dos_ingredientes):

    ingredientes = create_dos_ingredientes

    plato = client.post(
        '/api/v1/platos/',
        {
            'name': 'Papa Rellena',
            'ingredients': [ingredientes[0].data['id'], ingredientes[1].data['id']]
        },
        format='json'
    )

    #Esperamos 2 querys, debido a que el prefetch_related genera una para el modelo principal y otra para los ingredientes
    with django_assert_num_queries(2):
        platos = client.get('/api/v1/platos/')
    
    assert platos.status_code == 200


