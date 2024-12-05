# example:
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3

# list1 = [3,4,2,1,3,3]
# list2 = [4,3,5,3,9,3]

def useExampleInputs():
  return [3,4,2,1,3,3], [4,3,5,3,9,3]

def parseInputText():
  list1 = []
  list2 = []

  with open('input.txt', 'r') as fp:
    lines = fp.readlines()
    for line in lines:
      values = line.split('   ')
      list1.append(int(values[0]))
      list2.append(int(values[1]))
  return list1, list2

# list1, list2 = useExampleInputs()
list1, list2 = parseInputText()

list1.sort()
list2.sort()
deltas = 0

for first, second in zip(list1, list2):
  deltas += abs(first - second)

print(deltas)