__author__ = 'Agile Developers'

import csv
import os

def getColorByRGB(red, yellow, blue):

    return readColorFile(red, yellow, blue)

def readColorFile(red, yellow, blue):

    file = "C:/Users/Agile Developers/PycharmProjects/codingkatas4science/resources/" + 'colorhexrgbtable.csv'
    with open(file, newline='') as csvfile:
        colorReader = csv.reader(csvfile, delimiter=';', quotechar='|')
        lineCounter = 1
        for row in colorReader:

            if lineCounter > 1:
                colorname = row[0]
                rgb = row[1]
                hex = row[2]

                rgbTokens = rgb.split(",")
                redFromFile = rgbTokens[0]
                yellowFromFile = rgbTokens[1]
                blueFromFile = rgbTokens[2]

                if (redFromFile == str(red)) & (yellowFromFile == str(yellow)) & (blueFromFile == str(blue)):
                    print(colorname)
                    return colorname

            lineCounter = lineCounter +1