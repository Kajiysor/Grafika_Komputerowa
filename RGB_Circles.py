# from utils import *


def RGBCircles(width=100, height=100):
    img = NewImage(width, height)
    FillRect(img, 0, 0, width, height, '#000000')

    NewCircle(img, width, height, "Red")
    NewCircle(img, width, height, "Green")
    NewCircle(img, width, height, "Blue")


def NewCircle(img, width, height, name):
    layer_mode_addition = 33
    pdb.gimp_image_insert_layer(img, pdb.gimp_layer_new(
        img, width, height, 1, name, 100, layer_mode_addition), None, 0)

    if name.lower() == "red":
        FillCirc(img, width/2, height/3, width/4, '#ff0000')
    elif name.lower() == "green":
        FillCirc(img, width/3, height*2/3, width/4, '#00ff00')
    elif name.lower() == "blue":
        FillCirc(img, width*2/3, height*2/3, width/4, '#0000ff')
    else:
        print("Wrong color")
