import colorgram
from colorgram import Color


def to_rb_colors(color: Color)-> (int, int, int):
    return color.rgb.r, color.rgb.g, color.rgb.b

colors = list(map(to_rb_colors, colorgram.extract('image.jpeg', 100)))
print(colors)