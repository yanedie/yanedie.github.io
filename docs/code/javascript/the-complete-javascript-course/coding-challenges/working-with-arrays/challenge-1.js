const checkDogs = function (dogsJulia, dogsKate) {
  const correctDogsJulia = [...dogsJulia].slice(1,-2)
  const data = [...correctDogsJulia, ...dogsKate]
  data.forEach((d, i) => {
    d >= 3 && console.log(`Dog number ${i+1} is an adult, and is ${d} years old`)
    d < 3 && console.log(`Dog number ${i+1} is still a puppy`)
  })
}

checkDogs([3, 5, 2, 12, 7],[4, 1, 15, 8, 3])

// 区分了 slice 和 splice，slice 不改变原数组，splice 在原数组上改变
// slice(start, end) 是提取。包括 start，但不包括 end，左闭右开。