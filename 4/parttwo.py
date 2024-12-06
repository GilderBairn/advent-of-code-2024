def useExampleInputs():
  return """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split("\n")

def parseInputText():
  result = ""
  with open('input.txt', 'r') as fp:
    result = fp.readlines()
  return result

# wordSearch = useExampleInputs()
wordSearch = parseInputText()


directions = [
  [(1, 1), (-1, -1)],
  [(1, -1), (-1, 1)],
]

def checkForCrossMas(position):
  x, y = position
  
  # X-MAS cannot occur if the center is on the first or last row/column
  if x <= 0 or y <= 0:
    return False
  if y >= len(wordSearch)-1 or x >= len(wordSearch[y])-1:
    return False
  
  sCount = 0
  mCount = 0

  masCount = 0
  for dir in directions:
    foundWord = "A"
    for pos in dir:
      foundWord += wordSearch[y+pos[1]][x+pos[0]]
    if "S" in foundWord and "A" in foundWord and "M" in foundWord:
      masCount += 1
  
  return masCount == 2

totalXmas = 0
for y, line in enumerate(wordSearch):
  for x, char in enumerate(line):
    if char == "A" and checkForCrossMas((x,y)):
      totalXmas += 1

print(totalXmas)