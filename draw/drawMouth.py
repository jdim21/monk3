from PIL import Image
from colors import colorsDict
from traitEncodings import TRAIT_ENCODINGS

typesWithoutHighEyes = ["s", "z", "a"]

def drawMouth(im, trait, typeEncoding):
    imNew = Image.new('RGBA', (24, 24), (0, 0, 0, 0))

    decodedType = TRAIT_ENCODINGS["mouth"][trait]
    if decodedType == "Bubblegum":

        imNew.putpixel((13, 14), colorsDict["bubblegumOutline"])
        imNew.putpixel((14, 14), colorsDict["bubblegumOutline"])
        imNew.putpixel((15, 14), colorsDict["bubblegumOutline"])

        imNew.putpixel((12, 15), colorsDict["bubblegumOutline"])
        imNew.putpixel((13, 15), colorsDict["bubblegum"])
        imNew.putpixel((14, 15), colorsDict["bubblegum"])
        imNew.putpixel((15, 15), colorsDict["bubblegum"])
        imNew.putpixel((16, 15), colorsDict["bubblegumOutline"])

        imNew.putpixel((11, 16), colorsDict["bubblegumOutline"])
        imNew.putpixel((12, 16), colorsDict["bubblegum"])
        imNew.putpixel((13, 16), colorsDict["white"])
        imNew.putpixel((14, 16), colorsDict["bubblegum"])
        imNew.putpixel((15, 16), colorsDict["bubblegum"])
        imNew.putpixel((16, 16), colorsDict["bubblegum"])
        imNew.putpixel((17, 16), colorsDict["bubblegumOutline"])

        imNew.putpixel((11, 17), colorsDict["bubblegumOutline"])
        imNew.putpixel((12, 17), colorsDict["white"])
        imNew.putpixel((13, 17), colorsDict["bubblegum"])
        imNew.putpixel((14, 17), colorsDict["bubblegum"])
        imNew.putpixel((15, 17), colorsDict["bubblegum"])
        imNew.putpixel((16, 17), colorsDict["bubblegum"])
        imNew.putpixel((17, 17), colorsDict["bubblegumOutline"])

        imNew.putpixel((11, 18), colorsDict["bubblegumOutline"])
        imNew.putpixel((12, 18), colorsDict["bubblegum"])
        imNew.putpixel((13, 18), colorsDict["bubblegum"])
        imNew.putpixel((14, 18), colorsDict["bubblegum"])
        imNew.putpixel((15, 18), colorsDict["white"])
        imNew.putpixel((16, 18), colorsDict["bubblegum"])
        imNew.putpixel((17, 18), colorsDict["bubblegumOutline"])

        imNew.putpixel((12, 19), colorsDict["bubblegumOutline"])
        imNew.putpixel((13, 19), colorsDict["bubblegum"])
        imNew.putpixel((14, 19), colorsDict["bubblegum"])
        imNew.putpixel((15, 19), colorsDict["bubblegum"])
        imNew.putpixel((16, 19), colorsDict["bubblegumOutline"])

        imNew.putpixel((13, 20), colorsDict["bubblegumOutline"])
        imNew.putpixel((14, 20), colorsDict["bubblegumOutline"])
        imNew.putpixel((15, 20), colorsDict["bubblegumOutline"])

    elif decodedType == "Booger":
        imNew.putpixel((12, 15), colorsDict["booger"])
    elif decodedType == "Drool":
        imNew.putpixel((10, 17), colorsDict["drool"])
        imNew.putpixel((10, 19), colorsDict["drool"])
    elif decodedType == "ClownNose":
        imNew.putpixel((11, 14), colorsDict["clownNose"])
        imNew.putpixel((11, 15), colorsDict["clownNose"])
        imNew.putpixel((12, 14), colorsDict["clownNose"])
        imNew.putpixel((12, 15), colorsDict["clownNose"])
    elif decodedType == "Bacon":
        imNew.putpixel((11, 16), colorsDict["baconOuter"])
        imNew.putpixel((12, 16), colorsDict["baconOuter"])
        imNew.putpixel((15, 16), colorsDict["baconOuter"])
        imNew.putpixel((16, 16), colorsDict["baconOuter"])
        imNew.putpixel((17, 16), colorsDict["baconOuter"])
        imNew.putpixel((20, 16), colorsDict["baconOuter"])

        imNew.putpixel((11, 17), colorsDict["baconInner"])
        imNew.putpixel((12, 17), colorsDict["baconInner"])
        imNew.putpixel((13, 17), colorsDict["baconOuter"])
        imNew.putpixel((14, 17), colorsDict["baconOuter"])
        imNew.putpixel((15, 17), colorsDict["baconInner"])
        imNew.putpixel((16, 17), colorsDict["baconInner"])
        imNew.putpixel((17, 17), colorsDict["baconInner"])
        imNew.putpixel((18, 17), colorsDict["baconOuter"])
        imNew.putpixel((19, 17), colorsDict["baconOuter"])
        imNew.putpixel((20, 17), colorsDict["baconInner"])

        imNew.putpixel((11, 18), colorsDict["baconOuter"])
        imNew.putpixel((12, 18), colorsDict["baconOuter"])
        imNew.putpixel((13, 18), colorsDict["baconInner"])
        imNew.putpixel((14, 18), colorsDict["baconInner"])
        imNew.putpixel((15, 18), colorsDict["baconOuter"])
        imNew.putpixel((16, 18), colorsDict["baconOuter"])
        imNew.putpixel((17, 18), colorsDict["baconOuter"])
        imNew.putpixel((18, 18), colorsDict["baconInner"])
        imNew.putpixel((19, 18), colorsDict["baconInner"])
        imNew.putpixel((20, 18), colorsDict["baconOuter"])

        imNew.putpixel((13, 19), colorsDict["baconOuter"])
        imNew.putpixel((14, 19), colorsDict["baconOuter"])
        imNew.putpixel((18, 19), colorsDict["baconOuter"])
        imNew.putpixel((19, 19), colorsDict["baconOuter"])
    elif decodedType == "Cigarette":
        imNew.putpixel((22, 11), colorsDict["cigarette"])
        imNew.putpixel((21, 12), colorsDict["cigarette"])
        imNew.putpixel((22, 13), colorsDict["cigarette"])
        imNew.putpixel((21, 14), colorsDict["cigarette"])

        imNew.putpixel((11, 16), colorsDict["cigaretteYellow"])
        imNew.putpixel((12, 16), colorsDict["cigaretteYellow"])
        imNew.putpixel((13, 16), colorsDict["cigaretteYellow"])
        imNew.putpixel((14, 16), colorsDict["cigarette"])
        imNew.putpixel((15, 16), colorsDict["cigarette"])
        imNew.putpixel((16, 16), colorsDict["cigarette"])
        imNew.putpixel((17, 16), colorsDict["cigarette"])
        imNew.putpixel((18, 16), colorsDict["cigarette"])
        imNew.putpixel((19, 16), colorsDict["cigarette"])
        imNew.putpixel((20, 16), colorsDict["cigaretteOrange"])
    elif decodedType == "Twig":
        imNew.putpixel((21, 14), colorsDict["twigLeaf1"])

        imNew.putpixel((14, 15), colorsDict["twig"])
        imNew.putpixel((15, 15), colorsDict["twig"])
        imNew.putpixel((19, 15), colorsDict["twig"])
        imNew.putpixel((20, 15), colorsDict["twig"])

        imNew.putpixel((11, 16), colorsDict["twig"])
        imNew.putpixel((12, 16), colorsDict["twig"])
        imNew.putpixel((13, 16), colorsDict["twig"])
        imNew.putpixel((16, 16), colorsDict["twig"])
        imNew.putpixel((17, 16), colorsDict["twig"])
        imNew.putpixel((18, 16), colorsDict["twig"])
        imNew.putpixel((21, 16), colorsDict["twig"])

        imNew.putpixel((17, 17), colorsDict["twigLeaf1"])
        imNew.putpixel((20, 17), colorsDict["twigLeaf2"])
        imNew.putpixel((22, 17), colorsDict["twigLeaf1"])

    elif decodedType == "Cookie":
        imNew.putpixel((13, 14), colorsDict["cookieOutline"])
        imNew.putpixel((14, 14), colorsDict["cookieOutline"])
        imNew.putpixel((15, 14), colorsDict["cookieOutline"])


        imNew.putpixel((16, 17), colorsDict["twigLeaf1"])
    elif decodedType == "Cookie":
        imNew.putpixel((13, 14), colorsDict["cookieOutline"])
        imNew.putpixel((14, 14), colorsDict["cookieOutline"])
        imNew.putpixel((15, 14), colorsDict["cookieOutline"])

        imNew.putpixel((12, 15), colorsDict["cookieOutline"])
        imNew.putpixel((13, 15), colorsDict["cookie"])
        imNew.putpixel((14, 15), colorsDict["cookieChip"])
        imNew.putpixel((15, 15), colorsDict["cookie"])
        imNew.putpixel((16, 15), colorsDict["cookieOutline"])

        imNew.putpixel((11, 16), colorsDict["cookieOutline"])
        imNew.putpixel((12, 16), colorsDict["cookie"])
        imNew.putpixel((13, 16), colorsDict["cookie"])
        imNew.putpixel((14, 16), colorsDict["cookie"])
        imNew.putpixel((15, 16), colorsDict["cookie"])
        imNew.putpixel((16, 16), colorsDict["cookie"])
        imNew.putpixel((17, 16), colorsDict["cookieOutline"])

        imNew.putpixel((11, 17), colorsDict["cookieOutline"])
        imNew.putpixel((12, 17), colorsDict["cookieChip"])
        imNew.putpixel((13, 17), colorsDict["cookie"])
        imNew.putpixel((14, 17), colorsDict["cookieChip"])
        imNew.putpixel((15, 17), colorsDict["cookie"])
        imNew.putpixel((16, 17), colorsDict["cookie"])
        imNew.putpixel((17, 17), colorsDict["cookieOutline"])

        imNew.putpixel((11, 18), colorsDict["cookieOutline"])
        imNew.putpixel((12, 18), colorsDict["cookie"])
        imNew.putpixel((13, 18), colorsDict["cookie"])
        imNew.putpixel((14, 18), colorsDict["cookie"])
        imNew.putpixel((15, 18), colorsDict["cookie"])
        imNew.putpixel((16, 18), colorsDict["cookieChip"])
        imNew.putpixel((17, 18), colorsDict["cookieOutline"])

        imNew.putpixel((12, 19), colorsDict["cookieOutline"])
        imNew.putpixel((13, 19), colorsDict["cookieChip"])
        imNew.putpixel((14, 19), colorsDict["cookie"])
        imNew.putpixel((15, 19), colorsDict["cookie"])
        imNew.putpixel((16, 19), colorsDict["cookieOutline"])

        imNew.putpixel((13, 20), colorsDict["cookieOutline"])
        imNew.putpixel((14, 20), colorsDict["cookieOutline"])
        imNew.putpixel((15, 20), colorsDict["cookieOutline"])
    elif decodedType == "Ball":
        imNew.putpixel((13, 14), colorsDict["ballOutline"])
        imNew.putpixel((14, 14), colorsDict["ballOutline"])
        imNew.putpixel((15, 14), colorsDict["ballOutline"])

        imNew.putpixel((12, 15), colorsDict["ballOutline"])
        imNew.putpixel((13, 15), colorsDict["ball"])
        imNew.putpixel((14, 15), colorsDict["ball"])
        imNew.putpixel((15, 15), colorsDict["ballShine"])
        imNew.putpixel((16, 15), colorsDict["ballOutline"])

        imNew.putpixel((11, 16), colorsDict["ballOutline"])
        imNew.putpixel((12, 16), colorsDict["ball"])
        imNew.putpixel((13, 16), colorsDict["ball"])
        imNew.putpixel((14, 16), colorsDict["ball"])
        imNew.putpixel((15, 16), colorsDict["ball"])
        imNew.putpixel((16, 16), colorsDict["ballShine"])
        imNew.putpixel((17, 16), colorsDict["ballOutline"])

        imNew.putpixel((11, 17), colorsDict["ballOutline"])
        imNew.putpixel((12, 17), colorsDict["ball"])
        imNew.putpixel((13, 17), colorsDict["ball"])
        imNew.putpixel((14, 17), colorsDict["ballNotch"])
        imNew.putpixel((15, 17), colorsDict["ball"])
        imNew.putpixel((16, 17), colorsDict["ball"])
        imNew.putpixel((17, 17), colorsDict["ballOutline"])

        imNew.putpixel((11, 18), colorsDict["ballOutline"])
        imNew.putpixel((12, 18), colorsDict["white"])
        imNew.putpixel((13, 18), colorsDict["white"])
        imNew.putpixel((14, 18), colorsDict["white"])
        imNew.putpixel((15, 18), colorsDict["white"])
        imNew.putpixel((16, 18), colorsDict["white"])
        imNew.putpixel((17, 18), colorsDict["ballOutline"])

        imNew.putpixel((12, 19), colorsDict["ballOutline"])
        imNew.putpixel((13, 19), colorsDict["white"])
        imNew.putpixel((14, 19), colorsDict["white"])
        imNew.putpixel((15, 19), colorsDict["white"])
        imNew.putpixel((16, 19), colorsDict["ballOutline"])

        imNew.putpixel((13, 20), colorsDict["ballOutline"])
        imNew.putpixel((14, 20), colorsDict["ballOutline"])
        imNew.putpixel((15, 20), colorsDict["ballOutline"])

    elif decodedType == "BeerBottle":
        imNew.putpixel((16, 14), colorsDict["beerBottle"])
        imNew.putpixel((17, 14), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((18, 14), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((19, 14), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((20, 14), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((21, 14), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((22, 14), colorsDict["beerBottle"])

        imNew.putpixel((13, 15), colorsDict["beerBottleTop"])
        imNew.putpixel((14, 15), colorsDict["beerBottleTop"])
        imNew.putpixel((15, 15), colorsDict["beerBottle"])
        imNew.putpixel((16, 15), colorsDict["beerBottle"])
        imNew.putpixel((17, 15), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((18, 15), colorsDict["beerBottleLabelRed"])
        imNew.putpixel((19, 15), colorsDict["beerBottleLabelGray"])
        imNew.putpixel((20, 15), colorsDict["beerBottleLabelRed"])
        imNew.putpixel((21, 15), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((22, 15), colorsDict["beerBottle"])

        imNew.putpixel((12, 16), colorsDict["beer"])
        imNew.putpixel((13, 16), colorsDict["beerBottleTop"])
        imNew.putpixel((14, 16), colorsDict["beerBottleTop"])
        imNew.putpixel((15, 16), colorsDict["beerBottleShade"])
        imNew.putpixel((16, 16), colorsDict["beerBottleShade"])
        imNew.putpixel((17, 16), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((18, 16), colorsDict["beerBottleLabelRed"])
        imNew.putpixel((19, 16), colorsDict["beerBottleLabelGray"])
        imNew.putpixel((20, 16), colorsDict["beerBottleLabelRed"])
        imNew.putpixel((21, 16), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((22, 16), colorsDict["beerBottleShade"])

        imNew.putpixel((16, 17), colorsDict["beerBottleShade"])
        imNew.putpixel((17, 17), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((18, 17), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((19, 17), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((20, 17), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((21, 17), colorsDict["beerBottleLabelGreen"])
        imNew.putpixel((22, 17), colorsDict["beerBottleShade"])
    elif decodedType == "Rose":
        imNew.putpixel((17, 14), colorsDict["roseOutline"])
        imNew.putpixel((18, 14), colorsDict["roseOutline"])
        imNew.putpixel((19, 14), colorsDict["roseOutline"])

        imNew.putpixel((16, 15), colorsDict["roseOutline"])
        imNew.putpixel((17, 15), colorsDict["roseOutline"])
        imNew.putpixel((18, 15), colorsDict["rose"])
        imNew.putpixel((19, 15), colorsDict["roseLight"])

        imNew.putpixel((8, 16), colorsDict["roseStem"])
        imNew.putpixel((9, 16), colorsDict["roseStem"])
        imNew.putpixel((10, 16), colorsDict["roseStem"])
        imNew.putpixel((11, 16), colorsDict["roseStem"])
        imNew.putpixel((12, 16), colorsDict["roseStem"])
        imNew.putpixel((13, 16), colorsDict["roseStem"])
        imNew.putpixel((14, 16), colorsDict["roseStem"])
        imNew.putpixel((15, 16), colorsDict["roseStem"])
        imNew.putpixel((16, 16), colorsDict["roseOutline"])
        imNew.putpixel((17, 16), colorsDict["rose"])
        imNew.putpixel((18, 16), colorsDict["roseLight"])
        imNew.putpixel((19, 16), colorsDict["rose"])

        imNew.putpixel((16, 17), colorsDict["roseOutline"])
        imNew.putpixel((17, 17), colorsDict["roseOutline"])
        imNew.putpixel((18, 17), colorsDict["rose"])
        imNew.putpixel((19, 17), colorsDict["roseLight"])

        imNew.putpixel((17, 18), colorsDict["roseOutline"])
        imNew.putpixel((18, 18), colorsDict["roseOutline"])
        imNew.putpixel((19, 18), colorsDict["roseOutline"])
    elif decodedType == "Blushing":
        imNew.putpixel((7, 15), colorsDict["blushing"])
        imNew.putpixel((16, 15), colorsDict["blushing"])
    elif decodedType == "Surprised":
        imNew.putpixel((9, 15), colorsDict["white"])
        imNew.putpixel((14, 15), colorsDict["white"])
    elif decodedType == "Kazoo":
        imNew.putpixel((16, 15), colorsDict["kazooWhistle"])
        imNew.putpixel((17, 15), colorsDict["kazooWhistle"])

        imNew.putpixel((11, 16), colorsDict["kazooTop"])
        imNew.putpixel((12, 16), colorsDict["kazooTop"])
        imNew.putpixel((13, 16), colorsDict["kazooTop"])
        imNew.putpixel((14, 16), colorsDict["kazooTop"])
        imNew.putpixel((15, 16), colorsDict["kazooTop"])
        imNew.putpixel((16, 16), colorsDict["kazooTop"])
        imNew.putpixel((17, 16), colorsDict["kazooTop"])

        imNew.putpixel((13, 17), colorsDict["kazooBottom"])
        imNew.putpixel((14, 17), colorsDict["kazooBottom"])
        imNew.putpixel((15, 17), colorsDict["kazooBottom"])
        imNew.putpixel((16, 17), colorsDict["kazooBottom"])
        imNew.putpixel((17, 17), colorsDict["kazooBottom"])
    elif decodedType == "Money":
        imNew.putpixel((11, 16), colorsDict["moneyOuter"])
        imNew.putpixel((12, 16), colorsDict["moneyOuter"])
        imNew.putpixel((13, 16), colorsDict["moneyOuter"])
        imNew.putpixel((14, 16), colorsDict["moneyOuter"])
        imNew.putpixel((15, 16), colorsDict["moneyOuter"])
        imNew.putpixel((16, 16), colorsDict["moneyOuter"])
        imNew.putpixel((17, 16), colorsDict["moneyOuter"])
        imNew.putpixel((18, 16), colorsDict["moneyOuter"])

        imNew.putpixel((11, 17), colorsDict["moneyOuter"])
        imNew.putpixel((12, 17), colorsDict["moneyAccent"])
        imNew.putpixel((13, 17), colorsDict["moneyInner"])
        imNew.putpixel((14, 17), colorsDict["black"])
        imNew.putpixel((15, 17), colorsDict["moneyInner"])
        imNew.putpixel((16, 17), colorsDict["moneyInner"])
        imNew.putpixel((17, 17), colorsDict["moneyAccent"])
        imNew.putpixel((18, 17), colorsDict["moneyOuter"])

        imNew.putpixel((11, 18), colorsDict["moneyOuter"])
        imNew.putpixel((12, 18), colorsDict["moneyAccent"])
        imNew.putpixel((13, 18), colorsDict["moneyInner"])
        imNew.putpixel((14, 18), colorsDict["moneyInner"])
        imNew.putpixel((15, 18), colorsDict["black"])
        imNew.putpixel((16, 18), colorsDict["moneyInner"])
        imNew.putpixel((17, 18), colorsDict["moneyAccent"])
        imNew.putpixel((18, 18), colorsDict["moneyOuter"])

        imNew.putpixel((11, 19), colorsDict["moneyOuter"])
        imNew.putpixel((12, 19), colorsDict["moneyOuter"])
        imNew.putpixel((13, 19), colorsDict["moneyOuter"])
        imNew.putpixel((14, 19), colorsDict["moneyOuter"])
        imNew.putpixel((15, 19), colorsDict["moneyOuter"])
        imNew.putpixel((16, 19), colorsDict["moneyOuter"])
        imNew.putpixel((17, 19), colorsDict["moneyOuter"])
        imNew.putpixel((18, 19), colorsDict["moneyOuter"])
    elif decodedType == "FireBreath":
        imNew.putpixel((20, 10), colorsDict["fireRed"])

        imNew.putpixel((22, 11), colorsDict["fireRed"])

        imNew.putpixel((17, 12), colorsDict["fireRed"])
        imNew.putpixel((18, 12), colorsDict["fireRed"])
        imNew.putpixel((19, 12), colorsDict["fireRed"])
        imNew.putpixel((20, 12), colorsDict["fireRed"])

        imNew.putpixel((16, 13), colorsDict["fireRed"])
        imNew.putpixel((17, 13), colorsDict["fireOrange"])
        imNew.putpixel((18, 13), colorsDict["fireRed"])

        imNew.putpixel((14, 14), colorsDict["fireRed"])
        imNew.putpixel((15, 14), colorsDict["fireOrange"])
        imNew.putpixel((16, 14), colorsDict["fireOrange"])
        imNew.putpixel((17, 14), colorsDict["fireYellow"])
        imNew.putpixel((18, 14), colorsDict["fireOrange"])
        imNew.putpixel((19, 14), colorsDict["fireRed"])
        imNew.putpixel((21, 14), colorsDict["fireRed"])

        imNew.putpixel((13, 15), colorsDict["fireRed"])
        imNew.putpixel((14, 15), colorsDict["fireOrange"])
        imNew.putpixel((15, 15), colorsDict["fireYellow"])
        imNew.putpixel((16, 15), colorsDict["fireYellow"])
        imNew.putpixel((17, 15), colorsDict["fireYellow"])
        imNew.putpixel((18, 15), colorsDict["fireYellow"])
        imNew.putpixel((19, 15), colorsDict["fireOrange"])
        imNew.putpixel((20, 15), colorsDict["fireRed"])

        imNew.putpixel((11, 16), colorsDict["fireYellow"])
        imNew.putpixel((12, 16), colorsDict["fireYellow"])
        imNew.putpixel((13, 16), colorsDict["fireYellow"])
        imNew.putpixel((14, 16), colorsDict["fireYellow"])
        imNew.putpixel((15, 16), colorsDict["fireYellow"])
        imNew.putpixel((16, 16), colorsDict["fireYellow"])
        imNew.putpixel((17, 16), colorsDict["fireYellow"])
        imNew.putpixel((18, 16), colorsDict["fireYellow"])
        imNew.putpixel((19, 16), colorsDict["fireYellow"])
        imNew.putpixel((20, 16), colorsDict["fireOrange"])
        imNew.putpixel((21, 16), colorsDict["fireRed"])
        imNew.putpixel((22, 16), colorsDict["fireRed"])

        imNew.putpixel((13, 17), colorsDict["fireRed"])
        imNew.putpixel((14, 17), colorsDict["fireOrange"])
        imNew.putpixel((15, 17), colorsDict["fireYellow"])
        imNew.putpixel((16, 17), colorsDict["fireYellow"])
        imNew.putpixel((17, 17), colorsDict["fireYellow"])
        imNew.putpixel((18, 17), colorsDict["fireYellow"])
        imNew.putpixel((19, 17), colorsDict["fireOrange"])
        imNew.putpixel((20, 17), colorsDict["fireRed"])

        imNew.putpixel((14, 18), colorsDict["fireRed"])
        imNew.putpixel((15, 18), colorsDict["fireOrange"])
        imNew.putpixel((16, 18), colorsDict["fireOrange"])
        imNew.putpixel((17, 18), colorsDict["fireYellow"])
        imNew.putpixel((18, 18), colorsDict["fireOrange"])
        imNew.putpixel((19, 18), colorsDict["fireRed"])
        imNew.putpixel((23, 18), colorsDict["fireRed"])

        imNew.putpixel((15, 19), colorsDict["fireRed"])
        imNew.putpixel((16, 19), colorsDict["fireRed"])
        imNew.putpixel((17, 19), colorsDict["fireOrange"])
        imNew.putpixel((18, 19), colorsDict["fireRed"])

        imNew.putpixel((17, 20), colorsDict["fireRed"])
        imNew.putpixel((18, 20), colorsDict["fireRed"])
        imNew.putpixel((19, 20), colorsDict["fireRed"])
        imNew.putpixel((20, 20), colorsDict["fireRed"])
        imNew.putpixel((22, 20), colorsDict["fireRed"])

        imNew.putpixel((20, 22), colorsDict["fireRed"])
    elif decodedType == "Bone":

        imNew.putpixel((11, 15), colorsDict["black"])
        imNew.putpixel((12, 15), colorsDict["black"])
        imNew.putpixel((19, 15), colorsDict["black"])
        imNew.putpixel((20, 15), colorsDict["black"])

        imNew.putpixel((10, 16), colorsDict["black"])
        imNew.putpixel((11, 16), colorsDict["bone"])
        imNew.putpixel((12, 16), colorsDict["bone"])
        imNew.putpixel((13, 16), colorsDict["black"])
        imNew.putpixel((18, 16), colorsDict["black"])
        imNew.putpixel((19, 16), colorsDict["bone"])
        imNew.putpixel((20, 16), colorsDict["bone"])
        imNew.putpixel((21, 16), colorsDict["black"])

        imNew.putpixel((10, 17), colorsDict["black"])
        imNew.putpixel((11, 17), colorsDict["bone"])
        imNew.putpixel((12, 17), colorsDict["bone"])
        imNew.putpixel((13, 17), colorsDict["bone"])
        imNew.putpixel((14, 17), colorsDict["black"])
        imNew.putpixel((15, 17), colorsDict["black"])
        imNew.putpixel((16, 17), colorsDict["black"])
        imNew.putpixel((17, 17), colorsDict["black"])
        imNew.putpixel((18, 17), colorsDict["white"])
        imNew.putpixel((19, 17), colorsDict["bone"])
        imNew.putpixel((20, 17), colorsDict["bone"])
        imNew.putpixel((21, 17), colorsDict["black"])

        imNew.putpixel((11, 18), colorsDict["black"])
        imNew.putpixel((12, 18), colorsDict["bone"])
        imNew.putpixel((13, 18), colorsDict["bone"])
        imNew.putpixel((14, 18), colorsDict["bone"])
        imNew.putpixel((15, 18), colorsDict["bone"])
        imNew.putpixel((16, 18), colorsDict["bone"])
        imNew.putpixel((17, 18), colorsDict["bone"])
        imNew.putpixel((18, 18), colorsDict["bone"])
        imNew.putpixel((19, 18), colorsDict["white"])
        imNew.putpixel((20, 18), colorsDict["black"])

        imNew.putpixel((10, 19), colorsDict["black"])
        imNew.putpixel((11, 19), colorsDict["boneShade"])
        imNew.putpixel((12, 19), colorsDict["bone"])
        imNew.putpixel((13, 19), colorsDict["bone"])
        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["black"])
        imNew.putpixel((16, 19), colorsDict["black"])
        imNew.putpixel((17, 19), colorsDict["black"])
        imNew.putpixel((18, 19), colorsDict["bone"])
        imNew.putpixel((19, 19), colorsDict["bone"])
        imNew.putpixel((20, 19), colorsDict["bone"])
        imNew.putpixel((21, 19), colorsDict["black"])

        imNew.putpixel((10, 20), colorsDict["black"])
        imNew.putpixel((11, 20), colorsDict["boneShade"])
        imNew.putpixel((12, 20), colorsDict["boneShade"])
        imNew.putpixel((13, 20), colorsDict["black"])
        imNew.putpixel((18, 20), colorsDict["black"])
        imNew.putpixel((19, 20), colorsDict["boneShade"])
        imNew.putpixel((20, 20), colorsDict["bone"])
        imNew.putpixel((21, 20), colorsDict["black"])

        imNew.putpixel((11, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((19, 21), colorsDict["black"])
        imNew.putpixel((20, 21), colorsDict["black"])

    elif decodedType == "DiamondBone":

        imNew.putpixel((11, 15), colorsDict["black"])
        imNew.putpixel((12, 15), colorsDict["black"])
        imNew.putpixel((19, 15), colorsDict["black"])
        imNew.putpixel((20, 15), colorsDict["black"])

        imNew.putpixel((10, 16), colorsDict["black"])
        imNew.putpixel((11, 16), colorsDict["diamondBoneShade1"])
        imNew.putpixel((12, 16), colorsDict["diamondBone"])
        imNew.putpixel((13, 16), colorsDict["black"])
        imNew.putpixel((18, 16), colorsDict["black"])
        imNew.putpixel((19, 16), colorsDict["diamondBone"])
        imNew.putpixel((20, 16), colorsDict["white"])
        imNew.putpixel((21, 16), colorsDict["black"])

        imNew.putpixel((10, 17), colorsDict["black"])
        imNew.putpixel((11, 17), colorsDict["diamondBoneShade2"])
        imNew.putpixel((12, 17), colorsDict["diamondBone"])
        imNew.putpixel((13, 17), colorsDict["diamondBone"])
        imNew.putpixel((14, 17), colorsDict["black"])
        imNew.putpixel((15, 17), colorsDict["black"])
        imNew.putpixel((16, 17), colorsDict["black"])
        imNew.putpixel((17, 17), colorsDict["black"])
        imNew.putpixel((18, 17), colorsDict["diamondBoneShade1"])
        imNew.putpixel((19, 17), colorsDict["diamondBone"])
        imNew.putpixel((20, 17), colorsDict["diamondBone"])
        imNew.putpixel((21, 17), colorsDict["black"])

        imNew.putpixel((11, 18), colorsDict["black"])
        imNew.putpixel((12, 18), colorsDict["diamondBone"])
        imNew.putpixel((13, 18), colorsDict["diamondBoneShade1"])
        imNew.putpixel((14, 18), colorsDict["diamondBone"])
        imNew.putpixel((15, 18), colorsDict["diamondBoneShade1"])
        imNew.putpixel((16, 18), colorsDict["diamondBoneShade1"])
        imNew.putpixel((17, 18), colorsDict["diamondBone"])
        imNew.putpixel((18, 18), colorsDict["diamondBone"])
        imNew.putpixel((19, 18), colorsDict["diamondBone"])
        imNew.putpixel((20, 18), colorsDict["black"])

        imNew.putpixel((10, 19), colorsDict["black"])
        imNew.putpixel((11, 19), colorsDict["diamondBoneShade2"])
        imNew.putpixel((12, 19), colorsDict["diamondBone"])
        imNew.putpixel((13, 19), colorsDict["diamondBone"])
        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["black"])
        imNew.putpixel((16, 19), colorsDict["black"])
        imNew.putpixel((17, 19), colorsDict["black"])
        imNew.putpixel((18, 19), colorsDict["diamondBoneShade2"])
        imNew.putpixel((19, 19), colorsDict["diamondBone"])
        imNew.putpixel((20, 19), colorsDict["diamondBoneShade1"])
        imNew.putpixel((21, 19), colorsDict["black"])

        imNew.putpixel((10, 20), colorsDict["black"])
        imNew.putpixel((11, 20), colorsDict["diamondBoneShade2"])
        imNew.putpixel((12, 20), colorsDict["diamondBoneShade2"])
        imNew.putpixel((13, 20), colorsDict["black"])
        imNew.putpixel((18, 20), colorsDict["black"])
        imNew.putpixel((19, 20), colorsDict["diamondBoneShade2"])
        imNew.putpixel((20, 20), colorsDict["diamondBone"])
        imNew.putpixel((21, 20), colorsDict["black"])

        imNew.putpixel((11, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((19, 21), colorsDict["black"])
        imNew.putpixel((20, 21), colorsDict["black"])
    
    elif decodedType == "ChickenBone":

        imNew.putpixel((19, 14), colorsDict["black"])
        imNew.putpixel((20, 14), colorsDict["black"])

        imNew.putpixel((11, 15), colorsDict["black"])
        imNew.putpixel((12, 15), colorsDict["black"])
        imNew.putpixel((17, 15), colorsDict["black"])
        imNew.putpixel((18, 15), colorsDict["black"])
        imNew.putpixel((19, 15), colorsDict["chickenBone2"])
        imNew.putpixel((20, 15), colorsDict["chickenBone2"])
        imNew.putpixel((21, 15), colorsDict["black"])

        imNew.putpixel((10, 16), colorsDict["black"])
        imNew.putpixel((11, 16), colorsDict["bone"])
        imNew.putpixel((12, 16), colorsDict["bone"])
        imNew.putpixel((13, 16), colorsDict["black"])
        imNew.putpixel((16, 16), colorsDict["black"])
        imNew.putpixel((17, 16), colorsDict["chickenBone1"])
        imNew.putpixel((18, 16), colorsDict["chickenBone1"])
        imNew.putpixel((19, 16), colorsDict["chickenBone1"])
        imNew.putpixel((20, 16), colorsDict["chickenBone1"])
        imNew.putpixel((21, 16), colorsDict["chickenBone2"])
        imNew.putpixel((22, 16), colorsDict["black"])

        imNew.putpixel((10, 17), colorsDict["black"])
        imNew.putpixel((11, 17), colorsDict["bone"])
        imNew.putpixel((12, 17), colorsDict["bone"])
        imNew.putpixel((13, 17), colorsDict["bone"])
        imNew.putpixel((14, 17), colorsDict["black"])
        imNew.putpixel((15, 17), colorsDict["black"])
        imNew.putpixel((16, 17), colorsDict["black"])
        imNew.putpixel((17, 17), colorsDict["chickenBone1"])
        imNew.putpixel((18, 17), colorsDict["chickenBone1"])
        imNew.putpixel((19, 17), colorsDict["chickenBone1"])
        imNew.putpixel((20, 17), colorsDict["chickenBone1"])
        imNew.putpixel((21, 17), colorsDict["chickenBone1"])
        imNew.putpixel((22, 17), colorsDict["chickenBone2"])
        imNew.putpixel((23, 17), colorsDict["black"])

        imNew.putpixel((11, 18), colorsDict["black"])
        imNew.putpixel((12, 18), colorsDict["bone"])
        imNew.putpixel((13, 18), colorsDict["bone"])
        imNew.putpixel((14, 18), colorsDict["bone"])
        imNew.putpixel((15, 18), colorsDict["bone"])
        imNew.putpixel((16, 18), colorsDict["chickenBone3"])
        imNew.putpixel((17, 18), colorsDict["chickenBone1"])
        imNew.putpixel((18, 18), colorsDict["chickenBone1"])
        imNew.putpixel((19, 18), colorsDict["chickenBone1"])
        imNew.putpixel((20, 18), colorsDict["chickenBone1"])
        imNew.putpixel((21, 18), colorsDict["chickenBone1"])
        imNew.putpixel((22, 18), colorsDict["chickenBone1"])
        imNew.putpixel((23, 18), colorsDict["black"])

        imNew.putpixel((10, 19), colorsDict["black"])
        imNew.putpixel((11, 19), colorsDict["boneShade"])
        imNew.putpixel((12, 19), colorsDict["bone"])
        imNew.putpixel((13, 19), colorsDict["bone"])
        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["black"])
        imNew.putpixel((16, 19), colorsDict["black"])
        imNew.putpixel((17, 19), colorsDict["chickenBone1"])
        imNew.putpixel((18, 19), colorsDict["chickenBone1"])
        imNew.putpixel((19, 19), colorsDict["chickenBone1"])
        imNew.putpixel((20, 19), colorsDict["chickenBone1"])
        imNew.putpixel((21, 19), colorsDict["chickenBone1"])
        imNew.putpixel((22, 19), colorsDict["chickenBone3"])
        imNew.putpixel((23, 19), colorsDict["black"])

        imNew.putpixel((10, 20), colorsDict["black"])
        imNew.putpixel((11, 20), colorsDict["boneShade"])
        imNew.putpixel((12, 20), colorsDict["boneShade"])
        imNew.putpixel((13, 20), colorsDict["black"])
        imNew.putpixel((16, 20), colorsDict["black"])
        imNew.putpixel((17, 20), colorsDict["chickenBone3"])
        imNew.putpixel((18, 20), colorsDict["chickenBone3"])
        imNew.putpixel((19, 20), colorsDict["chickenBone1"])
        imNew.putpixel((20, 20), colorsDict["chickenBone1"])
        imNew.putpixel((21, 20), colorsDict["chickenBone3"])
        imNew.putpixel((22, 20), colorsDict["black"])

        imNew.putpixel((11, 21), colorsDict["black"])
        imNew.putpixel((12, 21), colorsDict["black"])
        imNew.putpixel((17, 21), colorsDict["black"])
        imNew.putpixel((18, 21), colorsDict["black"])
        imNew.putpixel((19, 21), colorsDict["chickenBone3"])
        imNew.putpixel((20, 21), colorsDict["chickenBone3"])
        imNew.putpixel((21, 21), colorsDict["black"])

        imNew.putpixel((19, 22), colorsDict["black"])
        imNew.putpixel((20, 22), colorsDict["black"])

    elif decodedType == "TongueOut":
        imNew.putpixel((11, 16), colorsDict["tongue"])
        imNew.putpixel((12, 16), colorsDict["tongue"])
        imNew.putpixel((11, 17), colorsDict["tongue"])
        imNew.putpixel((12, 17), colorsDict["tongue"])
        imNew.putpixel((11, 18), colorsDict["tongue"])
        imNew.putpixel((12, 18), colorsDict["tongue"])

    elif decodedType == "Joint":
        imNew.putpixel((21, 9), colorsDict["jointSmoke"])

        imNew.putpixel((20, 10), colorsDict["jointSmoke"])
        imNew.putpixel((21, 10), colorsDict["jointSmoke"])
        imNew.putpixel((22, 10), colorsDict["jointSmoke"])

        imNew.putpixel((20, 11), colorsDict["jointSmoke"])
        imNew.putpixel((21, 11), colorsDict["jointSmoke"])
        imNew.putpixel((22, 11), colorsDict["jointSmoke"])

        if typeEncoding not in typesWithoutHighEyes:
            imNew.putpixel((8, 12), colorsDict["jointEyes"])
            imNew.putpixel((14, 12), colorsDict["jointEyes"])

        imNew.putpixel((21, 12), colorsDict["jointSmoke"])

        imNew.putpixel((21, 14), colorsDict["jointSmoke"])

        imNew.putpixel((11, 16), colorsDict["black"])
        imNew.putpixel((12, 16), colorsDict["joint"])
        imNew.putpixel((13, 16), colorsDict["black"])
        imNew.putpixel((21, 16), colorsDict["jointSmoke"])

        imNew.putpixel((11, 17), colorsDict["black"])
        imNew.putpixel((12, 17), colorsDict["black"])
        imNew.putpixel((13, 17), colorsDict["joint"])
        imNew.putpixel((14, 17), colorsDict["black"])

        imNew.putpixel((13, 18), colorsDict["black"])
        imNew.putpixel((14, 18), colorsDict["joint"])
        imNew.putpixel((15, 18), colorsDict["black"])
        imNew.putpixel((16, 18), colorsDict["black"])
        imNew.putpixel((17, 18), colorsDict["black"])
        imNew.putpixel((20, 18), colorsDict["jointSmoke"])

        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["joint"])
        imNew.putpixel((16, 19), colorsDict["jointBurn"])
        imNew.putpixel((17, 19), colorsDict["black"])
        imNew.putpixel((19, 19), colorsDict["jointSmoke"])

        imNew.putpixel((15, 20), colorsDict["black"])
        imNew.putpixel((16, 20), colorsDict["black"])
        imNew.putpixel((17, 20), colorsDict["black"])

    elif decodedType == "Pipe":
        imNew.putpixel((20, 11), colorsDict["pipeSmoke"])
        imNew.putpixel((21, 11), colorsDict["pipeSmoke"])
        imNew.putpixel((22, 11), colorsDict["pipeSmoke"])
        imNew.putpixel((21, 12), colorsDict["pipeSmoke"])
        imNew.putpixel((21, 14), colorsDict["pipeSmoke"])

        imNew.putpixel((11, 16), colorsDict["black"])
        imNew.putpixel((12, 16), colorsDict["pipe"])
        imNew.putpixel((13, 16), colorsDict["black"])
        imNew.putpixel((20, 16), colorsDict["pipeSmoke"])

        imNew.putpixel((11, 17), colorsDict["black"])
        imNew.putpixel((12, 17), colorsDict["black"])
        imNew.putpixel((13, 17), colorsDict["pipe"])
        imNew.putpixel((14, 17), colorsDict["black"])
        imNew.putpixel((18, 17), colorsDict["black"])
        imNew.putpixel((19, 17), colorsDict["black"])
        imNew.putpixel((20, 17), colorsDict["black"])
        imNew.putpixel((21, 17), colorsDict["black"])

        imNew.putpixel((13, 18), colorsDict["black"])
        imNew.putpixel((14, 18), colorsDict["pipe"])
        imNew.putpixel((15, 18), colorsDict["black"])
        imNew.putpixel((18, 18), colorsDict["black"])
        imNew.putpixel((19, 18), colorsDict["pipe"])
        imNew.putpixel((20, 18), colorsDict["pipe"])
        imNew.putpixel((21, 18), colorsDict["black"])

        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["pipe"])
        imNew.putpixel((16, 19), colorsDict["black"])
        imNew.putpixel((18, 19), colorsDict["black"])
        imNew.putpixel((19, 19), colorsDict["pipe"])
        imNew.putpixel((20, 19), colorsDict["pipe"])
        imNew.putpixel((21, 19), colorsDict["black"])

        imNew.putpixel((15, 20), colorsDict["black"])
        imNew.putpixel((16, 20), colorsDict["pipe"])
        imNew.putpixel((17, 20), colorsDict["black"])
        imNew.putpixel((18, 20), colorsDict["black"])
        imNew.putpixel((19, 20), colorsDict["pipe"])
        imNew.putpixel((20, 20), colorsDict["pipe"])
        imNew.putpixel((21, 20), colorsDict["black"])
       
        imNew.putpixel((16, 21), colorsDict["black"])
        imNew.putpixel((17, 21), colorsDict["pipe"])
        imNew.putpixel((18, 21), colorsDict["pipe"])
        imNew.putpixel((19, 21), colorsDict["pipe"])
        imNew.putpixel((20, 21), colorsDict["black"])

        imNew.putpixel((17, 22), colorsDict["black"])
        imNew.putpixel((18, 22), colorsDict["black"])
        imNew.putpixel((19, 22), colorsDict["black"])
    
        
    elif decodedType == "Vape":
        imNew.putpixel((22, 13), colorsDict["pipeSmoke"])

        imNew.putpixel((21, 14), colorsDict["pipeSmoke"])
        imNew.putpixel((22, 14), colorsDict["solanaBand"][14])
        imNew.putpixel((23, 14), colorsDict["pipeSmoke"])

        imNew.putpixel((21, 15), colorsDict["pipeSmoke"])
        imNew.putpixel((22, 15), colorsDict["solanaBand"][15])
        imNew.putpixel((23, 15), colorsDict["pipeSmoke"])

        imNew.putpixel((11, 16), colorsDict["black"])
        imNew.putpixel((12, 16), colorsDict["vape"])
        imNew.putpixel((13, 16), colorsDict["black"])
        imNew.putpixel((22, 16), colorsDict["pipeSmoke"])
    
        imNew.putpixel((11, 17), colorsDict["black"])
        imNew.putpixel((12, 17), colorsDict["black"])
        imNew.putpixel((13, 17), colorsDict["vape"])
        imNew.putpixel((14, 17), colorsDict["black"])

        imNew.putpixel((13, 18), colorsDict["black"])
        imNew.putpixel((14, 18), colorsDict["vape"])
        imNew.putpixel((15, 18), colorsDict["black"])
        imNew.putpixel((22, 18), colorsDict["pipeSmoke"])

        imNew.putpixel((14, 19), colorsDict["black"])
        imNew.putpixel((15, 19), colorsDict["vape"])
        imNew.putpixel((16, 19), colorsDict["black"])
        imNew.putpixel((17, 19), colorsDict["black"])
        imNew.putpixel((18, 19), colorsDict["black"])
  
        imNew.putpixel((15, 20), colorsDict["black"])
        imNew.putpixel((16, 20), colorsDict["vape"])
        imNew.putpixel((17, 20), colorsDict["vapeLight"])
        imNew.putpixel((18, 20), colorsDict["black"])
        imNew.putpixel((21, 20), colorsDict["pipeSmoke"])
        
        imNew.putpixel((16, 21), colorsDict["black"])
        imNew.putpixel((17, 21), colorsDict["black"])
        imNew.putpixel((18, 21), colorsDict["black"]) 

    im.paste(imNew, (0,0), mask=imNew)
