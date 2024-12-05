def useExampleInputs():
  input_text = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
  return parseLines(input_text.split('\n'))

def parseInputText():
  with open('input.txt', 'r') as fp:
    lines = fp.readlines()
    result = parseLines(lines)
  return result

def parseLines(lines):
  result = []
  for line in lines:
    # if not line:
    #   continue
    values = line.split(' ')
    result.append(list(map(lambda v:float(v), values)))
  return result

# reports = useExampleInputs()
reports = parseInputText()

differences = []
for rpt in reports:
  rptDiffs = []
  for i in range(1, len(rpt)):
    rptDiffs.append(rpt[i] - rpt[i-1])
  differences.append(rptDiffs)

safeCount = 0
for rptDiff in differences:
  allNegative = all(n < 0 for n in rptDiff)
  allPositive = all(n > 0 for n in rptDiff)
  inRange = all(abs(n) >= 1 and abs(n) <= 3 for n in rptDiff)
  if inRange and (allNegative or allPositive):
    safeCount += 1

print(safeCount)