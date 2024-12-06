import math
from functools import cmp_to_key

def useExampleInputs():
  splitInput = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split("\n\n")
  return splitInput[0], splitInput[1]

def parseInputText():
  result = ""
  with open('input.txt', 'r') as fp:
    result = fp.read()
  splitInput = result.split("\n\n")
  return splitInput[0], splitInput[1]

def orderFulfillsRule(pageNumbers, rule):
  try:
    indexLeft = pageNumbers.index(rule[0])
    indexRight = pageNumbers.index(rule[1])

    return indexLeft <= indexRight
  except(ValueError):
    return True

def isValidOrder(pageNumbers, rules):
  for rule in rules:
    if not orderFulfillsRule(pageNumbers, rule):
      return False
  return True

# rulesText, updatesText = useExampleInputs()
rulesText, updatesText = parseInputText()

rules = []
for line in rulesText.split("\n"):
  nums = line.split("|")
  rules.append((int(nums[0]), int(nums[1])))

# note for later:
# To me the quick (to write) solution seems to be to use the
# default python sort functions to reorder the list if it violates the rules
# however, I feel like there must be a better way. Maybe I can go back later
# and create a predefined accepted order based on the rules and order by that
# instead of having ot iterate and check each rule for every compare
def compareByRuleOrder(left, right):
  if isValidOrder([left, right], rules):
    return -1
  return 1

updates = [line.split(",") for line in updatesText.split("\n") if len(line) > 0]
result = 0
for updatePages in updates:
  pageNums = [int(p) for p in updatePages]
  if not isValidOrder(pageNums, rules):
    sortedPages = sorted(pageNums, key=cmp_to_key(compareByRuleOrder))
    midpoint = math.ceil(len(pageNums)/2)-1
    middlePage = sortedPages[midpoint]
    result += middlePage

print(result)