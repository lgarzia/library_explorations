import pytest
from tutorials import http_error


@pytest.mark.parametrize('status, expected', [
    (200, 'OK'),
    (400, 'Bad request'),
    (401, 'Not allowed'),
    (403, 'Not allowed'),
    (404, 'Not allowed'),
    (500, 'Something is wrong'),
])
def test_http_error(status, expected):
    assert http_error(status) == expected
