from re import finditer, DOTALL, findall

inputString = open(r"input/3.txt", "r").read()

rBetweenDoAndDont = r"(?s)((?<=do\(\))|(^))((.*?))(?=don't\(\))"
rMul = r"(?s)(mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\))"

iterMatchBetweenDoAndDont = finditer(rBetweenDoAndDont, inputString)
itrbetween = list(iterMatchBetweenDoAndDont)

fullStr = ""
for strMatch in itrbetween:
    fullStr += strMatch.group()

iterMatchBetweenDoAndDont = finditer(rMul, fullStr, DOTALL)
findallmatch = findall(rMul, fullStr)
BetweenDoAndDont = list(iterMatchBetweenDoAndDont)

sum = 0

for m in findallmatch:
    sum += int(m[1]) * int(m[2])

print(str(sum))