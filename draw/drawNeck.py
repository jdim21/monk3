from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS
from draw.drawBowtie import drawBowtie
from draw.drawNecklace import drawNecklace
from draw.drawScarf import drawScarf

def drawNeck(im, trait):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    decodedType = TRAIT_ENCODINGS["neck"][trait]
    if decodedType == "BlueCollar":
        imNew.putpixel((7, 19), colorsDict["blueShade"])
        imNew.putpixel((8, 19), colorsDict["blue"])

        imNew.putpixel((9, 20), colorsDict["blue"])
        imNew.putpixel((10, 20), colorsDict["blue"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["blue"])
        imNew.putpixel((13, 20), colorsDict["blue"])
        imNew.putpixel((14, 20), colorsDict["blue"])
    elif decodedType == "GoldenCollar":
        # imNew.putpixel((7, 19), colorsDict["goldDogtagsShade"])
        # imNew.putpixel((8, 19), colorsDict["goldDogtags"])

        # imNew.putpixel((9, 20), colorsDict["goldDogtags"])
        imNew.putpixel((10, 20), colorsDict["goldDogtagsShade"])
        imNew.putpixel((11, 20), colorsDict["goldDogtags"])
        imNew.putpixel((12, 20), colorsDict["goldDogtagsShade"])
        # imNew.putpixel((13, 20), colorsDict["goldDogtags"])
        # imNew.putpixel((14, 20), colorsDict["goldDogtags"])
    elif decodedType == "RastaCollar":
        # imNew.putpixel((7, 19), colorsDict["bronzeDogtagsShade"])
        # imNew.putpixel((8, 19), colorsDict["bronzeDogtagsShade"])

        # imNew.putpixel((9, 20), colorsDict["bronzeDogtagsShade"])
        imNew.putpixel((10, 20), colorsDict["redDogtags"])
        imNew.putpixel((11, 20), colorsDict["yellowDogtags"])
        imNew.putpixel((12, 20), colorsDict["greenDogtags"])
        # imNew.putpixel((13, 20), colorsDict["bronzeDogtagsShade"])
        # imNew.putpixel((14, 20), colorsDict["bronzeDogtagsShade"])
    elif decodedType == "FreedomCollar":
        imNew.putpixel((10, 20), colorsDict["redDogtags"])
        imNew.putpixel((11, 20), colorsDict["white"])
        imNew.putpixel((12, 20), colorsDict["blueDogtags"])
    elif decodedType == "SilverCollar":
        imNew.putpixel((10, 20), colorsDict["silverDogtagsShade"])
        imNew.putpixel((11, 20), colorsDict["silverDogtags"])
        imNew.putpixel((12, 20), colorsDict["silverDogtagsShade"])
    elif decodedType == "LeatherCollar":
        imNew.putpixel((10, 20), colorsDict["bronzeDogtags"])
        imNew.putpixel((11, 20), colorsDict["silverDogtagsShade"])
        imNew.putpixel((12, 20), colorsDict["bronzeDogtags"])

    elif decodedType == "RedCollar":
        imNew.putpixel((7, 19), colorsDict["redCollarShade"])
        imNew.putpixel((8, 19), colorsDict["redCollar"])

        imNew.putpixel((9, 20), colorsDict["redCollar"])
        imNew.putpixel((10, 20), colorsDict["redCollar"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["redCollar"])
        imNew.putpixel((13, 20), colorsDict["redCollar"])
        imNew.putpixel((14, 20), colorsDict["redCollar"])
    elif decodedType == "PinkCollar":
        imNew.putpixel((7, 19), colorsDict["pinkCollarShade"])
        imNew.putpixel((8, 19), colorsDict["pinkCollar"])

        imNew.putpixel((9, 20), colorsDict["pinkCollar"])
        imNew.putpixel((10, 20), colorsDict["pinkCollar"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["pinkCollar"])
        imNew.putpixel((13, 20), colorsDict["pinkCollar"])
        imNew.putpixel((14, 20), colorsDict["pinkCollar"])
    elif decodedType == "GreenCollar":
        imNew.putpixel((7, 19), colorsDict["greenCollarShade"])
        imNew.putpixel((8, 19), colorsDict["greenCollar"])

        imNew.putpixel((9, 20), colorsDict["greenCollar"])
        imNew.putpixel((10, 20), colorsDict["greenCollar"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["greenCollar"])
        imNew.putpixel((13, 20), colorsDict["greenCollar"])
        imNew.putpixel((14, 20), colorsDict["greenCollar"])
    elif decodedType == "PurpleCollar":
        imNew.putpixel((7, 19), colorsDict["purpleCollarShade"])
        imNew.putpixel((8, 19), colorsDict["purpleCollar"])

        imNew.putpixel((9, 20), colorsDict["purpleCollar"])
        imNew.putpixel((10, 20), colorsDict["purpleCollar"])
        imNew.putpixel((11, 20), colorsDict["buckleSilver"])
        imNew.putpixel((12, 20), colorsDict["purpleCollar"])
        imNew.putpixel((13, 20), colorsDict["purpleCollar"])
        imNew.putpixel((14, 20), colorsDict["purpleCollar"])

    elif decodedType == "PurpleBowtie":
        drawBowtie(imNew, "purpleBowtie", "purpleBowtieBlue")
    elif decodedType == "GreenBowtie":
        drawBowtie(imNew, "greenBowtie", "greenBowtieShade")
    elif decodedType == "YellowBowtie":
        drawBowtie(imNew, "yellowBowtie", "yellowBowtieShade")
    elif decodedType == "OrangeBowtie":
        drawBowtie(imNew, "orangeBowtie", "orangeBowtieShade")
    elif decodedType == "EmeraldNecklace":
        gemColor = "necklaceEmerald"
        drawNecklace(imNew, gemColor)
    elif decodedType == "SapphireNecklace":
        gemColor = "necklaceSapphire"
        drawNecklace(imNew, gemColor)
    elif decodedType == "RubyNecklace":
        gemColor = "necklaceRuby"
        drawNecklace(imNew, gemColor)
    elif decodedType == "DiamondNecklace":
        gemColor = "necklaceDiamond"
        drawNecklace(imNew, gemColor)
    elif decodedType == "RedScarf":
        primaryColor = "scarfRed"
        primaryColorShade = "scarfRedShade"
        drawScarf(imNew, primaryColor, primaryColorShade)
    elif decodedType == "GreenScarf":
        primaryColor = "scarfGreen"
        primaryColorShade = "scarfGreenShade"
        drawScarf(imNew, primaryColor, primaryColorShade)
    elif decodedType == "Cape":
        imNew.putpixel((0, 15), colorsDict["black"])
        imNew.putpixel((1, 15), colorsDict["black"])

        imNew.putpixel((0, 16), colorsDict["capeShade"])
        imNew.putpixel((1, 16), colorsDict["capeShade"])
        imNew.putpixel((2, 16), colorsDict["black"])
        imNew.putpixel((3, 16), colorsDict["black"])

        imNew.putpixel((0, 17), colorsDict["cape"])
        imNew.putpixel((1, 17), colorsDict["cape"])
        imNew.putpixel((2, 17), colorsDict["capeShade"])
        imNew.putpixel((3, 17), colorsDict["black"])
        imNew.putpixel((4, 17), colorsDict["black"])

        imNew.putpixel((0, 18), colorsDict["cape"])
        imNew.putpixel((1, 18), colorsDict["cape"])
        imNew.putpixel((2, 18), colorsDict["cape"])
        imNew.putpixel((3, 18), colorsDict["capeShade"])
        imNew.putpixel((4, 18), colorsDict["capeShade"])
        imNew.putpixel((5, 18), colorsDict["black"])

        imNew.putpixel((0, 19), colorsDict["cape"])
        imNew.putpixel((1, 19), colorsDict["cape"])
        imNew.putpixel((2, 19), colorsDict["cape"])
        imNew.putpixel((3, 19), colorsDict["cape"])
        imNew.putpixel((4, 19), colorsDict["cape"])
        imNew.putpixel((5, 19), colorsDict["capeShade"])
        imNew.putpixel((6, 19), colorsDict["black"])
        imNew.putpixel((7, 19), colorsDict["capeShade"])
        imNew.putpixel((8, 19), colorsDict["capeShade"])
        imNew.putpixel((9, 19), colorsDict["cape"])
        imNew.putpixel((10, 19), colorsDict["black"])
        imNew.putpixel((11, 19), colorsDict["black"])
        imNew.putpixel((12, 19), colorsDict["black"])
        imNew.putpixel((13, 19), colorsDict["black"])

        imNew.putpixel((0, 20), colorsDict["cape"])
        imNew.putpixel((1, 20), colorsDict["cape"])
        imNew.putpixel((2, 20), colorsDict["cape"])
        imNew.putpixel((3, 20), colorsDict["black"])
        imNew.putpixel((4, 20), colorsDict["cape"])
        imNew.putpixel((5, 20), colorsDict["cape"])
        imNew.putpixel((6, 20), colorsDict["cape"])
        imNew.putpixel((7, 20), colorsDict["capeShade"])
        imNew.putpixel((8, 20), colorsDict["black"])
        imNew.putpixel((9, 20), colorsDict["black"])
        imNew.putpixel((10, 20), colorsDict["cape"])
        imNew.putpixel((11, 20), colorsDict["cape"])
        imNew.putpixel((12, 20), colorsDict["cape"])
        imNew.putpixel((13, 20), colorsDict["capeShade"])
        imNew.putpixel((14, 20), colorsDict["black"])

        imNew.putpixel((0, 21), colorsDict["capeShade"])
        imNew.putpixel((1, 21), colorsDict["black"])
        imNew.putpixel((2, 21), colorsDict["black"])
        imNew.putpixel((4, 21), colorsDict["black"])
        imNew.putpixel((5, 21), colorsDict["black"])
        imNew.putpixel((6, 21), colorsDict["black"])
        imNew.putpixel((7, 21), colorsDict["black"])
        imNew.putpixel((10, 21), colorsDict["black"])
        imNew.putpixel((11, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((13, 21), colorsDict["black"])

        imNew.putpixel((0, 22), colorsDict["black"])

    im.paste(imNew, (0,0), mask=imNew)
