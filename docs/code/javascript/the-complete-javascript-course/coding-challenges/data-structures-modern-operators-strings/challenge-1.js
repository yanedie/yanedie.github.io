// 1. Create one player array for each team (variables 'players1' and 'players2')
// const players1 = game.players[0]
// const players2 = game.players[1]
const [players1, players2] = game.players

// 2. The first player in any player array is the goalkeeper and the others are field players.
// For Bayern Munich (team 1) create one variable ('gk') with the goalkeeper's name, and one array ('fieldPlayers') with all the remaining 10 field players
const [gk, ...fieldPlayers] = players1

// 3. Create an array 'allPlayers' containing all players of both teams (22 players)
// const allPlayers = players1.concat(players2)
const allPlayers = [...players1, ...players2]

// 4. During the game, Bayern Munich (team 1) used 3 substitute players. So create a new array ('players1Final') containing all the original team1 players plus 'Thiago', 'Coutinho' and 'Perisic'
const players1Final = [...players1, 'Thiago', 'Coutinho', 'Perisic']

// 5. Based on the game.odds object, create one variable for each odd (called 'team1', 'draw' and 'team2')
// const {team1, draw, team2} = odds
const { odds: {team1, x: draw, team2 } } = game

// 6. Write a function ('printGoals') that receives an arbitrary number of player names (NOT an array) and prints each of them to the console, along with the number of goals that were scored in total (number of player names passed in)
const printGoals = function (...players) {
  console.log(players)
  console.log(`${players.length} goals were scored`)
}
printGoals('Davies', 'Muller', 'Lewandowski', 'Kimmich')
printGoals(...game.scored)

// 7. The team with the lower odd is more likely to win. Print to the console which team is more likely to win, WITHOUT using an if/else statement or the ternary operator.
team1 > team2 && console.log('Team 1 is more likely to win')
team1 < team2 && console.log('Team 2 is more likely to win')