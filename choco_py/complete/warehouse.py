from choco_py.complete.chocos.choco import Choco
from choco_py.complete.chocos.dark_choco import DarkChoco
from choco_py.complete.chocos.milk_choco import MilkChoco


class WareHouse():

    chocos = []
    milk_chocos = []
    dark_chocos = []

    def __init__(self):
        pass

    def store(self, choco):
        if isinstance(choco, Choco):
            self.chocos.append(choco)
            return

        if isinstance(choco, MilkChoco):
            self.milk_chocos.append(choco)
            return

        if isinstance(choco, DarkChoco):
            self.dark_chocos.append(choco)
            return

