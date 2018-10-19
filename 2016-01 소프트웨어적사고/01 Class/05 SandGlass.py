"""
알고리즘 설명
Code by kde713

모래시계 형태 출력 문제에서는 실제 형태를 구성하는 것은 *과 +가 번갈아가며 출력되는 것이므로, 나머지 공간을 매꾸는 -에 중점을 두고 코딩하였다
-의 개수는 입력된 k값을 2로 나눈 몫의 개수까지 증가하고 그 이후로는 다시 감소한다.
"""


def getsandglass(k):
    center = k // 2
    for i in range(k):
        if i <= center:
            cal = i
        else:
            cal = 2 * center - i;
        print('-' * cal, end='')
        for j in range(k - (2 * cal)):
            if j % 2 == 0:
                print('*', end='')
            else:
                print('+', end='')
        print('-' * cal)


getsandglass(int(input('k=')))
