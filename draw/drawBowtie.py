from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS

def drawBowtie(im, primaryColor, secondaryColor):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    imNew.putpixel((8, 17), colorsDict["black"])
    imNew.putpixel((15, 17), colorsDict["black"])

    imNew.putpixel((7, 18), colorsDict["black"])
    imNew.putpixel((8, 18), colorsDict[primaryColor])
    imNew.putpixel((9, 18), colorsDict["black"])
    imNew.putpixel((10, 18), colorsDict["black"])
    imNew.putpixel((13, 18), colorsDict["black"])
    imNew.putpixel((14, 18), colorsDict["black"])
    imNew.putpixel((15, 18), colorsDict[primaryColor])
    imNew.putpixel((16, 18), colorsDict["black"])

    imNew.putpixel((7, 19), colorsDict["black"])
    imNew.putpixel((8, 19), colorsDict[secondaryColor])
    imNew.putpixel((9, 19), colorsDict[primaryColor])
    imNew.putpixel((10, 19), colorsDict[primaryColor])
    imNew.putpixel((11, 19), colorsDict["black"])
    imNew.putpixel((12, 19), colorsDict["black"])
    imNew.putpixel((13, 19), colorsDict[primaryColor])
    imNew.putpixel((14, 19), colorsDict[primaryColor])
    imNew.putpixel((15, 19), colorsDict[secondaryColor])
    imNew.putpixel((16, 19), colorsDict["black"])

    imNew.putpixel((7, 20), colorsDict["black"])
    imNew.putpixel((8, 20), colorsDict[primaryColor])
    imNew.putpixel((9, 20), colorsDict[secondaryColor])
    imNew.putpixel((10, 20), colorsDict["black"])
    imNew.putpixel((11, 20), colorsDict[secondaryColor])
    imNew.putpixel((12, 20), colorsDict[primaryColor])
    imNew.putpixel((13, 20), colorsDict["black"])
    imNew.putpixel((14, 20), colorsDict[secondaryColor])
    imNew.putpixel((15, 20), colorsDict[primaryColor])
    imNew.putpixel((16, 20), colorsDict["black"])

    imNew.putpixel((7, 21), colorsDict["black"])
    imNew.putpixel((8, 21), colorsDict[primaryColor])
    imNew.putpixel((9, 21), colorsDict["black"])
    imNew.putpixel((11, 21), colorsDict["black"])
    imNew.putpixel((12, 21), colorsDict["black"])
    imNew.putpixel((14, 21), colorsDict["black"])
    imNew.putpixel((15, 21), colorsDict[primaryColor])
    imNew.putpixel((16, 21), colorsDict["black"])

    imNew.putpixel((8, 22), colorsDict["black"])
    imNew.putpixel((15, 22), colorsDict["black"])

    im.paste(imNew, (0,0), mask=imNew)
