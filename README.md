# BTCconverter
Working on a bigger project to build my own online crypto trading system, I wrote a simple Python based CLI script to compare various currency prices against BTC using the Forex-Python module. This utility had minimal value but it will be used in the larger overarching project.

Usage:
Clone the project and run the convertBTC.py script and pass the Currency Type and the currency amount.

###Examples:

If you want to convert 50 united Kingdom Pound to bitcoin, you would run:

    python convertBTC.py -c GBP -a 50

If you want to convert 5000 USD to BTC, you run:

    python convertBTC.py -c USD -a 5000

Valid input for currencies follow the ISO4217 specification (USD, JPY, GBP, etc.). You can get more detailed information [here](http://www.xe.com/iso4217.php).

###BTC Price calculation:

Per the [forex-python documentation](https://pypi.python.org/pypi/forex-python):

Bitcoin prices calculated every minute. For more information visit [CoinDesk API](http://www.coindesk.com/api/).
