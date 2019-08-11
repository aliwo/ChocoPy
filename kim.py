kim = 'hi'

def hi():
    global_kim = kim # 전역변수를 지역변수에 할당할 수 있다!
    print(kim) # 전역변수를 출력하는 것도 된다.
    kim = 'new hi' # 전역변수를 수정할 수는 없다!

def hi2():
    kim = 'local kim' # 전역변수와 똑같은 이름의

