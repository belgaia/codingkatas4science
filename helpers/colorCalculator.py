__author__ = 'Agile Developers'

import csv
import os

def getColorByRGB(red, yellow, blue):

    readColorFile()
    #readCsvFile

def readColorFile():

    file = "C:/Users/Agile Developers/PycharmProjects/codingkatas4science/resources/" + 'colorhexrgbtable.csv'
    with open(file, newline='') as csvfile:
            colorReader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in colorReader:
                #print(row)
                colorname = row[0]
                rgb = row[1]
                hex = row[2]

                print("colorname: " + colorname + ", rgb: " + rgb + ", hex: " + hex)


def readCsvFile():

    file = "C:/Users/Agile Developers/PycharmProjects/codingkatas4science/resources/" + 'colorhexrgbtable.csv'
    inputFile = csv.DictReader(open(file))

    for row in inputFile:
        print(row)
