import random
from datetime import datetime


class Choco:
    kakao = 60
    sugar = 120
    milk = 100
    price = 1000

    def init(self, factory):
        factory.kakao -= self.kakao
        factory.sugar -= self.sugar
        factory.milk -= self.milk
        self.origin = str(factory)
        self.created_at = datetime.now()
        self.taste = random.randint(0, 5)

    def format_report(self):
        created_at = self.created_at.strftime('%Y-%m-%d')
        return f'{created_at} 에 {self.origin}에서 생산된 초콜릿입니다. ' \
               f'\n맛은 {self.taste}입니다.'

    @classmethod
    def requirements(self):
        return self.kakao, self.sugar, self.milk

