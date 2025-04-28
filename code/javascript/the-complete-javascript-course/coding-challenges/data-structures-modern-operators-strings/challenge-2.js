// 1. Loop over the game.scored array and print each player name to the console, along with the goal number (Example: "Goal 1: Lewandowski")
// game.scored.forEach((player, idx) => {
//   console.log(`Goal ${idx + 1}: ${player}`)
// });
// Object.entries() 相当于 Python 的 foo.items()
for (const [i, player] of Object.entries(game.scored)) {
  console.log(`Goal ${i}: ${player}`)
}
// 2. Use a loop to calculate the average odd and log it to the console (We already studied how to calculate averages, you can go check if you don't remember)
// Object.values 会返回一个数组
const odds = Object.values(game.odds)
let  avg = 0
for (const odd in odds) avg += odd
avg /= odds.length
console.log(avg)

/* 3. Print the 3 odds to the console, but in a nice formatted way, exaclty like this:
      Odd of victory Bayern Munich: 1.33
      Odd of draw: 3.25
      Odd of victory Borrussia Dortmund: 6.5
Get the team names directly from the game object, don't hardcode them (except for "draw"). HINT: Note how the odds and the game objects have the same property names 😉 */
for (const [team, odd] of Object.entries(game.odds)) {
  const teamStr = team === 'x' ? "draw" : `victory ${game[team]}`;
  console.log(`Odd of ${teamStr}: ${odd}`)
}

/* BONUS: Create an object called 'scorers' which contains the names of the players who scored as properties, and the number of goals as the value. In this game, it will look like this:
      {
        Gnarby: 1,
        Hummels: 1,
        Lewandowski: 2
      }
*/
const scorers = {};
for (const player of game.scored) {
  scorers[player] ? scorers[player]++ : (scorers[player] = 1);
}
console.log(scorers)

const result = game.scored.reduce((accumulator, player) => {
  if (accumulator[player]) {
    accumulator[player]++
    return accumulator
  }  else {
    accumulator[player] = 1
    return accumulator
  }
  }, {})
console.log(result);