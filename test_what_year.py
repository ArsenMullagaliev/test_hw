import urllib.request
from unittest.mock import patch, Mock
from what_is_year_now import what_is_year_now
import json
import pytest


def test_patch_YYYYMMDD():
    expected_year = 2009
    response_val = {'currentDateTime': '2009-07-21'}
    api_patch = Mock(return_value=response_val)
    api_patch.__enter__ = Mock(return_value=None)
    api_patch.__exit__ = Mock(return_value=False)
    with patch.object(urllib.request, 'urlopen', return_value=api_patch):
        with patch.object(json, 'load', return_value=response_val):
            year = what_is_year_now()
    assert expected_year == year


def test_patch_DDMMYYYY():
    expected_year = 2009
    response_val = {'currentDateTime': '21.07.2009'}
    api_patch = Mock(return_value=response_val)
    api_patch.__enter__ = Mock(return_value=None)
    api_patch.__exit__ = Mock(return_value=False)
    with patch.object(urllib.request, 'urlopen', return_value=api_patch):
        with patch.object(json, 'load', return_value=response_val):
            year = what_is_year_now()
    assert expected_year == year


def test_patch_invalid_input():
    response_val = {'currentDateTime': '1111111111111111111111111111111111'}
    api_patch = Mock(return_value=response_val)
    api_patch.__enter__ = Mock(return_value=None)
    api_patch.__exit__ = Mock(return_value=False)
    with pytest.raises(ValueError):
        with patch.object(urllib.request, 'urlopen', return_value=api_patch):
            with patch.object(json, 'load', return_value=response_val):
                what_is_year_now()


def test_today():
    expected = 2021
    actual = what_is_year_now()
    assert expected == actual
