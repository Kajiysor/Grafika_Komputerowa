# from utils import *

def ProgressBar():
    pdb.gimp_image_undo_disable

    normal_layer_type = 28
    img = NewImage(300, 50)
    FillRect(img, 0, 0, 300, 50, "#00ff10")
    for x in range(10):
        new_layer = pdb.gimp_layer_new(
            img, 300, 50, 1, "Progress bar: " + str(x), 100, normal_layer_type)
        pdb.gimp_image_insert_layer(img, new_layer, None, 0)
        pdb.gimp_image_set_active_layer(img, new_layer)
        FillRect(img, 0, 0, (x+1)*30, 50, "#004d05")

    pdb.gimp_image_undo_enable

    SaveGIF(img, "ProgressBar.gif", delay=10)
