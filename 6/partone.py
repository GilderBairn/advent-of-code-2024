import re

def useExampleInputs():
  return """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

def parseInputText():
  result = ""
  with open('input.txt', 'r') as fp:
    result = fp.read()
  return result

# inputMap = useExampleInputs()
inputMap = parseInputText()

splitMap = inputMap.split("\n")

charToDir = {
  "^": (0, -1),
  ">": (1, 0),
  "v": (0, 1),
  "<": (-1, 0),
}

nextDir = {
  (-1, 0): (0, -1),
  (0, -1): (1, 0),
  (1, 0): (0, 1),
  (0, 1): (-1, 0),
}

wallPositions = []
guardPos = (0,0)
guardDir = (0, 1)

cury = 0
# init tracking varialbes
for line in splitMap:
  curx = 0
  for char in line:
    if char in "v^><":
      guardPos = (curx, cury)
      guardDir = charToDir[char]
    elif char == "#":
      wallPositions.append((curx, cury))
    curx += 1
  cury += 1

uniqueCoords = set([guardPos])

# def wallInDirection(pos):
#   dirx, diry = guardDir
#   posx, posy = pos
#   guardx, guardy = guardPos
#   okHoriz = dirx == 0 or (dirx == -1 and posx < guardx) or (dirx == 1 and posx > guardx)
#   okVert = diry == 0 or (diry == -1 and posy < guardy) or (diry == 1 and posy > guardy)
#   return okHoriz and okVert

# def closestWallInDir(value):
#   dirx, diry = guardDir
#   guardx, guardy = guardPos
#   select = None
#   if dirx != 0:
#     select = value[0] # comparing on X values
#   else:
#     select = value[1] # comparing on Y values
  
#   # determine if polarity of search
#   if min(value) == -1:
#     return select
#   else:
#     return select * -1

# def getNextWall():
#   wallsInDir = filter(wallInDirection, wallPositions)
#   if len(wallsInDir) == 0:
#     return None
#   sorted(wallsInDir, key=closestWallInDir)
#   return wallsInDir[0]

# simulate guard movement
# nextWall = getNextWall()
# while nextWall:
#   #
#   nextWall = getNextWall()

while guardPos[0] >= 0 and guardPos[1] >= 0:
  dirx, diry = guardDir
  guardx, guardy = guardPos
  nextPos = (guardx + dirx, guardy + diry)
  nextx, nexty = nextPos
  try:
    if (splitMap[nexty][nextx] == "#"):
      #turn
      guardDir = nextDir[guardDir]
    else:
      guardPos = nextPos
      uniqueCoords.add(nextPos)
  except(IndexError):
    break



# track remaining places

# print result
print(len(uniqueCoords))