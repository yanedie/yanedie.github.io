// 1.	Loop over the 'dogs' array containing dog objects, and for each dog, calculate the recommended food portion and add it to the object as a new property. Do not create a new array, simply loop over the array. Forumla: recommendedFood = weight ** 0.75 * 28. (The result is in grams of food, and the weight needs to be in kg)

dogs.forEach((dog) => {
  dog.recommendedFood = Math.trunc(dog.weight ** 0.75 * 28);
});

// 2.	Find Sarah's dog and log to the console whether it's eating too much or too little. Hint: Some dogs have multiple owners, so you first need to find Sarah in the owners array, and so this one is a bit tricky (on purpose)

// const sarahsDog = dogs.filter((dog) => dog.owners.includes("Sarah"));
const sarahsDog = dogs.find((dog) => dog.owners.includes("Sarah"));
console.log(
  `Sarah's dog is eating ${
    sarahsDog.curFood > sarahsDog.recommendedFood ? "much" : "little"
  }`
);

// filter 返回一个新数组，包含所有满足条件的元素。（可以返回零个或多个元素）
// find 返回第一个满足条件的元素。（只返回第一个符合条件的元素，都不符合就返回 undefined）

// 3.	Create an array containing all owners of dogs who eat too much ('ownersEatTooMuch') and an array with all owners of dogs who eat too little ('ownersEatTooLittle').

const ownersEatTooMuch = dogs
  .filter((dog) => dog.curFood > dog.recommendedFood)
  .map((dog) => dog.owners)
  .flat();

const ownersEatTooLittle = dogs
  .filter(({ curFood, recommendedFood }) => curFood < recommendedFood)
  .flatMap(({ owners }) => owners);

console.log(ownersEatTooMuch);
console.log(ownersEatTooLittle);

// 链式调用 map 和 fiat，可以直接用 flatMap

// 4.	Log a string to the console for each array created in 3., like this: "Matilda and Alice and Bob's dogs eat too much!" and "Sarah and John and Michael's dogs eat too little!"

console.log(`${ownersEatTooMuch.join(" and ")}'s dogs eat too much!`);
console.log(`${ownersEatTooLittle.join(" and ")}'s dogs eat too little!`);

// 5.	Log to the console whether there is any dog eating exactly the amount of food that is recommended (just true or false)
// console.log(
//   `${dogs.find((dog) => dog.curFood === dog.recommendedFood) ? true : false}`
// );
console.log(dogs.some((dog) => dog.curFood === dog.recommendedFood));

// 6.	Log to the console whether there is any dog eating an okay amount of food (just true or false)
console.log(
  dogs.some(
    (dog) =>
      dog.curFood > dog.recommendedFood * 0.9 &&
      dog.curFood < dog.recommendedFood * 1.1
  )
);

// some 返回布尔值

// 7.	Create an array containing the dogs that are eating an okay amount of food (try to reuse the condition used in 6.)
console.log(
  dogs.filter(
    (dog) =>
      dog.curFood > dog.recommendedFood * 0.9 &&
      dog.curFood < dog.recommendedFood * 1.1
  )
);

// 8.	Create a shallow copy of the 'dogs' array and sort it by recommended food portion in an ascending order (keep in mind that the portions are inside the array's objects)
const dogsCopy = dogs
  .slice()
  .sort((a, b) => a.recommendedFood - b.recommendedFood);
console.log(dogsCopy);

// 浅拷贝直接用 slice()，sort() 升序一般都是用 a,b => a-b
