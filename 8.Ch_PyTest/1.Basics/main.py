def weather_check(temp:float)->str:
    if temp<0:
        return "It´s freeezing outside!"
    elif temp < 15:
        return "it's a bit chilly"
    elif temp < 25:
        return "the weather is pleasant"
    else:
        return "It's hot outside"
print(weather_check(10))