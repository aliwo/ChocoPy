from choco_py.complete.factory import Factory
from choco_py.complete.warehouse import WareHouse


def test_what():
    '''
    TODO: factory 를 fixture 로 만들어 볼까요 ?
    '''
    warehouse = WareHouse()
    factory = Factory(1000, 1000, 1000, warehouse)
    factory.make_choco('초코')
    choco = warehouse.pop('초코')
    print(choco.format_report())
    # assert 0
    assert choco
