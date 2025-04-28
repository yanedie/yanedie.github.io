let markMass = 78;
let markHeight = 1.69;
let johnMass = 92;
let johnHeight = 1.95;

let markBMI = markMass / (markHeight * markHeight);
let johnBMI = johnMass / (johnHeight * johnHeight);
let markHigherBMI = markBMI > johnBMI;

console.log("Mark's BMI:", markBMI);
console.log("John's BMI:", johnBMI);
markHigherBMI
  ? console.log(`Mark's BMI (${markBMI}) is higher than John's (${johnBMI})!`)
  : console.log(`John's BMI (${johnBMI}) is higher than Mark's (${markBMI})!`);

markMass = 95;
markHeight = 1.88;
johnMass = 85;
johnHeight = 1.76;

markBMI = markMass / (markHeight * markHeight);
johnBMI = johnMass / (johnHeight * johnHeight);

markHigherBMI = markBMI > johnBMI;

console.log("Mark's BMI:", markBMI);
console.log("John's BMI:", johnBMI);
markHigherBMI
  ? console.log(`Mark's BMI (${markBMI}) is higher than John's (${johnBMI})!`)
  : console.log(`John's BMI (${johnBMI}) is higher than Mark's (${markBMI})!`);
