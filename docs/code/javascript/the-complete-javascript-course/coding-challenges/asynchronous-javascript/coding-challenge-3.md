# Coding Challenge #3

## Your tasks

### PART 1

1. Write an async function 'loadNPause' that recreates Challenge #2, this time using async/await (only the part where the promise is consumed, reuse the 'createImage' function from before)
2. Compare the two versions, think about the big differences, and see which one you like more
3. Don't forget to test the error handler, and to set the network speed to “Fast 3G” in the dev tools Network tab

### PART 2

4. Create an async function 'loadAll' that receives an array of image paths 'imgArr'
5. Use `.map` to loop over the array, to load all the images with the 'createImage' function (call the resulting array 'imgs')
6. Check out the 'imgs' array in the console! Is it like you expected?
7. Use a promise combinator function to actually get the images from the array 😉
8. Add the 'parallel' class to all the images (it has some CSS styles)

## Test data Part 2

`['img/img-1.jpg', 'img/img-2.jpg', 'img/img-3.jpg']`. To test, turn off the 'loadNPause' function

**GOOD LUCK 😀**

---

```javascript
--8<-- "docs/code/javascript/the-complete-javascript-course/coding-challenges/asynchronous-javascript/challenge-3.js"
```
