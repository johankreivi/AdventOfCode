
import re

puzzleInput = open(r"input/1.txt", "r").read()

regX = r"((?P<leftList>\d+)* +(?P<rightList>\d+)*)"

fullIter = re.finditer(regX, puzzleInput)

fullMatch = list(fullIter)

leftSide = []
rightSide = []

for m in fullMatch:
    left = m.group("leftList")
    right = m.group("rightList")
    leftSide.append(left)
    rightSide.append(right)

leftSide.sort()
rightSide.sort()
combined = zip(leftSide, rightSide)

distsum = 0
for n in combined:
    dist = abs(int(n[0]) - int(n[1]))
    distsum += dist


print(distsum)