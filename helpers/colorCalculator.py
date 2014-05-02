__author__ = 'Agile Developers'

import csv
import os

file = "C:/Users/Agile Developers/PycharmProjects/codingkatas4science/resources/" + 'colorhexrgbtable.csv'
RED = "red"
GREEN = "green"
BLUE = "blue"

def getColorByHex(hexvalue):

    with open(file, newline='') as csvfile:

        colorReader = csv.reader(csvfile, delimiter=';', quotechar='|')
        lineCounter = 1
        for row in colorReader:

            if lineCounter > 1:
                foundColor = __findHexColor(hexvalue, row)
                if foundColor != None:
                    return foundColor
            lineCounter = lineCounter +1

def getColorByRGB(red, green, blue):

    with open(file, newline='') as csvfile:

        colorReader = csv.reader(csvfile, delimiter=';', quotechar='|')
        lineCounter = 1
        for row in colorReader:

            if lineCounter > 1:
                foundColor = __findRgbColor(red, green, blue, row)
                if foundColor != None:
                    return foundColor
            lineCounter = lineCounter +1

def getRgbAndHexByColorname(colorname):

    with open(file, newline='') as csvfile:

        colorReader = csv.reader(csvfile, delimiter=';', quotechar='|')
        lineCounter = 1
        for row in colorReader:

            if lineCounter > 1:
                foundColorInformation = __findColor(colorname, row)
                if foundColorInformation != None:
                    return foundColorInformation
            lineCounter = lineCounter +1
'''
def calculateUniColorMixByPercent(colorInRgb, colorToCalculate, percent):

    # 255,255,255 + 0,0,255

    #Hex-Wert 	RGB-Anteil 	Leuchtkraft (%)
    #00 	        0        	0 %
    #40 	        64 	        25 %
    #80 	        128 	    50 %
    #C0 	        192 	    75 %
    #FF 	        255 	    100 %

    rgbToken = colorInRgb.split(',')

    colorInfo = {}
    if colorToCalculate == BLUE:
        colorInfo['colorname'] = getColorByRGB(rgbToken[0], rgbToken[1], (rgbToken[2] * 0,5))
        colorInfo['']

'''

def __findRgbColor(red, green, blue, colorLine):

    color = {}

    colorname = colorLine[0]
    rgb = colorLine[1]
    hex = colorLine[2]

    rgbTokens = rgb.split(",")
    redFromFile = rgbTokens[0]
    greenFromFile = rgbTokens[1]
    blueFromFile = rgbTokens[2]

    if (redFromFile == str(red)) & (greenFromFile == str(green)) & (blueFromFile == str(blue)):
        color['name'] = colorname
        color['rgb'] = colorLine[1]
        color['hex'] = colorLine[2]
        return color

def __findHexColor(hexvalue, colorLine):

    hexFromFile = colorLine[2]

    color = {}
    if hexvalue == hexFromFile:
        color['name'] = colorLine[0]
        color['rgb'] = colorLine[1]
        color['hex'] = hexFromFile
        return color

def __findColor(colorname, colorLine):

    colornameFromFile = colorLine[0]

    if colornameFromFile == colorname:

        colorRgbAndHex = {}
        colorRgbAndHex['rgb'] = colorLine[1]
        colorRgbAndHex['hex'] = colorLine[2]
        colorRgbAndHex['name'] = colorname
        return colorRgbAndHex