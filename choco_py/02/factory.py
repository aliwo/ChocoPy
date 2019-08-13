# 이곳은 초코 공장입니다.


# 다음은 공장의 총 재료양 입니다.
kakao = 1000
sugar = 1000
milk = 1000

choco = 5
milk_choco = 1
dark_choco = 1


def get_choco_ingredients():
    return 60, 120, 100


def get_milk_choco_ingredients():
    return 60, 120, 200


def get_dark_choco_ingredients():
    return 90, 120, 100


def report(choco, milk_choco, dark_choco):
    '''
    전역변수에 접근해도 되긴 함!
    '''
    print('현재 보유하고 있는 초코의 양은 다음과 같습니다.')
    print(f'초코: {choco}개')
    print(f'밀크 초코: {milk_choco}개')
    print(f'다크 초코: {dark_choco}개')


for i in range(10):
    k, s, m = get_choco_ingredients()
    if kakao >= k and sugar >= s and milk >= m:
        kakao -= k
        sugar -= s
        milk -= m
        choco += 1
    else:
        print('재료가 부족합니다!')
        break





