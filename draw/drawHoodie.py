from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS

def drawHoodie(im, color):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    primaryColor = "pink"
    shadeColor = "pinkShade"
    if color == "pink":
        primaryColor = "pink"
        shadeColor = "pinkShade"
    elif color == "blueHoodie":
        primaryColor = "blueHoodie"
        shadeColor = "blueHoodieShade"
    elif color == "grayHoodie":
        primaryColor = "grayHoodie"
        shadeColor = "grayHoodieShade"
    elif color == "orangeHoodie":
        primaryColor = "orangeHoodie"
        shadeColor = "orangeHoodieShade"
    elif color == "purpleHoodie":
        primaryColor = "purpleHoodie"
        shadeColor = "purpleHoodieShade"
    elif color == "lime":
        primaryColor = "lime"
        shadeColor = "limeShade"
    elif color == "white":
        primaryColor = "white"
        shadeColor = "whiteShade"
    elif color == "purple":
        primaryColor = "purple"
        shadeColor = "purpleShade"
    elif color == "yellowHoodie":
        primaryColor = "yellowCollared"
        shadeColor = "yellowCollaredShade"
    elif color == "goku":
        primaryColor = "orange"
        shadeColor = "orangeShade"
    elif color == "dark":
        primaryColor = "darkShirt"
        shadeColor = "darkShirtShade"
    elif color == "stripes":
        primaryColor = "stripes1"
        shadeColor = "stripes1Shade"
    elif color == "vice":
        primaryColor = "vice"
        shadeColor = "viceShade"
    imNew.putpixel((5, 17), colorsDict["black"])

    imNew.putpixel((4, 18), colorsDict["black"])
    imNew.putpixel((5, 18), colorsDict[primaryColor])
    imNew.putpixel((6, 18), colorsDict[primaryColor])

    imNew.putpixel((4, 19), colorsDict["black"])
    imNew.putpixel((5, 19), colorsDict[primaryColor])
    imNew.putpixel((6, 19), colorsDict["black"])
    imNew.putpixel((7, 19), colorsDict[shadeColor])
    imNew.putpixel((8, 19), colorsDict["hoodieStrings"])
    imNew.putpixel((15, 19), colorsDict["hoodieStrings"])
    imNew.putpixel((16, 19), colorsDict[primaryColor])
    imNew.putpixel((17, 19), colorsDict["black"])

    imNew.putpixel((5, 20), colorsDict["black"])
    imNew.putpixel((6, 20), colorsDict[shadeColor])
    imNew.putpixel((7, 20), colorsDict[primaryColor])
    imNew.putpixel((8, 20), colorsDict[primaryColor])
    imNew.putpixel((9, 20), colorsDict["black"])
    imNew.putpixel((13, 20), colorsDict["black"])
    imNew.putpixel((14, 20), colorsDict[primaryColor])
    imNew.putpixel((15, 20), colorsDict["black"])
    imNew.putpixel((16, 20), colorsDict[primaryColor])
    imNew.putpixel((17, 20), colorsDict["black"])

    imNew.putpixel((4, 21), colorsDict["black"])
    imNew.putpixel((5, 21), colorsDict[shadeColor])
    imNew.putpixel((6, 21), colorsDict[primaryColor])
    imNew.putpixel((7, 21), colorsDict[primaryColor])
    imNew.putpixel((8, 21), colorsDict[primaryColor])
    imNew.putpixel((9, 21), colorsDict[primaryColor])
    imNew.putpixel((10, 21), colorsDict["black"])
    imNew.putpixel((11, 21), colorsDict["black"])
    imNew.putpixel((12, 21), colorsDict["black"])
    imNew.putpixel((13, 21), colorsDict[primaryColor])
    imNew.putpixel((14, 21), colorsDict[primaryColor])
    imNew.putpixel((15, 21), colorsDict["black"])
    imNew.putpixel((16, 21), colorsDict["black"])

    imNew.putpixel((3, 22), colorsDict["black"])
    imNew.putpixel((4, 22), colorsDict[shadeColor])
    imNew.putpixel((5, 22), colorsDict[primaryColor])
    imNew.putpixel((6, 22), colorsDict[primaryColor])
    imNew.putpixel((7, 22), colorsDict[primaryColor])
    imNew.putpixel((8, 22), colorsDict[primaryColor])
    imNew.putpixel((9, 22), colorsDict[primaryColor])
    imNew.putpixel((10, 22), colorsDict[primaryColor])
    imNew.putpixel((11, 22), colorsDict[primaryColor])
    imNew.putpixel((12, 22), colorsDict[primaryColor])
    imNew.putpixel((13, 22), colorsDict[primaryColor])
    imNew.putpixel((14, 22), colorsDict[primaryColor])
    imNew.putpixel((15, 22), colorsDict["black"])

    imNew.putpixel((2, 23), colorsDict["black"])
    imNew.putpixel((3, 23), colorsDict[shadeColor])
    imNew.putpixel((4, 23), colorsDict[primaryColor])
    imNew.putpixel((5, 23), colorsDict[primaryColor])
    imNew.putpixel((6, 23), colorsDict[primaryColor])
    imNew.putpixel((7, 23), colorsDict[primaryColor])
    imNew.putpixel((8, 23), colorsDict[primaryColor])
    imNew.putpixel((9, 23), colorsDict["black"])
    imNew.putpixel((10, 23), colorsDict[shadeColor])
    imNew.putpixel((11, 23), colorsDict[shadeColor])
    imNew.putpixel((12, 23), colorsDict["black"])
    imNew.putpixel((13, 23), colorsDict[shadeColor])
    imNew.putpixel((14, 23), colorsDict[shadeColor])
    imNew.putpixel((15, 23), colorsDict["black"])

    im.paste(imNew, (0,0), mask=imNew)
