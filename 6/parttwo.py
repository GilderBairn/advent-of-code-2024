# This one really puzzled me, and took me way too long. I did try another approach which feels
# a little better to the first part of the problem as well. I will admit, I did poke around the internet
# a bit after this one stumped me for a while (meaning, the brute-force approach was way too long-running
# for me to accept it as a reasonable solution, and I was looking for something else). What made things click
# for me was to see the advice "only check for walls in the spots which were found in the first step"; that
# might be paraphrasing but you get the gist.

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

splitMap = inputMap.strip().split("\n")

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
yMax = len(splitMap)-1
xMax = len(splitMap[0].strip())-1

cury = 0
# init tracking varialbes
for line in splitMap:
  curx = 0
  for char in line:
    if char in "v^><":
      guardPos = (curx, cury)
      initGuardPos = guardPos
      guardDir = charToDir[char]
      initGuardDir = guardDir
    elif char == "#":
      wallPositions.append((curx, cury))
    curx += 1
  cury += 1

uniqueCoords = set([guardPos])
uniqueCoordsWithDir = set([(guardPos, guardDir)])

def searchWallRight():
  guardx, guardy = guardPos
  wallsToRight = [w for w in filter(lambda pos: pos[1] == guardy and pos[0] > guardx, wallPositions)]
  if len(wallsToRight) == 0:
    return None
  return sorted(wallsToRight, key=lambda pos:pos[0])[0]

def searchWallLeft():
  guardx, guardy = guardPos
  wallsToLeft = [w for w in filter(lambda pos: pos[1] == guardy and pos[0] < guardx, wallPositions)]
  if len(wallsToLeft) == 0:
    return None
  return sorted(wallsToLeft, key=lambda pos:pos[0], reverse=True)[0]

def searchWallUp():
  guardx, guardy = guardPos
  wallsUp = [w for w in filter(lambda pos: pos[1] < guardy and pos[0] == guardx, wallPositions)]
  if len(wallsUp) == 0:
    return None
  return sorted(wallsUp, key=lambda pos:pos[1], reverse=True)[0]

def searchWallDown():
  guardx, guardy = guardPos
  wallsDown = [w for w in filter(lambda pos: pos[1] > guardy and pos[0] == guardx, wallPositions)]
  if len(wallsDown) == 0:
    return None
  return sorted(wallsDown, key=lambda pos:pos[1])[0]

def getNextWall():
  dirToSearchFunc = {
    (0, -1): searchWallUp,
    (0, 1): searchWallDown,
    (1, 0): searchWallRight,
    (-1, 0): searchWallLeft
  }
  return dirToSearchFunc[guardDir]()

def getCoordsBetween(stopPos):
  coords = []
  curr = guardPos
  while curr != stopPos:
    coords.append(curr)
    curr = (curr[0] + guardDir[0], curr[1] + guardDir[1])
  return coords

blockPositions = set()

nextWall = getNextWall()
while nextWall:
  between = getCoordsBetween(nextWall)
  uniqueCoords = uniqueCoords.union(between)
  uniqueCoordsWithDir = uniqueCoordsWithDir.union([(pos, guardDir) for pos in between])
  guardPos = between[-1]
  guardDir = nextDir[guardDir]
  nextWall = getNextWall()

# once no next wall - finish out the coords
curr = guardPos
while curr[0] >= 0 and curr[0] <= xMax and curr[1] >= 0 and curr[1] <= yMax:
  dirx, diry = guardDir
  uniqueCoords.add(curr)
  curr = (curr[0] + guardDir[0], curr[1] + guardDir[1])

print(len(uniqueCoords))

for prevPos in uniqueCoords:
  wallPositions.append(prevPos)
  guardPos = initGuardPos
  guardDir = initGuardDir

  nextWall = getNextWall()
  seenWallsWithDir = set()
  while nextWall and (nextWall, guardDir) not in seenWallsWithDir:
    seenWallsWithDir.add((nextWall, guardDir))
    between = getCoordsBetween(nextWall)
    guardPos = between[-1]
    guardDir = nextDir[guardDir]
    nextWall = getNextWall()
    
  if nextWall:
    blockPositions.add(prevPos)

  wallPositions.remove(prevPos)

print(len(blockPositions))