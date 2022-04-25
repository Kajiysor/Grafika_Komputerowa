# from utils import *

import colorsys
import math


def ColorWheelGIF():
    pdb.gimp_image_undo_disable

    img = NewImage(300, 300)
    drw = pdb.gimp_image_get_active_drawable(img)
    x0 = 150
    y0 = 150
    r0 = 148

    for y in range(-r0, r0):
        for x in range(-r0, r0):
            radius = math.sqrt(x ** 2 + y ** 2)
            if radius > r0:
                continue
            else:
                rgb_color = colorsys.hsv_to_rgb(
                    (math.atan2(y, x) + math.pi) / (2 * math.pi), 1, 1.0)
                color = [val * 255 for val in list(rgb_color)]
                color.append(255)
                pdb.gimp_drawable_set_pixel(drw, x0 + x, y0 + y, 4, color)
    pdb.gimp_item_transform_flip_simple(drw, 0, FALSE, 150)

    for i in range(2):
        pdb.gimp_image_insert_layer(
            img, pdb.gimp_layer_copy(img.layers[0], FALSE), None, 0)
        pdb.gimp_item_transform_rotate(
            img.layers[0], 120*(math.pi/180), TRUE, 0, 0)
    pdb.gimp_image_undo_enable

    SaveGIF(img, "ColorWheelGIF.gif", delay=20)
