import unittest
from csvprinter.csvprinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read1(self):
        printer = CSVPrinter('tests/sample.csv')
        l = printer.read()
        self.assertEqual(2, len(l))
        
        
    def test_read2(self):
        printer = CSVPrinter('tests/sample.csv')
        line = printer.read()
        self.assertEqual(line[1][1], '2')
    
    def test_read3(self):
        printer = CSVPrinter('tests/sample.csv')
        lines = printer.read()
        unittest.TestCase.fail("this line should not be execate")
