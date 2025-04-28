class Person {
  constructor(fullName, mass, height) {
      this.fullName = fullName;
      this.mass = mass;
      this.height = height;
  }
  calcBMI() {
      this.BMI = this.mass / this.height ** 2;
      return this.BMI;
  }
}

const mark = new Person('Mark Miller', 78, 1.69);
const john = new Person('John Smith', 92, 1.95);

mark.calcBMI() > john.calcBMI()
  ? console.log(
        `${mark.fullName}'s BMI (${mark.BMI}) is higher than ${john.fullName}'s (${john.BMI})!`
    )
  : console.log(
        `${john.fullName}'s BMI (${john.BMI}) is higher than ${mark.fullName}'s (${mark.BMI})!`
    );
