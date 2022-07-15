from main import app
from unittest.mock import Mock
import pytest

@pytest.mark.parametrize('name, code',(
    ('/', 200),
    ('/popular/', 200),
    ('/nowplaying/', 200),
    ('/toprated/', 200),
    ('/upcoming/', 200),
    ('/popular/', 200),
    ('/search', 200),
    ('/today', 200)
))


def test_websites(name, code, monkeypatch):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("main.popular", api_mock)
    with app.test_client() as client:
        response = client.get(name)
        assert response.status_code == code