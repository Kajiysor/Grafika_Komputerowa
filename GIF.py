import math


def MCopyRotate(img, N):
    pdb.gimp_image_undo_disable
    if (len(img.layers) == 1):
        radians_rotation = (360/N)*(math.pi/180)
        for n in range(N-1):
            new_layer = pdb.gimp_layer_copy(img.layers[0], FALSE)
            pdb.gimp_image_insert_layer(img, new_layer, None, 0)
            pdb.gimp_item_transform_rotate(
                img.layers[0], radians_rotation, TRUE, 0, 0)
        pdb.plug_in_autocrop(img, pdb.gimp_image_get_active_drawable(img))
    pdb.gimp_image_undo_enable


def SaveGIF(img, file_name, delay=40):
    if (pdb.gimp_drawable_is_indexed(pdb.gimp_image_get_active_drawable(img)) == 0):
        pdb.gimp_image_convert_indexed(img, 2, 0, 255, FALSE, FALSE, file_name)
    pdb.file_gif_save(img, pdb.gimp_image_get_active_drawable(
        img), file_name, file_name, 0, 1, delay, 0)
