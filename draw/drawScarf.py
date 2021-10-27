from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS

def drawScarf(im, primaryColor, primaryColorShade):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    imNew.putpixel((2, 17), colorsDict["black"])
    imNew.putpixel((3, 17), colorsDict["black"])
    imNew.putpixel((5, 17), colorsDict["black"])
    imNew.putpixel((6, 17), colorsDict["black"])

    imNew.putpixel((1, 18), colorsDict["black"])
    imNew.putpixel((2, 18), colorsDict[primaryColorShade])
    imNew.putpixel((3, 18), colorsDict[primaryColor])
    imNew.putpixel((4, 18), colorsDict["black"])
    imNew.putpixel((5, 18), colorsDict["black"])
    imNew.putpixel((6, 18), colorsDict[primaryColor])
    imNew.putpixel((7, 18), colorsDict["black"])
    imNew.putpixel((8, 18), colorsDict["black"])

    imNew.putpixel((0, 19), colorsDict["black"])
    imNew.putpixel((1, 19), colorsDict[primaryColorShade])
    imNew.putpixel((2, 19), colorsDict[primaryColor])
    imNew.putpixel((3, 19), colorsDict["black"])
    imNew.putpixel((4, 19), colorsDict[primaryColorShade])
    imNew.putpixel((5, 19), colorsDict[primaryColor])
    imNew.putpixel((6, 19), colorsDict["black"])
    imNew.putpixel((7, 19), colorsDict[primaryColor])
    imNew.putpixel((8, 19), colorsDict[primaryColor])
    imNew.putpixel((9, 19), colorsDict["black"])
    imNew.putpixel((10, 19), colorsDict["black"])
    imNew.putpixel((11, 19), colorsDict["black"])
    imNew.putpixel((12, 19), colorsDict["black"])
    imNew.putpixel((13, 19), colorsDict["black"])
    imNew.putpixel((14, 19), colorsDict["black"])

    imNew.putpixel((0, 20), colorsDict[primaryColorShade])
    imNew.putpixel((1, 20), colorsDict[primaryColor])
    imNew.putpixel((2, 20), colorsDict["black"])
    imNew.putpixel((4, 20), colorsDict["black"])
    imNew.putpixel((5, 20), colorsDict["black"])
    imNew.putpixel((7, 20), colorsDict["black"])
    imNew.putpixel((8, 20), colorsDict[primaryColor])
    imNew.putpixel((9, 20), colorsDict[primaryColorShade])
    imNew.putpixel((10, 20), colorsDict[primaryColorShade])
    imNew.putpixel((11, 20), colorsDict[primaryColor])
    imNew.putpixel((12, 20), colorsDict[primaryColor])
    imNew.putpixel((13, 20), colorsDict[primaryColor])
    imNew.putpixel((14, 20), colorsDict["black"])

    imNew.putpixel((0, 21), colorsDict[primaryColor])
    imNew.putpixel((1, 21), colorsDict["black"])
    imNew.putpixel((8, 21), colorsDict["black"])
    imNew.putpixel((9, 21), colorsDict["black"])
    imNew.putpixel((10, 21), colorsDict["black"])
    imNew.putpixel((11, 21), colorsDict["black"])
    imNew.putpixel((12, 21), colorsDict["black"])
    imNew.putpixel((13, 21), colorsDict["black"])

    imNew.putpixel((0, 22), colorsDict["black"])

    im.paste(imNew, (0,0), mask=imNew)
