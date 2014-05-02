__author__ = 'Agile Developers'
from unittest import TestCase
from unittest import skip
import helpers.colorCalculator

class TestFileReader(TestCase):

    def testGettingRgbColor(self):

        foundColor = helpers.colorCalculator.getColorByRGB(240, 248, 255)
        self.assertEquals("AliceBlue", foundColor)

    def testGettingHexColor(self):

        foundColor = helpers.colorCalculator.getColorByHex("F0F8FF")
        self.assertEquals("AliceBlue", foundColor)

    def testGettingRgbAndHexForColorname(self):

        foundRgbAndHex = helpers.colorCalculator.getRgbAndHexByColorname("AliceBlue")
        self.assertEquals("240,248,255", foundRgbAndHex["rgb"])
        self.assertEquals("F0F8FF", foundRgbAndHex["hex"])