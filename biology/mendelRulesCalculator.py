__author__ = 'Agile Developers'
from biology.BlossomColor import BlossomColor

def calculateF1Generation(parentOne, parentTwo):

    if parentOne == BlossomColor.WHITE:
        if parentTwo == BlossomColor.RED:
            return BlossomColor.PINK
    elif parentOne == BlossomColor.RED:
        if parentTwo == BlossomColor.WHITE:
            return BlossomColor.PINK
        elif parentTwo == BlossomColor.BLUE:
            return BlossomColor.PURPLE
    elif parentOne == BlossomColor.BLUE:
        if parentTwo == BlossomColor.RED:
            return BlossomColor.PURPLE

    return BlossomColor.UNDEFINED