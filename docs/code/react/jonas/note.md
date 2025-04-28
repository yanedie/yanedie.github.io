---
created: 2024-03-01T12:18
updated: 2024-09-16T22:58
---

# Jonas React Course Note

## Building our first React App

```javascript title="First React App"
import { useEffect, useState } from "react";

export default function App() {
  const [advice, setAdvice] = useState("");
  const [count, setCount] = useState(0);

  async function getAdvice() {
    const res = await fetch("https://api.adviceslip.com/advice");
    const data = await res.json();
    setAdvice(data.slip.advice);
    setCount((count) => count + 1);
  }

  useEffect(function () {
    getAdvice();
  }, []);

  return (
    <div>
      <h1>{advice}</h1>
      <button onClick={getAdvice}>Get Device</button>
      <Message count={count} />
    </div>
  );
}

function Message(props) {
  return (
    <p>
      You have read <strong>{props.count}</strong> pieces of advice
    </p>
  );
}
```

## Challenge #1 Profile Card (v1)

```javascript title="index.js"
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";

function App() {
  return (
    <div className="card">
      <Avatar />
      <div className="data">
        <Intro />
        <SkillList />
      </div>
    </div>
  )
}

function Avatar(props) {
  return <img className="avatar" src="avatar.png" alt="avatar" />
}

function Intro() {
  return (
    <div>
      <h1>Ryan Chen</h1>
      <p>Full-stack web developer and teacher at Udemy. When not coding or preparing a course,I like to play board games,to cook (and eat)or to just enjoy the Portuguese sun at the beach.</p>
    </div>
  )
}

function SkillList() {
  return (
    <div className="skill-list">
      <Skill skill="HTML+CSS" emoji="💪" color="blue" />
      <Skill skill="JavaScript" emoji="💪" color="orange" />
      <Skill skill="Web Design" emoji="💪" color="yellow" />
    </div>
  )
}

function Skill(props) {
  return (
    <div className="skill" style={{ backgroundColor: props.color }}>
      <span>{props.skill}</span>
      <span>{props.emoji}</span>
    </div>
  )
}

const root = createRoot(document.getElementById('root'))

root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
```

![Profile Card V1](https://pub-35f8b3b9fb1540899fcf1e6fb1fab07b.r2.dev/profile-card-v1.png)

## 渲染列表

```
const pizzaData = {...}

function Menu() {
  return (
    <main className="menu">
      <h2>Our menu</h2>
      <ul>
        {pizzaData.map((pizza) => (
          <Pizza pizzaObj={pizza} />
        ))}
      </ul>
    </main>
  )
}
```

```
function Pizza(props) {
  return (
    <div className="pizza">
      <img src={props.pizzaObj.photoName} alt={props.pizzaObj.name} />
      <div>
        <h3>{props.pizzaObj.name}</h3>
        <p>{props.pizzaObj.ingredients}</p>
        <span>{props.pizzaObj.price}</span>
      </div>
    </div>
  )
}
```

## 条件渲染

### 逻辑与

!!! warning "注意"

    在使用逻辑与（&&）渲染列表时，如果列表为空，应该判断列表长度是否大于0，而非判断列表长度本身，否则，页面上将出现0，这是由逻辑与运算符决定的。

``` hl_lines="7"
const pizzas = pizzaData
const pizzasNum = pizzas.length

return (
  <main className="menu">
    <h2>Our menu</h2>
    {pizzasNum > 0 && (
      <ul className="pizzas">
        {pizzas.map((pizza) => (
          <Pizza pizzaObj={pizza} key={pizza.name} />
        ))}
      </ul>
    )}
  </main>
)
```

### 三目运算符

比较推荐这种方式。因为可以有候选。

```
  return (
    <main className="menu">
      <h2>Our menu</h2>
      {pizzasNum > 0 ? (
        <ul className="pizzas">
          {pizzas.map((pizza) => (
            <Pizza pizzaObj={pizza} key={pizza.name} />
          ))}
        </ul>) : (<p>We're still working on our menu. Please come back later :)</p>)
      }
    </main>
  )
```

### Returns

```hl_lines="2"

function Pizza({ pizzaObj }) {
  if (pizzaObj.soldOut) return null

  return (
    <li className={`pizza ${pizzaObj.soldOut ? "sold-out" : ""}`}>
      <img src={pizzaObj.photoName} alt={pizzaObj.name} />
      <div>
        <h3>{pizzaObj.name}</h3>
        <p>{pizzaObj.ingredients}</p>
        <span>{pizzaObj.soldOut ? "Sold out" : pizzaObj.price}</span>
      </div>
    </li>
  )
}
```

## 解构

``` hl_lines="5 11 15 17 18"
function Menu() {
  ...
  <ul className="pizzas">
    {pizzas.map((pizza) => (
      <Pizza pizzaObj={pizza} key={pizza.name} />
    ))}
  </ul>
 ...
}

function Pizza({ pizzaObj }) {
  ...
  return (
    <li className={`pizza ${pizzaObj.soldOut ? "sold-out" : ""}`}>
      <img src={pizzaObj.photoName} alt={pizzaObj.name} />
      <div>
        <h3>{pizzaObj.name}</h3>
        <p>{pizzaObj.ingredients}</p>
        <span>{pizzaObj.soldOut ? "Sold out" : pizzaObj.price}</span>
      </div>
    </li>
  )
}

function Footer() {
  const hour = new Date().getHours();
  const openHour = 8;
  const closeHour = 22;
  const isOpen = hour >= openHour && hour <= closeHour

  return (
    <footer className="footer">
      {isOpen ? <Order openHour={openHour} closeHour={closeHour} /> : (<p>We're happy to welcome you between {openHour}:00 and {closeHour}:00.</p>)}
    </footer >
  )
}

function Order({ openHour, closeHour }) {
  return (
    <div className="order">
      <p>
        We're open from {openHour}:00 to {closeHour}:00. Come visit us or order online.
      </p>
      <button className="btn">Order</button>
    </div>
  )
}
```
