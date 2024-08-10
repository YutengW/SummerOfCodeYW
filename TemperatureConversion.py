import math
temperatureInCelsius = 0
convertedTemperatureInFahrenheit = 0
temperatureInFahrenheit = 0
convertedTemperatureInCelsius = 0
def convertToFahrenheit(temperatureInCelsius):
    return temperatureInCelsius * (9/5) + 32

def convertToCelsius(temperatureInFahrenheit):
    return (temperatureInFahrenheit - 32) * (5/9)

assert convertToCelsius(0) == -17.77777777777778 
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(180) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001

print (convertedTemperatureInFahrenheit)


