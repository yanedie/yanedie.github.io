# Coding Challenge #3

## Your tasks

1. Use a constructor function to implement an Electric Car (called 'EV') as a child "class" of 'Car'. Besides a make and current speed, the 'EV' also has the current battery charge in % ('charge' property)
2. Implement a 'chargeBattery' method which takes an argument 'chargeTo' and sets the battery charge to 'chargeTo'
3. Implement an 'accelerate' method that will increase the car's speed by 20, and decrease the charge by 1%. Then log a message like this: 'Tesla going at 140 km/h, with a charge of 22%'
4. Create an electric car object and experiment with calling 'accelerate', 'brake' and 'chargeBattery' (charge to 90%). Notice what happens when you 'accelerate'! **Hint**: Review the definition of polymorphism 😉

## Test data

* **Data car 1:** 'Tesla' going at 120 km/h, with a charge of 23%

**GOOD LUCK 😀**

---

```javascript
--8<-- "docs/code/javascript/the-complete-javascript-course/coding-challenges/object-oriented-programming-oop/challenge-3.js"
```
