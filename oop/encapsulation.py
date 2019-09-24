
class AppleSeller:

    _apple = 20
    _money = 0

    def sell_apple(self, money):
        if money < 500:
            return 0
        self.money += money
        apple_cnt = money // 500
        self.apple = self.apple - apple_cnt
        return apple_cnt


seller = AppleSeller()
seller.sell_apple(1000)
seller.__money = 0




