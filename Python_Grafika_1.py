def BriCon(img, b, c, allLayers=False):
    if (allLayers):
        layers = img.layers
        for i in range(len(layers)):
            drw = layers[i]
            pdb.gimp_drawable_brightness_contrast(drw, b, c)
    else:
        drw = pdb.gimp_image_get_active_drawable(img)
        pdb.gimp_drawable_brightness_contrast(drw, b, c)


def BriConAllImages(b, c, allLayers=False):
    for i in range(len(gimp.image_list())):
        img = gimp.image_list()[i]
        BriCon(img, b, c, allLayers)

# def BriConOneLayer(img, b, c):
#     drw = pdb.gimp_image_get_active_drawable(img)
#     pdb.gimp_drawable_brightness_contrast(drw, b, c)


# def BriConAllLayers(img, b, c):
#     # layers = pdb.gimp_image_get_layers(img)[1]
#     layers = img.layers
#     for i in range(len(layers)):
#         drw = layers[i]
#         pdb.gimp_drawable_brightness_contrast(drw, b, c)

def Gamma(img, gam, allLayers=False):
    if (allLayers):
        layers = img.layers
        for i in range(len(layers)):
            drw = layers[i]
            pdb.gimp_drawable_levels(drw, 0, 0, 1, False, gam, 0, 1, False)
    else:
        drw = pdb.gimp_image_get_active_drawable(img)
        pdb.gimp_drawable_levels(drw, 0, 0, 1, False, gam, 0, 1, False)


# def GammaOneLayer(img, gam):
#     drw = pdb.gimp_image_get_active_drawable(img)
#     pdb.gimp_drawable_levels(drw, 0, 0, 1, False, gam, 0, 1, False)


# def GammaAllLayers(img, gam):
#     layers = img.layers
#     for i in range(len(layers)):
#         drw = layers[i]
#         pdb.gimp_drawable_levels(drw, 0, 0, 1, False, gam, 0, 1, False)


def FlipHOneLayer(img):
    drw = pdb.gimp_image_get_active_drawable(img)
    pdb.gimp_item_transform_flip_simple(drw, 0, True, 0.0)


def FlipVOneLayer(img):
    drw = pdb.gimp_image_get_active_drawable(img)
    pdb.gimp_item_transform_flip_simple(drw, 1, True, 0.0)
