__author__ = 'Agile Developers'

import csv
import os

file = "C:/Users/Agile Developers/PycharmProjects/codingkatas4science/resources/" + 'colorhexrgbtable.csv'

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

def getColorByRGB(red, yellow, blue):

    with open(file, newline='') as csvfile:

        colorReader = csv.reader(csvfile, delimiter=';', quotechar='|')
        lineCounter = 1
        for row in colorReader:

            if lineCounter > 1:
                foundColor = __findRgbColor(red, yellow, blue, row)
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


def __findRgbColor(red, yellow, blue, colorLine):

    colorname = colorLine[0]
    rgb = colorLine[1]
    hex = colorLine[2]

    rgbTokens = rgb.split(",")
    redFromFile = rgbTokens[0]
    yellowFromFile = rgbTokens[1]
    blueFromFile = rgbTokens[2]

    if (redFromFile == str(red)) & (yellowFromFile == str(yellow)) & (blueFromFile == str(blue)):
        return colorname

def __findHexColor(hexvalue, colorLine):

    colorname = colorLine[0]
    hexFromFile = colorLine[2]

    if hexvalue == hexFromFile:
        return colorname

def __findColor(colorname, colorLine):

    colornameFromFile = colorLine[0]

    if colornameFromFile == colorname:

        colorRgbAndHex = {}
        colorRgbAndHex['rgb'] = colorLine[1]
        colorRgbAndHex['hex'] = colorLine[2]
        print(colorRgbAndHex)
        return colorRgbAndHex