import sys
from Converter import Converter 

amount = float(sys.argv[1])
src_currency=  sys.argv[2]
dest_currency= sys.argv[3]
reference_date= sys.argv[4]


converter = Converter( amount, src_currency, dest_currency, reference_date)
result = converter.execute()

print(result)
sys.stdout.flush()
