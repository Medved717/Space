import pytest
from unittest.mock import patch

from ls_13.age_checker import is_adult, get_current_year


@patch('ls_13.age_checker.get_current_year')
def test_is_adult_born_2000(mock_year):
    mock_year.return_value = 2026
    result = is_adult(2000)
    assert result == True
    mock_year.assert_called_once()


@patch('ls_13.age_checker.get_current_year')
def test_is_adult_born_2000(mock_year):
    mock_year.return_value = 2005
    result = is_adult(2000)
    assert result == False
    mock_year.assert_called_once()



