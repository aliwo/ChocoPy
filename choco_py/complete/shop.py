
class Shop():

    choco_price = {
        '초코': 1000,
        '밀크초코': 1500,
        '다크초코': 2000
    }

    def __init__(self, warehouse):
        self.warehouse = warehouse

    def sell(self, money, order_spec):
        '''
        초코 객체와 거스름돈이 담긴 dict 를 리턴
        '''

        # 돈이 충분한지 먼저 계산합니다.
        # 모든 초코의 재고가 충분한지 계산하고
        # 충분하다면 choco 를 pop 해서 담은 후 return 합니다.

        result = {
            'chocos': [],
            'change': money
        }

        for key, value in order_spec.items():
            if self.warehouse.peek(key) < value:
                return # 재고 부족!
            result['change'] -= (self.choco_price[key] * value)
            if result['change'] < 0:
                return # 금액 부족!

        for key, value in order_spec.items():
            for _ in range(value):
                result['chocos'].append(self.warehouse.pop(key))

        return result
