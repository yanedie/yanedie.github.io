const data = [
  {
    dolphins: [44, 23, 71],
    koalas: [64, 54, 49],
  },
  {
    dolphins: [85, 54, 41],
    koalas: [23, 34, 27],
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

const checkWinner = (avg1, avg2) => {
  const winner =
    avg1 >= 2 * avg2
      ? `Dolphins win 🏆 (${avg1} vs. ${avg2})`
      : avg2 >= avg1
      ? `Koalas win 🏆 (${avg1} vs. ${avg2})`
      : "No one wins";

  console.log(winner);
};

data.forEach((scores, index) => {
  console.log(`\nCompetition ${index + 1}`);
  const avgDolhins = calcAvgScore(scores.dolphins);
  const avgKoalas = calcAvgScore(scores.koalas);
  checkWinner(avgDolhins, avgKoalas);
});
