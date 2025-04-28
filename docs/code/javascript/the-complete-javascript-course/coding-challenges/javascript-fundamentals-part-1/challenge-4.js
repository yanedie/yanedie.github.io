const bill = [275, 40, 430];
const calTip = (bill) => {
  const percent = bill >= 50 && bill <= 300 ? 15 : 20;
  const tip = bill * (percent / 100);
  return tip;
};

for (let i = 0; i < bill.length; i++) {
  const tip = calTip(bill[i]);
  console.log(
    `The bill was ${bill[i]}, the tip was ${tip}, and the total value ${
      bill[i] + tip
    }`
  );
}
