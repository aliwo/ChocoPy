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


for i in range(10):
    k, s, m = get_choco_ingredients() # 일단은 초코만 생각하자!
    if kakao >= k and sugar >= s and milk >= m:
        kakao -= k
        sugar -= s
        milk -= m
        choco += 1
    else:
        print('재료가 부족합니다!')
        break





