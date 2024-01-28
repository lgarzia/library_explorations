import pytest
from tutorials import get_service_level


@pytest.mark.parametrize('user_data, expected', [
    ({'subscription': 'free', 'msg_type': 'info'}, 0),
    ({'subscription': 'free', 'msg_type': 'error'}, 1),
    ({'subscription': 'premium', 'msg_type': 'error'}, 2),
])
def test_get_service_level(user_data, expected):
    assert get_service_level(user_data) == expected
