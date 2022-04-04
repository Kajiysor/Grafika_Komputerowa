image = gimp.image_list()[0]

BriCon(image, 0.2, 0.4)
BriConAllImages(0.5, 0.3, False)
Gamma(image, 10)
GammaAllImages(2.2, True)
FlipH(image)
FlipHAllImages(False)
FlipV(image, True)
FlipVAllImages(False)
Caption(image)
CaptionAllImages()
