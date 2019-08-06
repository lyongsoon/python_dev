# 구구단 출력 프로그램 구현
# 1. 몇번째 단을 출력할지 단수를 입력받는다
# 2. 입력한 단수 기준 해당 단을 for문으로 출력 한다.

dan = int(input("몇번째 단을 출력하시겠습니까? "))
for num in range(1,10):
    print("{} * {} = {}".format(dan, num, dan * num))
