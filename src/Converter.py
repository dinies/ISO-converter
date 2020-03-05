import xml.etree.ElementTree as ET

class Converter(object):
    def __init__(self, amount, src_currency, dest_currency, reference_date):
        self.amount = amount
        self.src_currency=src_currency
        self.dest_currency=dest_currency
        self.reference_date=reference_date

    def getAmount(self): 
        return self.amount
    def getSrcCurrency(self): 
        return self.src_currency
    def getDestCurrency(self): 
        return self.dest_currency
    def getReferenceDate(self): 
        return self.reference_date

    def execute(self):
        src_ratio_response = self.fetchRatio( self.src_currency, self.reference_date)
        dest_ratio_response = self.fetchRatio( self.dest_currency, self.reference_date)
        if ( src_ratio_response and dest_ratio_response):
            src_ratio= src_ratio_response[0]
            dest_ratio = dest_ratio_response[0]
            converted_amount = round( (self.amount * dest_ratio) / src_ratio, 2)
            result = {
                'amount':converted_amount,
                'currency':self.dest_currency
                }
        else:
            result = {
                'error message': 'the currencies or the data given as input are not valid'
                }
        return result

    def fetchRatio(self, currency, reference_date):
        if ( currency == 'EUR') :
            return [1]
        else: 
            tree = ET.parse('../data/eurofxref-hist-90d.xml')
            root = tree.getroot()
            namespaces = {
                'ex': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'
                }

            for cube in root.findall('.//ex:Cube[@time="{}"]'.format(reference_date), namespaces= namespaces):
                for subcube in cube: 
                    if ( subcube.attrib['currency'] == currency):
                        return [ float(subcube.attrib['rate'])]
            return []

                   
