from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    def __init__(self,name, caffeine):
        self.__caffeine = caffeine
        self.MIlLILITERS = 50
        self.PRICE = 3.50
        super().__init__(name, self.PRICE, self.MIlLILITERS)
