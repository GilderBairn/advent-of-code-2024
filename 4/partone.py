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

nextChars = {
  "M":"A",
  "A":"S",
}

directions = [
  (0, 1),
  (1, 0),
  (-1, 0),
  (0, -1),
  (1, 1),
  (-1, -1),
  (-1, 1),
  (1, -1),
]

def countXmasAllDirections(position):
  x, y = position
  count = 0
  for dir in directions:
    if checkForXmas((x+dir[0], y+dir[1]), dir):
      count += 1
  return count

def checkForXmas(position, direction, currentChar="M"):
  x, y = position

  if currentChar not in "XMAS" or x < 0 or y < 0:
    return False

  found = ""
  try:
    found = wordSearch[y][x]
  except(IndexError):
    return False

  if found != currentChar:
    return False
  if currentChar == "S":
    return True
  
  nextPos = (x+direction[0], y+direction[1])
  return checkForXmas(nextPos, direction, nextChars[currentChar])

totalXmas = 0
for y, line in enumerate(wordSearch):
  for x, char in enumerate(line):
    if char == "X":
      totalXmas += countXmasAllDirections((x, y))

print(totalXmas)