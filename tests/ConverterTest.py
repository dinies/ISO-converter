import unittest
from context import src
from src.Converter import *

class ConverterTest( unittest.TestCase):
    def setUp(self):
        self.amount = 100
        self.src_currency='BGN'
        self.dest_currency='JPY'
        self.reference_date='2020-02-26'
        self.converter = Converter(
                self.amount, self.src_currency,
                self.dest_currency, self.reference_date
                )

    def test_constructor(self):

        self.assertTrue(
            self.converter.getAmount() == self.amount   and
            self.converter.getSrcCurrency() == self.src_currency and
            self.converter.getDestCurrency() == self.dest_currency and
            self.converter.getReferenceDate() == self.reference_date 
        )


    def test_execute_success(self):
        result= self.converter.execute()
        self.assertEqual(result['amount'], 6142.24)
        self.assertEqual(result['currency'] , 'JPY')

    def test_execute_failure(self):
        self.converter.src_currency = 'UUU'
        self.assertEqual(
                self.converter.execute(), 
                {'error message': 'the currencies or the data given as input are not valid'}
                )

    def test_fetchRatio(self):

        self.assertTrue(self.converter.fetchRatio( self.src_currency, self.reference_date) == [1.9558]) 
        self.assertTrue(self.converter.fetchRatio( self.dest_currency, self.reference_date) == [120.13])
        self.assertTrue(self.converter.fetchRatio( 'EUR', self.reference_date) == [1])
        self.assertTrue( not self.converter.fetchRatio( 'UUU', self.reference_date))

if __name__ == '__main__':
    unittest.main()
