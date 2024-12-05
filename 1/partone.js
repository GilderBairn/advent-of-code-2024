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

let zipped = list1.map((element, idx) => {
  // console.log(`el: ${element}, idx: ${idx}, pair: ${list2[idx]}`)
  return [element, list2[idx]]
})

let deltas = 0
for (let pair of zipped) {
  deltas += Math.abs(pair[0] - pair[1])
}

console.log(deltas)