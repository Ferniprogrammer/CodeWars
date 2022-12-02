def color(RGB):
    if RGB > 255:
        RGB = 255
    elif RGB < 0:
        RGB = 0
    RGB = hex(RGB)[2:].upper()
    if len(RGB)<2:
        RGB = '0'+RGB
    return RGB    

def rgb(c1, c2, c3):
    return color(c1)+color(c2)+color(c3)
