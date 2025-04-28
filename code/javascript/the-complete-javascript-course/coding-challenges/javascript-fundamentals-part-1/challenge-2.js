testData1 = {
  mark: {
    weight: 78,
    height: 1.69,
  },
  john: {
    weight: 92,
    height: 1.95,
  },
};

testData2 = {
  mark: {
    weight: 95,
    height: 1.88,
  },
  john: {
    weight: 85,
    height: 1.76,
  },
};

const getBMI = (people) => {
  const { weight, height } = people;
  const bmi = weight / (height * height);
  return bmi.toFixed(2);
};

const markBMI = getBMI(testData1.mark);
const johnBMI = getBMI(testData1.john);

const markHigherBMI = markBMI > johnBMI ? true : false;

markHigherBMI
  ? console.log(`Mark's BMI (${markBMI}) is higher than John's (${johnBMI})!`)
  : console.log(`John's BMI (${johnBMI}) is higher than Mark's (${markBMI})!`);
