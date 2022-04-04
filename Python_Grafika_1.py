def BriCon(img, b, c, allLayers=False):
    if (allLayers):
        for layer in img.layers:
            pdb.gimp_drawable_brightness_contrast(layer, b, c)
    else:
        pdb.gimp_drawable_brightness_contrast(
            pdb.gimp_image_get_active_drawable(img), b, c)


def BriConAllImages(b, c, allLayers=True):
    for image in gimp.image_list():
        BriCon(image, b, c, allLayers)


def Gamma(img, gam, allLayers=False):
    if (allLayers):
        for layer in img.layers:
            pdb.gimp_drawable_levels(layer, 0, 0, 1, False, gam, 0, 1, False)
    else:
        pdb.gimp_drawable_levels(pdb.gimp_image_get_active_drawable(
            img), 0, 0, 1, False, gam, 0, 1, False)


def GammaAllImages(gam, allLayers=True):
    for image in gimp.image_list():
        Gamma(image, gam, allLayers)


def FlipH(img, allLayers=False):
    if (allLayers):
        for layer in img.layers:
            pdb.gimp_item_transform_flip_simple(layer, 0, True, 0.0)
    else:
        drw = pdb.gimp_image_get_active_drawable(img)
        pdb.gimp_item_transform_flip_simple(drw, 0, True, 0.0)


def FlipHAllImages(allLayers=True):
    for image in gimp.image_list():
        FlipH(image, allLayers)


def FlipV(img, allLayers=False):
    if (allLayers):
        for layer in img.layers:
            pdb.gimp_item_transform_flip_simple(layer, 1, True, 0.0)
    else:
        drw = pdb.gimp_image_get_active_drawable(img)
        pdb.gimp_item_transform_flip_simple(drw, 1, True, 0.0)


def FlipVAllImages(allLayers=True):
    for image in gimp.image_list():
        FlipV(image, allLayers)
