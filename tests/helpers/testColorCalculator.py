__author__ = 'Agile Developers'
from unittest import TestCase
from unittest import skip
import helpers.colorCalculator

class TestFileReader(TestCase):

    def testGettingRgbColor(self):

        foundColor = helpers.colorCalculator.getColorByRGB(240, 248, 255)
        self.assertEquals("AliceBlue", foundColor['name'])
        self.assertEquals("F0F8FF", foundColor['hex'])
        self.assertEquals("240,248,255", foundColor['rgb'])

    def testGettingHexColor(self):

        foundColor = helpers.colorCalculator.getColorByHex("F0F8FF")
        self.assertEquals("AliceBlue", foundColor['name'])
        self.assertEquals("F0F8FF", foundColor['hex'])
        self.assertEquals("240,248,255", foundColor['rgb'])

    def testGettingRgbAndHexForColorname(self):

        foundRgbAndHex = helpers.colorCalculator.getRgbAndHexByColorname("AliceBlue")
        self.assertEquals("240,248,255", foundRgbAndHex["rgb"])
        self.assertEquals("F0F8FF", foundRgbAndHex["hex"])
        self.assertEquals("AliceBlue", foundRgbAndHex["name"])

    '''
    skip("first refactor other tests")
    def testCalculateColorMix(self):

        blue = "0,0,255"
        percent = 50
        foundColor = helpers.colorCalculator.calculateUniColorMixByPercent(blue, "blue", percent)

        self.assertEquals("0,0,128", foundColor['rgb'])

    '''