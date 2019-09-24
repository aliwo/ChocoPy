from choco_py.complete.chocos.choco import Choco
from choco_py.complete.chocos.dark_choco import DarkChoco
from choco_py.complete.chocos.milk_choco import MilkChoco


class WareHouse():

    chocos = []
    milk_chocos = []
    dark_chocos = []

    def __init__(self):
        self.chocos_dict = {
            '초코': self.chocos,
            '밀크초코': self.milk_chocos,
            '다크초코': self.dark_chocos,
        }

    def store(self, choco):
        # TODO: append 와 pop() 만 사용하면 제일 오래된 초코가 남겠죠? queue 를 사용해 볼까요?
        if isinstance(choco, MilkChoco):
            self.milk_chocos.append(choco)
            return

        if isinstance(choco, DarkChoco):
            self.dark_chocos.append(choco)
            return

        if isinstance(choco, Choco):
            self.chocos.append(choco)
            return


    def peek(self, choco_name):
        return len(self.chocos_dict[choco_name])

    def pop(self, choco_name):
        return self.chocos_dict[choco_name].pop()
