'use strict';
let guessNum = Math.trunc(Math.random() * 20 + 1);
// document.querySelector('.number').textContent = guessNum;
let score = 20;
let highscore = 0;

const checkBtn = document.querySelector('.btn.check');

const displayMessage = message => {
  document.querySelector('.message').textContent = message;
};

checkBtn.addEventListener('click', () => {
  let myNum = Number(document.querySelector('.guess').value);
  !myNum && displayMessage('⛔️ No number!');

  // 答对的情况
  if (myNum === guessNum) {
    displayMessage('🎉 Correct Number!');

    document.querySelector('.number').textContent = guessNum;
    document.querySelector('body').style.backgroundColor = '#60b347';
    document.querySelector('.number').style.width = '30rem';

    // 如果超过了最高纪录，刷新
    if (score > highscore) {
      highscore = score;
      document.querySelector('.highscore').textContent = highscore;
    }
    // 答错的情况
  } else if (myNum !== guessNum) {
    // 确保在次数范围内
    if (score >= 1) {
      displayMessage(myNum > guessNum ? '📈 Too high!' : '📉 Too low!');
      score--;
      document.querySelector('.score').textContent = score;
    }
    if (score === 0) {
      displayMessage('💥 You lost the game!')
    }
  }
});

document.querySelector('.btn.again').addEventListener('click', () => {
  document.querySelector('body').style.backgroundColor = '#222';
  document.querySelector('.number').style.width = '15rem';
  document.querySelector('.number').textContent = '?';
  document.querySelector('.guess').value = '';

  score = 20
  document.querySelector('.score').textContent = score;

  guessNum = Math.trunc(Math.random() * 20 + 1);
  // document.querySelector('.number').textContent = guessNum;
  displayMessage('Start guessing...')
})
