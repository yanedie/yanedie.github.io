const bills = [125, 555, 44];
// const tips = [];
// const total = [];

const calcTip = (bill) =>
    bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2;

// bills.forEach((bill) => {
//     const tip = calcTip(bill);
//     tips.push(tip);
//     const sum = bill + tip;
//     total.push(sum);
// });

const tips = bills.map(calcTip);
const total = bills.map((bill, index) => bill + tips[index]);

console.log(bills, tips, total);
