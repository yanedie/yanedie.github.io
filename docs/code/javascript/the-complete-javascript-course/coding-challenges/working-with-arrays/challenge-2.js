const calcAverageHumanAge = function (dogAges) {
  const humanAges = dogAges.map((dogAge) =>
    dogAge <= 2 ? 2 * dogAge : 16 + dogAge * 4
  );
  const adults = humanAges.filter((age) => age >= 18);
  const averageHumanAge =
    adults.reduce((acc, age) => acc + age, 0) / adults.length;
  return averageHumanAge;
};

const data1 = [5, 2, 4, 1, 15, 8, 3];
const data2 = [16, 6, 10, 5, 6, 1, 4];

console.log(calcAverageHumanAge(data1));
console.log(calcAverageHumanAge(data2));
