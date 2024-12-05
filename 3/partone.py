import re

def useExampleInputs():
  return """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

def parseInputText():
  result = ""
  with open('input.txt', 'r') as fp:
    result = fp.read()
  return result

#memoryDump = useExampleInputs()
memoryDump = parseInputText()

matches = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", memoryDump)
result = sum([int(left) * int(right) for left, right in matches])
print(result)