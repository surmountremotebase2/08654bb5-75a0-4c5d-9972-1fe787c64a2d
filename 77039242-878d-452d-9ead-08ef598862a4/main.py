from surmount.base_class import Strategy, TargetAllocation

class TradingStrategy(Strategy):

    def __init__(self):
        self.count = 0

    @property
    def assets(self):
        return ["SHOP"]

    @property
    def interval(self):
        return "5min"

    def run(self, data):
        
        if self.count % 2 == 0:
            target_allocation = 1
        else:
            target_allocation = 0
        
        self.count += 1
    
        return TargetAllocation({"SHOP": target_allocation})