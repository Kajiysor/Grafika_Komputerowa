# from utils import *

normal_layer_type = 28


def GammaCal(width=500, height=500):
    img = NewImage(width, height)

    gray_layer = pdb.gimp_layer_new(
        img, width/2, height/2, 1, "Gray", 100, normal_layer_type)
    pdb.gimp_image_insert_layer(img, gray_layer, None, 0)
    pdb.gimp_image_set_active_layer(img, gray_layer)
    Checkerboard(img, 0, 0)
    FillRect(img, width/6, height/6, width/6, height/6, '#7f7f7f')
    pdb.gimp_selection_none(img)

    red_layer = pdb.gimp_layer_new(
        img, width/2, height/2, 1, "Red", 100, normal_layer_type)
    pdb.gimp_image_insert_layer(img, red_layer, None, 0)
    pdb.gimp_image_set_active_layer(img, red_layer)
    Checkerboard(img, 1, 0)
    FillRect(img, width/6, height/6, width/6, height/6, '#7f0000')
    pdb.gimp_selection_none(img)
    pdb.gimp_layer_set_offsets(img.layers[0], width/2, 0)

    green_layer = pdb.gimp_layer_new(
        img, width/2, height/2, 1, "Green", 100, normal_layer_type)
    pdb.gimp_image_insert_layer(img, green_layer, None, 0)
    pdb.gimp_image_set_active_layer(img, green_layer)
    Checkerboard(img, 1, 0.3333)
    FillRect(img, width/6, height/6, width/6, height/6, '#007f00')
    pdb.gimp_selection_none(img)
    pdb.gimp_layer_set_offsets(img.layers[0], 0, height/2)

    blue_layer = pdb.gimp_layer_new(
        img, width/2, height/2, 1, "Blue", 100, normal_layer_type)
    pdb.gimp_image_insert_layer(img, blue_layer, None, 0)
    pdb.gimp_image_set_active_layer(img, blue_layer)
    Checkerboard(img, 1, 0.6667)
    FillRect(img, width/6, height/6, width/6, height/6, '#00007f')
    pdb.gimp_selection_none(img)
    pdb.gimp_layer_set_offsets(img.layers[0], width/2, height/2)
