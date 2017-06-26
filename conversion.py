def convert(celsius):
    fahrenheit = []
    for val in celsius:
        f  = (val*9/5) + 32
        fahrenheit.append(f)
    return fahrenheit
