kakao = 10  # 더 이상 재료가 없다!
sugar = 20
milk = 100


def choco_ingredients():
    return 60, 120, 100  # 필요한 재료의 양만 알려준다.


def milk_choco_ingredients():
    return 60, 120, 200


def dark_choco_ingredients():
    return 60, 120, 200


# 재료가 없는데 초코를 만든다?
k, s, m = choco_ingredients()

kakao_need = kakao - k < 0
sugar_need = sugar - s < 0
milk_need = milk - m < 0

if kakao_need:
    print('카카오 부족')
if sugar_need:
    print('설탕 부족')
if milk_need:
    print('우유 부족')

if kakao_need and sugar_need and milk_need:
    kakao -= k
    sugar -= s
    milk -= m

