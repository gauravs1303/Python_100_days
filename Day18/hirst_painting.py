import colorgram

colors = colorgram.extract('color_check.png', 20)

rgb_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)

print(rgb_color)

col_list = [(254, 253, 253), (101, 190, 171), (100, 164, 209), (207, 137, 182), (213, 230, 240), (56, 179, 154), (49, 124, 170), (187, 222, 211), (25, 26, 26), (217, 163, 85), (239, 212, 97), (189, 89, 132), (124, 73, 114), (160, 209, 185), (89, 126, 186), (237, 160, 182), (242, 206, 217), (51, 154, 194), (46, 134, 112), (64, 30, 45)]
