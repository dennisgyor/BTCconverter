#!/usr/bin/python
import argparse
from forex_python.bitcoin import BtcConverter

parser = argparse.ArgumentParser(description='Convert currency to BTC.')
parser.add_argument('-c', dest='currency', type=str, default='USD', help='Enter type of currency to convert.')
parser.add_argument('-a', dest='amount', type=float, help='Enter amount of currency to convert.')

args = parser.parse_args()

# usdamount = 400

# create a new converter object
b = BtcConverter()

x = b.get_latest_price(args.currency)
print("The latest price in {} for 1.0 Bitcoin (BTC) is {}".format(args.currency, str(x)))


# convert USD to BTC
a = b.convert_to_btc(args.amount, args.currency)
print("Converting {} to BTC. {} {} is currently worth {} BTC!".format(args.currency, args.amount, args.currency, str(a)))
