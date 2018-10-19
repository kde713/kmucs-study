# Sort
import time
import random

items = []

count = int(input("항목 개수를 입력해주세요 : "))
for i in range(count):
    items.append(random.randint(0, count * 10))

print("Random array that contains %d items generated" % (count))

# Python 기본 정렬 알고리즘
target = items[:]
stime = time.time()

target.sort()

print()
print("Python Default Sort Algorithm Completed Sorting in %0.8f sec for %d items" % (time.time() - stime, count))

# 버블 정렬 알고리즘 (일부 수정)
# 의미 없는 루프를 방지하기 위해 noChange 체크 변수를 부여한다
target = items[:]
stime = time.time()

for i in range(0, count):
    noChange = True
    for j in range(0, count - i - 1):
        if target[j] > target[j + 1]:
            t = target[j + 1]
            target[j + 1] = target[j]
            target[j] = t
            noChange = False
    if noChange:
        break

print("Bubble Sort Algorithm Completed Sorting in %0.8f sec for %d items" % (time.time() - stime, count))

# 선택 정렬 알고리즘
target = items[:]
stime = time.time()

chkchange = False
for i in range(0, count):
    mn = target[i]
    for j in range(i, count - 1):
        if mn > target[j + 1]:
            mn = target[j + 1]
            t = j + 1
            chkchange = True
    if chkchange:
        target[t] = target[i]
        target[i] = mn
        chkchange = False

print("Selection Sort Algorithm Completed Sorting in %0.8f sec for %d items" % (time.time() - stime, count))

# 삽입 정렬 알고리즘
target = items[:]
stime = time.time()

for i in range(1, count):
    t = target[i]
    for j in range(i, 0):
        if target[j - 1] > t:
            target[j] = target[j - 1]
            if j == 1:
                target[j - 1] = t
                break
        else:
            target[j] = t
            break

print("Insertion Sort Algorithm Completed Sorting in %0.8f sec for %d items" % (time.time() - stime, count))


# 병합 정렬 알고리즘
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


target = items[:]
stime = time.time()

mergeSort(target)

print("Merge Sort Algorithm Completed Sorting in %0.8f sec for %d items" % (time.time() - stime, count))

target = items[:]
stime = time.time()