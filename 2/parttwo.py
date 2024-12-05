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


def isReportSafe(rpt):
  diffs = []
  for i in range(1, len(rpt)):
    diffs.append(rpt[i] - rpt[i-1])

  # print(diffs)
  allNegative = all(n < 0 for n in diffs)
  allPositive = all(n > 0 for n in diffs)
  inRange = all(abs(n) >= 1 and abs(n) <= 3 for n in diffs)
  return inRange and (allNegative or allPositive)


def isReportSafeWithProblemDampener(rpt):
  for i in range(len(rpt)):
    splice = rpt[:i] + rpt[i+1:]
    if isReportSafe(splice):
      return True
  return False


# reports = useExampleInputs()
reports = parseInputText()
safeCount = 0

for rpt in reports:
  if isReportSafe(rpt):
    safeCount += 1
  elif isReportSafeWithProblemDampener(rpt):
    safeCount += 1

print(safeCount)