import pytest
import converter


def test_get_data():
    data = converter.get_data()
    assert data.columns[0] == "name" and data.columns[1] == "one_dollar"


@pytest.mark.parametrize("fahrenheit, celsius", [(99, 37.22222222222222), (50, 10.0)])
def test_to_celsius(fahrenheit, celsius):
    assert converter.to_celsius(fahrenheit) == celsius


@pytest.mark.parametrize("fahrenheit, celsius", [(99, 37.22222222222222), (50, 10.0)])
def test_to_fahrenheit(fahrenheit, celsius):
    assert converter.to_fahrenheit(celsius) == fahrenheit
