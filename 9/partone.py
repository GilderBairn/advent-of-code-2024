def useExampleInputs():
  return """2333133121414131402"""

def parseInputText():
  result = ""
  with open('input.txt', 'r') as fp:
    result = fp.read()
  return result

# rawInput = useExampleInputs()
rawInput = parseInputText()
rawInput = rawInput.strip()

def printDisk(data):
  result = ""
  for block in data:
    if block == ".":
      result += "."
    else:
      result += hex(block)[2:]
  return result

def getCheckSum(data):
  result = 0
  pos = 0
  for block in data:
    if block != ".":
      result += block * pos
    pos += 1
  return result
    

curID = 0
isFree = False
disk = []
for size in rawInput:
  if isFree:
    disk += ["." for _ in range(int(size))]
  else:
    disk += [curID for _ in range(int(size))]
    curID += 1
  isFree = not isFree

print(f"disk:\t{printDisk(disk)}")

freePtr = 0
swapPtr = len(disk)-1

# move pointers to init position
while disk[freePtr] != ".":
  freePtr += 1
while disk[swapPtr] == ".":
  swapPtr -= 1

while swapPtr > freePtr:
  disk[freePtr] = disk[swapPtr]
  disk[swapPtr] = "."
  while disk[freePtr] != ".":
    freePtr += 1
  while disk[swapPtr] == ".":
    swapPtr -= 1

print(f"defrag:\t{printDisk(disk)}")
print(f"checksum: {getCheckSum(disk)}")