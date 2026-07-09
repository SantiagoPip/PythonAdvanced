from main import weather
import pytest
def test_weather_check():
    w = weather()
    assert w.weather_check(-5) == "It´s freeezing outside!"
    assert w.weather_check(10) == "it's a bit chilly"
    assert w.weather_check(20) == "the weather is pleasant"
def test_rain_check():
    w= weather()
    assert w.weather_check(0.8) == "it's a bit chilly"
    assert w.weather_check(0.5) == "it's a bit chilly"
    assert w.weather_check(0.2) == "it's a bit chilly"
def test_divide():
    w = weather()
    assert w.divide(10,2)==5
    assert w.divide(9,3)==3
    with pytest.raises(ValueError,match="Cannot divide by zero!"):
        w.divide(10,0)