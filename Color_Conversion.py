# Defining a function that takes 3 arguments the value of each color.
def rgb_to_hex(r,g,b):
# Returning values in hex format, using format to make values into hexadecimal numbers.
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)
# Defining a function for converting hex to RGB
def hex_to_rgb(hex):
# Creating a empty list for my for loop.
    rgb = []
# For loop for taking two colors at a time from the hexcode.
    for color in (0, 2, 4):
# Converting values to their decimal form with 16 as a base.
        decimal = int(hex[color:color+2], 16)
# Appending my empty list.
        rgb.append(decimal)
# Returning the rgb value as tuple.
    return tuple(rgb)
