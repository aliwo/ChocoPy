# 이곳은 초코 공장입니다.

choco = 60 + 120 + 100
milk_choco = 60 + 120 + 200
dark_choco = 90 + 120 + 100

def make_choco(): # def 는 define 의 약자로, '정의'한다는 뜻이다.
    # 함수 안에는 choco 를 만드는 과정이 그대로 적혀 있다.
    global kakao, sugar, milk
    kakao -= 60
    sugar -= 120
    milk -= 100

make_choco() # 함수 호출
print(kakao) # 940
print(sugar) # 940
print(milk) # 940

# 다음은 공장의 총 재료양 입니다.
kakao = 1000
sugar = 1000
milk = 1000
