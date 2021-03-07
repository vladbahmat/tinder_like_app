from model_bakery import baker
import json
import pytest


from .models import Subscribe

pytestmark = pytest.mark.django_db

class TestSubscribeEndPoint():
    endpoint = ('subscribe')
    def test_update(self, rf, api_client):
        old_subscribe = baker.make(Subscribe)
        new_subscribe = baker.prepare(Subscribe)
        subscribe_dict = {
            'name': new_subscribe.name,
            'swipes': new_subscribe.swipes,
            'radius': new_subscribe.radius
        }

        response = api_client().put(
            endpoint,
            subscribe_dict,
            format='json'
        )

        assert response.status_code == 200
        assert json.loads(response.content) == subscribe_dict
