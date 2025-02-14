from surmount.base_class import Strategy, TargetAllocation
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        # Define a ticker for Apple
        self.ticker = "AAPL"
        # Optionally, maintain state to remember the shares bought
        self.shares_held = 0  
    
    @property
    def assets(self):
        # We're only interested in AAPL for this strategy
        return [self.ticker]

    @property
    def interval(self):
        # Use '1hour' interval to check data on an hourly basis
        return "1hour"
    
    def run(self, data):
        # Initialize our target allocation for AAPL with 0 shares (0% of portfolio)
        allocation_dict = {self.ticker: 0.0}

        # Get the current hour from the last data point
        # Assuming data["ohlcv"] is structured correctly and contains a "date" field in each entry
        # This might need adjustment based on the actual structure of data provided by Surmount
        current_hour = int(data["ohlcv"][-1][self.ticker]["date"].split(' ')[1].split(':')[0])
        
        # If it's 12:00, intend to buy 5 shares (represented by setting the allocation to 1 to indicate a buy)
        if current_hour == 12 and self.shares_held == 0:
            log(f"Buying 5 shares of {self.ticker} at 12:00")
            allocation_dict[self.ticker] = 1.0  # This represents a full allocation to AAPL
            self.shares_held = 5  # Mark as bought
        
        # If it's 13:00 and we hold 5 shares, intend to sell all 5 shares (represented by setting allocation to 0 to indicate a sell)
        if current_hour == 13 and self.shares_held == 5:
            log(f"Selling 5 shares of {self.ticker} at 13:00")
            allocation_dict[self.ticker] = 0  # This represents selling off AAPL
            self.shares_held = 0  # Reset shares held

        return TargetAllocation(allocation_dict)