const data = [
  {
    dolphins: [96, 108, 89],
    koalas: [88, 91, 110],
  },
  {
    dolphins: [97, 112, 101],
    koalas: [109, 95, 123],
  },
  {
    dolphins: [97, 112, 101],
    koalas: [109, 95, 106],
  },
];

const calcAvgScore = (scores) => {
  const initialValue = 0;
  sum = scores.reduce(
    (accmulator, currentValue) => accmulator + currentValue,
    initialValue
  );
  avgScore = sum / scores.length;
  return avgScore.toFixed(2);
};

for (let i = 0; i < data.length; i++) {
  console.log(`\nCompetition ${i + 1}:`);

  const dol = calcAvgScore(data[i].dolphins);
  const koa = calcAvgScore(data[i].koalas);

  const rule = dol >= 100 && koa >= 100;

  if (dol !== koa && rule) {
    const winner = dol > koa ? "Dolphins" : "Koalas";
    console.log(
      `${winner} wins with an average score of ${
        winner === "Dolphins" ? dol : koa
      }! Congratulations!`
    );
  } else if (dol === koa && rule) {
    console.log("It's a draw!");
  } else {
    console.log("No one wins the trophy!");
  }
}
