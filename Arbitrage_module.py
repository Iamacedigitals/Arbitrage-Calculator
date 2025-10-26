class Arbitrage:
    #Checks if an arbitrag exists
    #Performs the arbitrage
    def __init__(self, quoted_rate):
        # Specifically for the Implied rate calculations 
        self.quoted_rate = quoted_rate # This also implies the yz rate as in xy,xz (read second try on arbitrage for more info)
        self.implied_rate = 0
        # Specifically for the Pnl Calculations
        self.capital = 1000000
        self.selling_price = 0
        self.charges = (0.01/100)
        self.xy_rate = 0
        self.xz_rate = 0
    def conv_implied_rate(self, xy, xz):
    # xy is the value of the destination currency that was quoted on the exchange with the intermediate,
    # xz is the value quoted with the capital currency
        self.xy_rate = xy
        self.xz_rate = xz
        self.implied_rate = self.xz_rate/self.xy_rate
        # second_implied_rate = self.xz_rate/self.quoted_rate >>> Not really needed
        if self.implied_rate != self.quoted_rate:
            print(f'The quoted is {self.quoted_rate} and the implied is {self.implied_rate}')
            return self.implied_rate
        elif self.implied_rate == self.quoted_rate:
            print(f"Arbitrage doesn't exist")
            return "Not available"
    def conv_pnl(self):
        conv_capital = self.capital/self.quoted_rate # self.quoted is the same as yz
        conv_intermediary = conv_capital / self.xy_rate
        self.selling_price = conv_intermediary * self.xz_rate
        if self.selling_price > (self.capital+self.charges):
            pnl = self.selling_price - (self.capital + self.charges)
            return f'You will get a profit of {pnl}'
        elif self.selling_price < (self.capital+self.charges):
            pnl = (self.capital+self.charges) - self.selling_price
            return f'You will make a loss of {pnl}'
        return self.selling_price