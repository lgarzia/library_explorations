import pytest
from tutorials import ServiceLevel


@pytest.mark.parametrize('subscription, msg_type, expected', [
    ('free', 'info', 'Level = 0'),
    ('free', 'error', 'Level = 1'),
    ('premium', 'error', 'Level = 2'),
    ('invalid', 'error', 'Provide valid parameters'),
])
def test_get_service_level(subscription, msg_type, expected):
    user_data = {'subscription': subscription, 'msg_type': msg_type}
    service_level = ServiceLevel(subscription, msg_type)
    assert service_level.get_service_level(user_data) == expected
