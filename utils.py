import colorsys

normal_layer_type = 28


def NewImage(wid, hig):
    img = pdb.gimp_image_new(wid, hig, 0)
    pdb.gimp_display_new(img)
    layer = pdb.gimp_layer_new(
        img, wid, hig, 1, "New_layer", 100, normal_layer_type)
    pdb.gimp_image_insert_layer(img, layer, None, 0)
    return img


def FillRect(Img, x, y, wid, hig, color):
    fg = pdb.gimp_context_get_foreground()
    pdb.gimp_image_select_rectangle(Img, 2, x, y, wid, hig)
    pdb.gimp_context_set_foreground(color)
    pdb.gimp_drawable_edit_fill(pdb.gimp_image_get_active_drawable(Img), 0)
    pdb.gimp_context_set_foreground(fg)


def FillCirc(Img, x, y, r, color):
    fg = pdb.gimp_context_get_foreground()
    pdb.gimp_image_select_ellipse(Img, 2, x-r, y-r, r*2, r*2)
    pdb.gimp_context_set_foreground(color)
    pdb.gimp_drawable_edit_fill(pdb.gimp_image_get_active_drawable(Img), 0)
    pdb.gimp_context_set_foreground(fg)


def Checkerboard(Img, sat=0.0, hue=0.0):
    fg = pdb.gimp_context_get_foreground()
    bg = pdb.gimp_context_get_background()

    layer = pdb.gimp_image_get_active_layer(Img)
    width = pdb.gimp_drawable_width(layer)
    height = pdb.gimp_drawable_height(layer)
    pdb.gimp_context_set_foreground(colorsys.hsv_to_rgb(hue, sat, 1.0))
    pdb.gimp_drawable_edit_fill(layer, 0)

    pdb.gimp_context_set_foreground('#000000')
    pdb.gimp_context_set_background('#000000')
    tmp_layer = pdb.gimp_layer_new(
        Img, width, height, 1, "tmp_layer", 100, normal_layer_type)
    pdb.gimp_image_insert_layer(Img, tmp_layer, None, -1)
    offset_x, offset_y = layer.offsets
    pdb.gimp_layer_set_offsets(tmp_layer, offset_x, offset_y)
    pdb.plug_in_checkerboard(Img, tmp_layer, 0, 1)

    pdb.gimp_image_merge_down(Img, tmp_layer, 0)
    pdb.gimp_context_set_foreground(fg)
    pdb.gimp_context_set_background(bg)
