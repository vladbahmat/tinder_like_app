from model_bakery import baker
import json
import pytest


from .models import User

pytestmark = pytest.mark.django_db

class TestUsersEndpoints():

    def test_show(self, api_client):
        user = baker.make(User, _quantity=1)

        response = api_client().get(
            f'users/{user.id}'
        )

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_create(self, api_client):
        currency = baker.prepare(User)
        expected_json = {
            'username': currency.name,
            'password': currency.code,
        }

        response = api_client().post(
            'users'
            data=expected_json,
            format='json'
        )

        assert response.status_code == 201
        assert json.loads(response.content) == expected_json