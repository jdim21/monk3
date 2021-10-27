from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS

def drawNecklace(im, gem):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    imNew.putpixel((8, 19), colorsDict["necklaceShade"])

    imNew.putpixel((9, 20), colorsDict["necklaceShade"])
    imNew.putpixel((10, 20), colorsDict["necklace"])
    imNew.putpixel((11, 20), colorsDict[gem])
    imNew.putpixel((12, 20), colorsDict["necklace"])
    imNew.putpixel((13, 20), colorsDict["necklace"])
    imNew.putpixel((14, 20), colorsDict["necklaceShade"])

    imNew.putpixel((11, 21), colorsDict["necklace"])


    im.paste(imNew, (0,0), mask=imNew)
