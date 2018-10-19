def getweekday(y, m, d):
    print('구하고자 하는 일자는 %d년 %d월 %d일입니다.' % (y, m, d))

    days = 0
    daydic = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    wddic = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']

    # Compute count from 1-01-01
    for i in range(1, y):
        if i % 4 == 0 and i % 100 != 0:
            days += 366
        elif i % 400 == 0:
            days += 366
        else:
            days += 365

    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        daydic[1] = 29

    for i in range(1, m):
        days += daydic[i - 1]

    days += d

    # Compute Weekday
    wd = days % 7
    print('요청하신 날짜는 %s입니다.' % wddic[wd])

getweekday(int(input('년: ')), int(input('월: ')), int(input('일: ')))

