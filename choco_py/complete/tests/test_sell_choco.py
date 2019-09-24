

from choco_py.complete.factory import Factory
from choco_py.complete.shop import Shop
from choco_py.complete.warehouse import WareHouse


def test_sell_choco():
    warehouse = WareHouse()
    factory = Factory(1000, 1000, 1000, warehouse)
    shop = Shop(warehouse)
    factory.make_choco('초코')
    factory.make_choco('밀크초코')
    factory.make_choco('다크초코')

    result = shop.sell(10000, {'초코':1, '밀크초코':1, '다크초코':1})
    assert result
    print()
    for choco in result['chocos']:
        print(choco.format_report())
    assert 0




