def useExampleInputs():
  return """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def parseInputText():
  result = ""
  with open('input.txt', 'r') as fp:
    result = fp.read()
  return result

# rawInput = useExampleInputs()
rawInput = parseInputText()
equations = rawInput.strip().split('\n')

def countResolvedOperators(target, values):
  successCount = 0

  if len(values) < 2:
    return 0
  
  mulTotal = values[0] * values[1]
  sumTotal = values[0] + values[1]

  if len(values) == 2:
    if mulTotal == target:
      successCount += 1
    if sumTotal == target:
      successCount += 1
  else:
    successCount += countResolvedOperators(target, [mulTotal, *values[2:]])
    successCount += countResolvedOperators(target, [sumTotal, *values[2:]])
  return successCount

result = 0
for eq in equations:
  parts = eq.split(": ")
  target = int(parts[0])
  values = [int(num) for num in parts[1].split(" ")]
  possibleConfigs = countResolvedOperators(target, values)
  if possibleConfigs > 0:
    result += target

print(result)