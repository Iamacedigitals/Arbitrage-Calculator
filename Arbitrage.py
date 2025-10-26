from itertools import *
from Arbitrage_module import *

count = 0
currency_list = []
while count < 3:
    currency_query = input("Input Currency: >> ")
    currency_list.append(currency_query)
    count += 1

arbitrage_path = permutations(currency_list) # Gives the permutated list of the currencies
currency_pair_values = {}
value_query = 0
paths = []
symbols = []
inv_symbols = []
for path in arbitrage_path:
    c_symbols = combinations(path, 2)
    paths.append(list(c_symbols))

for quotes in paths:
    if len(currency_pair_values) <= 5:
        symbols.append(f'{quotes[0][0]}{quotes[1][1]}')
        inv_symbols.append(f'{quotes[1][1]}{quotes[0][0]}')
        value_query = float(input(f"Input value for {quotes[0][0]}{quotes[1][1]} : >> "))
        currency_pair_values[f'{quotes[0][0]}{quotes[1][1]}'] = value_query
        currency_pair_values[f'{quotes[1][1]}{quotes[0][0]}'] = 1/value_query


print(symbols)
print(inv_symbols)
print(currency_pair_values)

transaction1 = Arbitrage(currency_pair_values[symbols[2]]) # this initializes the quoted rate of in this case btc usd
transaction1.conv_implied_rate(xy=currency_pair_values[symbols[1]],xz=currency_pair_values[symbols[0]])
print(transaction1.conv_pnl())

transaction2 = Arbitrage(currency_pair_values[symbols[0]])
transaction2.conv_implied_rate(xy=currency_pair_values[inv_symbols[1]],xz=currency_pair_values[symbols[2]])
print(transaction2.conv_pnl())

transaction3 = Arbitrage(currency_pair_values[symbols[1]]) 
transaction3.conv_implied_rate(xy=currency_pair_values[inv_symbols[0]],xz=currency_pair_values[inv_symbols[2]])
print(transaction3.conv_pnl())

transaction4 = Arbitrage(currency_pair_values[inv_symbols[0]])
transaction4.conv_implied_rate(xy=currency_pair_values[symbols[2]],xz=currency_pair_values[inv_symbols[1]])
print(transaction4.conv_pnl())

transaction5 = Arbitrage(currency_pair_values[inv_symbols[1]])
transaction5.conv_implied_rate(xy=currency_pair_values[inv_symbols[2]],xz=currency_pair_values[inv_symbols[0]])
print(transaction5.conv_pnl())

transaction6 = Arbitrage(currency_pair_values[inv_symbols[2]])
transaction6.conv_implied_rate(xy=currency_pair_values[symbols[0]],xz=currency_pair_values[symbols[1]])
print(transaction6.conv_pnl())

# Now this is just a part of the real deal. the real deal will be taking in data from the exchanges and doing stuff with the data taken. 
# Limitations to be broken.
# Knowing how to send request to exchange's data base and use the returned data
# Firstly understanding how the data is structured and how to pull the data into my code -> currency_pair_values, and using the site data to form a list for symbols and inv_symbols so that the transactions can run
# Then using actuall world data create an algorithm that can sort the most profitable arbitrages.
# Find a way to vectorize it so that multiple transactions can actually work simultaneously for instance: the transaction above has only a specific list of element 


