
class Shop():

    def __init__(self, warehouse):
        self.warehouse = warehouse

    def sell(self, money ,order_spec):
        '''
        초코 객체와 거스름돈이 담긴 dict 를 리턴
        '''
        result = []
        for key, value in order_spec:
            if key == '초코':
                self.warehouse.pop()
