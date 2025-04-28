'use strict';
const poll = {
  question: 'What is your favourite programming lanaguge?',
  options: ['0: Javascript', '1, Python', '2: Rust', '3: C++'],
  answers: new Array(4).fill(0),
  registerNewAnswer() {
    const answer = Number(
      prompt(
        `${this.question}\n${this.options.join('\n')}\nWrite option number`
      )
    );
    typeof answer === 'number' &&
      answer < this.answers.length &&
      this.answers[answer]++;
    this.displayResults();
    this.displayResults('string');
  },
  displayResults(type = 'array') {
    type === 'array' && console.log(this.answers);
    type === 'string' &&
      console.log(`Poll results are ${this.answers.join(', ')}`);
  },
};

document
  .querySelector('.poll')
  .addEventListener('click', poll.registerNewAnswer.bind(poll));

// BONUS
// { } 就等于 new 了一个对象，call 把 this 指向了这个对象。
const data1 = [5, 2, 3];
const data2 = [1, 5, 3, 9, 6, 1];
poll.displayResults.call({ answers: [5, 2, 3] }, 'string');
poll.displayResults.call({ answers: [1, 5, 3, 9, 6, 1] }, 'array');
poll.displayResults.call({ answers: [1, 5, 3, 9, 6, 1] });

/* const greet = (greeting) => (name) => console.log(`${greeting}, ${name}`)
greet('Hey')('Chen Jinyi')

const addTaxRate = function (rate) {
  return function (value) {
    // 记得还要再 return，否则默认返回 undefined
    return value + value * rate
  }
}

const addVAT = addTaxRate(0.23)
addVAT(200) */