from random import shuffle

yapp_12th = [
    '김관현'
    ,'편주영'
    ,'이림아'
    ,'이승연'
    ,'박주현'
    ,'조수근'
    ,'김지영'
    ,'이지연'
    ,'이주리'
    ,'명수현'
    ,'박소현'
    ,'박수영'
    ,'이한결'
    ,'양현준'
    ,'김현진'
    ,'양희지'
    ,'박성호'
    ,'김다연'
    ,'최다희'
    ,'노현영'
    ,'노한나'
    ,'김지연'
    ,'김훈정'
    ,'이은경'
    ,'장윤정'
    ,'고준희'
    ,'김예림'
    ,'김보현'
    ,'강희룡'
    ,'서명윤'
    ,'김혜연'

]

부분참석 = [
    '오혜준, 13일만'
    ,'양은비, 13일 full 및 14일 저녁시간대만'
]

합격자중_ot참석불가 = [
    '김보경'
    ,'김지희'
    , '양종열'
    , '조이수'
    , '김수현'
    , '서명윤'
]

shuffle(yapp_12th)

for i, elem in enumerate(yapp_12th, 4):
    print(i)
    print((yapp_12th[i:i+4]))





print('낙오자!')
print(yapp_12th)