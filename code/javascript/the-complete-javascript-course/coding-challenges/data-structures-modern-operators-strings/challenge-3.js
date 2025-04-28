// 1. Create an array 'events' of the different game events that happened (no duplicates)
const events = [...new Set(gameEvents.values())]
console.log(events)

// 2. After the game has finished, is was found that the yellow card from minute 64 was unfair. So remove this event from the game events log.
gameEvents.delete(64)
console.log(gameEvents)

// 3. Print the following string to the console: "An event happened, on average, every 9 minutes" (keep in mind that a game has 90 minutes)
console.log(`An event happened, on average, every ${90/gameEvents.size} minutes`)

// pop() 方法从数组中删除最后一个元素，并返回该元素的值。
const time = [...gameEvents.keys()].pop();
// expected output: 92
console.log(time);
console.log(
  `An event happened, on average, every ${time / gameEvents.size} minutes`
);

/* 4. Loop over the events and log them to the console, marking whether it's in the first half or second half (after 45 min) of the game, like this:
      [FIRST HALF] 17: ⚽️ GOAL */
for (const [time, event] of gameEvents) {
  const half = time <= 45 ? 'FIRST' : 'SECOND';
  console.log(`[${half} HALF] ${time}: ${event}`)
}

// Padding
const message = 'Go to gate 23!';
console.log(message.padStart(20, '+').padEnd(30, '+'));
console.log('Jonas'.padStart(20, '+').padEnd(30, '+'));

const maskCreditCard = function (number) {
  const str = number + '';
  const last = str.slice(-4);
  return last.padStart(str.length, '*');
};

console.log(maskCreditCard(64637836));
console.log(maskCreditCard(43378463864647384));
console.log(maskCreditCard('334859493847755774747'))