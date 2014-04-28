__author__ = 'Agile Developers'

import biology.mendelRulesCalculator
from unittest import TestCase
from biology.BlossomColor import BlossomColor
from biology.HeredityType import HeredityType

class TestMendelRules(TestCase):

    def test_firstMendelRuleRedWhite(self):

        self.f1Gen = biology.mendelRulesCalculator.calculateF1Generation(HeredityType.INTERMEDIUS, BlossomColor.WHITE, BlossomColor.RED)
        self.assertEquals(self.f1Gen, BlossomColor.PINK)

        self.f1Gen = biology.mendelRulesCalculator.calculateF1Generation(HeredityType.INTERMEDIUS, BlossomColor.RED, BlossomColor.WHITE)
        self.assertEquals(self.f1Gen, BlossomColor.PINK)

    def test_firstMendelRuleBlueRed(self):

        self.f1Gen = biology.mendelRulesCalculator.calculateF1Generation(HeredityType.INTERMEDIUS, BlossomColor.BLUE, BlossomColor.RED)
        self.assertEquals(self.f1Gen, BlossomColor.PURPLE)

        self.f1Gen = biology.mendelRulesCalculator.calculateF1Generation(HeredityType.INTERMEDIUS, BlossomColor.RED, BlossomColor.BLUE)
        self.assertEquals(self.f1Gen, BlossomColor.PURPLE)
