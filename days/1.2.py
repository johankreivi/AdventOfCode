
import re
from shlex import join

puzzleInput = open(r"input/1.txt", "r").read()

regX = r"((?P<leftList>\d+)* +(?P<rightList>\d+)*)"

fullIter = re.finditer(regX, puzzleInput)

fullMatch = list(fullIter)

leftSide = []
rightSide = []

score = 0

for m in fullMatch:
    left = m.group("leftList")
    right = m.group("rightList")
    leftSide.append(left)
    rightSide.append(right)


leftSide.sort()
rightSide.sort()
combined = zip(leftSide, rightSide)

for n in combined:
    L = int(n[0])
    R = int(n[1])
    numOfHits = rightSide.count(str(L))
    pointsToAdd = numOfHits * L
    score += pointsToAdd
    if pointsToAdd > 0:
        print(f'number of hits: {numOfHits} * {L} = {pointsToAdd}')
        print(f'score acc: {score}')

print(f'Final score: {score}')