from ast import List
from ctypes import sizeof


puzzleinput = open(r'input/2.txt', 'r').read()

reports = puzzleinput.split('\n')
print(reports)

def checkLevel(level: list[int]) -> bool:

    litSize = level.__len__() - 1

    for i, v in enumerate(level):
        if i == 0 and v < level[i + 1]:
            trend = 1
            print(f'First value: {v} is smaller than next value: {level[i + 1]}, trend is positive')
        elif i == 0 and v > level[i + 1]:
            trend = -1
            print(f'First value: {v} is bigger than next value: {level[i + 1]}, trend is negative')

        print(f'Size: {litSize}')
        print(f'Index: {i}')

        if i == litSize:
            print('End of list, returning True')
            return True
        
        nextValue = level[i + 1]
        
        if v > nextValue and trend == 1:
            print('Trend has changed to from positive to negative, returning False')
            return False
        
        if v < nextValue and trend == -1:
            print('Trend has changed from negative to positive, returning False')
            return False

        if (4 > (v - nextValue) | (v - nextValue) > -4) & ((v - nextValue) != 0):
            print(f'Current value: {v} is not too far from next value: {nextValue}, continuing')
            continue

        else:
            print('Difference is too high, returning False')
            return False

numberOfSafeLevels = 0
listOfSafeLevels = []
for report in reports:
    level = report.split()
    level = [int(i) for i in level]
    if checkLevel(level):
        numberOfSafeLevels += 1
        listOfSafeLevels.append(level)

print(f'List of safe levels: {listOfSafeLevels}')
print()
print(f'Number of safe levels: {numberOfSafeLevels}')
