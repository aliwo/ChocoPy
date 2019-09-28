from abc import ABC

from choco_py.complete.chocos.choco import Choco
from choco_py.complete.chocos.dark_choco import DarkChoco
from choco_py.complete.chocos.milk_choco import MilkChoco
from choco_py.complete.errors.NoRecipeFound import NoRecipeFound
from choco_py.complete.errors.NotEnoughIngredient import NotEnoughIngredient


class Factory:
    '''
    이곳은 초코 생산장입니다.
    '''

    choco_dict = {
        '초코': Choco,
        '밀크초코': MilkChoco,
        '다크초코': DarkChoco,
    }

    def __str__(self):
        return '초코PY 공장'

    def __init__(self, kakao, sugar, milk, warehouse):
        '''
        공장의 초기 재료 보유량을 결정합니다.
        '''
        self.kakao = kakao
        self.sugar = sugar
        self.milk = milk
        self.warehouse = warehouse

    def make_choco(self, name):
        '''
        API 에서 쓰일 함수
        '''
        if name not in self.choco_dict:
            pass
            # raise NoRecipeFound(name)

        choco = self.choco_dict[name]

        k, s, m = choco.requirements()

        if self.kakao < k:
            pass
            # raise NotEnoughIngredient('kakao')

        if self.sugar < s:
            pass
            # raise NotEnoughIngredient('sugar')

        if self.milk < m:
            pass
            # raise NotEnoughIngredient('milk')

        self.warehouse.store(choco(self))


