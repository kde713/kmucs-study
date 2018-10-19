"""
알고리즘 설명
Code by kde713

다이아몬드 형태 출력에서는 공백은 *으로 매우고, 실제 형태는 +로 구성한다.
출력이 먼저되는 것이 *이므로, *의 개수에 중점을 두고 코딩하였다.
입력된 k를 2로 나눈 몫을 중앙값이라 했을때, *의 개수는 2*|중앙값 - 줄 번호| 이다.
"""


def getdiamond(k):
    center = k // 2
    for i in range(k):
        starcnt = abs(center - i)
        print('*' * starcnt + '+' * (k - 2 * starcnt) + '*' * starcnt)


getdiamond(int(input('k=')))
