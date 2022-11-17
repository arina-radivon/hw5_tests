import urllib.request
import json
import pytest
from unittest.mock import patch

API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


"""
I've tried to mock only one object as string but it doesn't work.
Thats why I mocked 2 objects further.

def test_dash():
    # mock_tmp.return_value.__enter__.return_value.name = mytmpname
    with patch('urllib.request.urlopen') as response:
        response.return_value.__enter__.return_value =
                                    {'currentDateTime': '2022-03-01'}
        assert what_is_year_now() == 2022
"""


def test_dash():
    with patch('urllib.request.urlopen'):
        with patch('json.load') as json_load:
            json_load.return_value = {'currentDateTime': '2022-03-01'}
            assert what_is_year_now() == 2022


def test_dots():
    with patch('urllib.request.urlopen'):
        with patch('json.load') as json_load:
            json_load.return_value = {'currentDateTime': '01.03.2019'}
            assert what_is_year_now() == 2019


def test_error():
    with patch('urllib.request.urlopen'):
        with patch('json.load') as json_load:
            json_load.return_value = {'currentDateTime': '2022.03.01'}
            with pytest.raises(ValueError):
                what_is_year_now()


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля
    'currentDateTime' год
    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)
