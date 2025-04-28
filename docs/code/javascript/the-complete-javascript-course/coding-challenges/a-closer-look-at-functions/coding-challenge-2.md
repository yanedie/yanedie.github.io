# Coding Challenge #2

This is more of a thinking challenge than a coding challenge 🤓

## Your tasks

1. Take the IIFE below and at the end of the function, attach an event listener that changes the color of the selected h1 element ('header') to blue, each time the body element is clicked. Do not select the h1 element again!
2. And now explain to yourself (or someone around you) why this worked! Take all the time you need. Think about when exactly the callback function is executed, and what that means for the variables involved in this example.

## Starter Code

```javascript
(function () {
  const header = document.querySelector('h1');
  header.style.color = 'red';
})();
```

**GOOD LUCK 😀**

---

这段代码使用了一个立即执行函数表达式 (IIFE)。IIFE 创建了一个新的作用域，在这个作用域里，`header` 变量被定义并指向文档中的 `h1` 元素。

代码首先将 `h1` 元素的颜色设置成红色。然后，它给 `body` 元素添加了一个点击事件监听器。这个监听器会在每次 `body` 元素被点击时执行一个回调函数。

回调函数的作用是将 `header` 元素的颜色设置成蓝色。因为 `header` 变量是在 IIFE 的作用域中定义的，即使回调函数是在 `body` 元素的作用域中执行，它仍然可以访问和修改 `header` 变量。

重点是：

1. **IIFE 创建了一个闭包。** `header` 变量在 IIFE 内部定义，回调函数也在 IIFE 内部定义，所以回调函数可以“记住”并访问 `header` 变量，即使 IIFE 已经执行完了。
2. **事件监听器回调函数的执行时机。** 回调函数只有在 `body` 被点击的时候 *才* 执行。当它执行的时候，仍然可以访问到 IIFE 创建的闭包里面的 `header` 变量。

因此，每次点击 `body`，回调函数都会执行，并将 `header` 元素的颜色设置为蓝色。因为 `header` 变量只选择了一次 (在 IIFE 内部)，所以避免了每次点击都重新选择 `h1` 元素。
