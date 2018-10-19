# 에라토스테네스의 체
# Python Programming
#
# Code by DongEon Kim

count = int(input("마지막 숫자를 입력해주세요 : "))
items = []
print()

print("# 에라토스테네스의 체에 거르기 전")

for i in range(1, count+1):
    print(i, end='\t')
    items.append(i)
    if i % 10 == 0:
        print()

items.remove(1)     # 1은 소수가 아니므로 먼저 제거하고 시작한다

# 체에 거르는 작업
for i in items:
    t = 2
    n = i*t
    while n <= count:
        if items.count(n) > 0:
            items.remove(n)
        t += 1
        n = i*t

print()
print("# 에라토스테네스의 체에 거른 후")

# 거른 결과를 출력하는 작업
# 체에 걸러진 수는 출력하지 않고 공백을 출력한다
for i in range(1, count+1):
    if i in items:
        print(i, end='\t')
    else:
        print(' ', end='\t')

    if i % 10 == 0:
        print()

print()
print("1에서 %d까지의 숫자 중에서 소수는", end=' ')

for i in items:
    print(i, end=', ')
