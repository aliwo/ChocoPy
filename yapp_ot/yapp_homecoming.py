from random import shuffle


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

BYE_BYE = [
 '강희룡',
 '노한나',
 '박수영'
]

YAPP_12기 = [
'정여은',
'문현주',
'강찬영',
'김영중',
'이경원',
'김지연',
'노현영',
'오혜준',
'양은비',
'최다희',
'고준희',
'김관현',
'김다인',
'김보경',
'김보현',
'김수현',
'김예림',
'김현진',
'김혜연',
'명수현',
'박성호',
'박소현',
'박주현',
'서명윤',
'양종열',
'양현준',
'이림아',
'이승연',
'이주리',
'이한결',
'조수근',
'편주영',
]

운영진 = [
    '김하영',
    '원지영',
    '김록범',
    '백승찬',
    '정승원',
    '최성훈',
    '김강산',
    '홍유리',
]

OB = [
    '김환태',
    '백운천',
    '최평강',
    '이나래',
    '최슬기나라',
    '박병호',
    '성아람',
    '유호재',
    '유송이'
]

디자이너들 = [
    '박서진',
    '김훈정',
    '양희지',
    '김하영',
    '김지희',
    '장윤정',
    '김유현',
    '이은경',
]

# YAPP_12기 += OB

shuffle(YAPP_12기)

for i, chunk in enumerate(chunks(YAPP_12기, int(len(YAPP_12기)/ 8))):
    # print(i, chunk)
    if i ==8:
        print('나머지: {}'.format(chunk))
        break
    chunk.insert(0, 디자이너들[i])
    print('팀 {} : {}'.format(i+1, ', '.join(chunk)))
