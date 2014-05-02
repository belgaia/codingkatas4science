__author__ = 'Agile Developers'
from unittest import TestCase
import helpers.colorCalculator

class TestFileReader(TestCase):

    def testReadingCSVFile(self):

        foundColor = helpers.colorCalculator.getColorByRGB(240, 248, 255)
        self.assertEquals("AliceBlue", foundColor)


