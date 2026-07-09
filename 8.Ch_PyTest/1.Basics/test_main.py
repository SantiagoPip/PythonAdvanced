from main import weather_check
def test_weather_check():
    assert weather_check(-5) == "It´s freeezing outside!"
    assert weather_check(10) == "it's a bit chilly"
    assert weather_check(20) == "the weather is pleasant"
if __name__ == "__main__":
    test_weather_check()
