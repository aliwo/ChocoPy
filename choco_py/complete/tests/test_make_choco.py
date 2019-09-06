from choco_py.complete.factory import Factory
from choco_py.complete.warehouse import WareHouse


def test_make_choco():
    warehouse = WareHouse()
    Factory(1000, 1000, 1000, warehouse)


