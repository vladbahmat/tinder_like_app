from model_bakery import baker
import json
import pytest


from .models import Photo

pytestmark = pytest.mark.django_db


class TestPhotosEndPoint():
    endpoint = ('photos')
    photo = baker.prepare(Photo)
    expected_json = {
        'image': photo.image,
        'description': photo.description,
    }

    response = api_client().post(
        endpoint,
        data=expected_json,
        format='json'
    )

    assert response.status_code == 201
    assert json.loads(response.content) == expected_json
