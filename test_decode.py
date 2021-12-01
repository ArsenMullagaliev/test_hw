import pytest
from morse import decode


@pytest.mark.parametrize('message,decoded', [
    ('.-', 'A'),
    ('... --- ...', 'SOS'),
    ('.- .- .-', 'AAA')
])
def test_decode(message, decoded):
    assert decode(message) == decoded
