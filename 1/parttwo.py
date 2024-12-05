# example:
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3

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
list2Counts = {}
similarity = 0

for item in list2:
  if item in list2Counts:
    list2Counts[item] += 1
  else:
    list2Counts[item] = 1

for item in list1:
  count = list2Counts.get(item) or 0
  similarity += item * count

print(similarity)