import random
import json


class GiveMeAColor:

    # create random color rgb code
    def randomRGB(self):
        rColor = random.randint(0, 255)
        gColor = random.randint(0, 255)
        bColor = random.randint(0, 255)
        response = f'rgb{rColor,gColor,bColor}'
        return response

    # create random color HEX code
    def randomHex(self):
        rColor = random.randint(0, 255)
        gColor = random.randint(0, 255)
        bColor = random.randint(0, 255)
        hexCode = '{:02x}{:02x}{:02x}'.format(
            rColor, gColor, bColor).upper()
        return hexCode

    # create random color with rgb,rgba and hex code
    def generateColor(self):
        rColor = random.randint(0, 255)
        gColor = random.randint(0, 255)
        bColor = random.randint(0, 255)
        hexCode = '{:02x}{:02x}{:02x}'.format(rColor, gColor, bColor).upper()
        color = {
            "HEX": "#"+hexCode,
            "RGB": f'rgb{rColor,gColor,bColor}',
            "RGBA": f'rgb{rColor,gColor,bColor,1}'
        }
        responseColor = json.dumps(color)
        return responseColor
