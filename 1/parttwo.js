function useExampleInputs() {
  return [
    [3,4,2,1,3,3],
    [4,3,5,3,9,3],
  ]
}

async function parseInputText() {
  let list1 = []
  let list2 = []

  const text = await Deno.readTextFile('input.txt')
  const lines = text.split('\r\n')
  for (let line of lines) {
    if (line) {
      let values = line.split('   ')
      list1.push(Number(values[0]))
      list2.push(Number(values[1]))
    }
  }

  return [list1, list2]
}

let list1, list2
// [list1, list2] = useExampleInputs()
[list1, list2] = await parseInputText()

list1.sort((a, b) => {return a - b})
list2.sort((a, b) => {return a - b})

let counts = {}
for (let value of list2) {
  if (counts[value]) {
    counts[value]++
  } else {
    counts[value] = 1
  }
}

let similarity = 0
for (let value of list1) {
  let count = counts[value] || 0
  similarity += value * count
}

console.log(similarity)