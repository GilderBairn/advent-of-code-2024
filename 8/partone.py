from itertools import permutations

def useExampleInputs():
  return """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def parseInputText():
  result = ""
  with open('input.txt', 'r') as fp:
    result = fp.read()
  return result

# rawInput = useExampleInputs()
rawInput = parseInputText()

inputLines = rawInput.strip().split("\n")
yMax = len(inputLines)
xMax = len(inputLines[0].strip())

nodes = {}

# init list of nodes
cury = 0
for line in inputLines:
  curx = 0
  for char in line:
    if char != ".":
      if nodes.get(char):
        nodes[char].append((curx, cury))
      else:
        nodes[char] = [(curx, cury)]
    curx += 1
  cury += 1

antinodes = set()
yRange = range(yMax)
xRange = range(xMax)
for freq in nodes:
  locations = nodes[freq]
  pairs = permutations(locations,2)
  for a, b in pairs:
    rise = b[1] - a[1]
    run = b[0] - a[0]
    # project out antinode for checking
    antinode = (b[0]+run, b[1]+rise)
    if antinode[0] in xRange and antinode[1] in yRange:
      antinodes.add(antinode)

print(len(antinodes))
