---
created: 2024-07-11T00:02
updated: 2024-07-11T00:55
---
## Setting Up the Project

1. `npm create vite @4.1.0`
	- Name: game-hub
	- Library: React
	- Language: Typescript
2. `cd game-hub`
3. `npm i`
4. `npm run dev`
5. `code .`
6. `git init`
7. `git add .`
8. `git commit -m "Initial commit"`

## Installing Chakra UI

<v2.chara-ui.com>

To use Chakra UI in your project, run the following commands in your terminal:

`npm i @chakra-ui/react @emotion/react @emotion/styled framer-motion`

After installing Chakra UI, you need to set up the `ChakraProvider` at the root of your application. This can be either in your `index.jsx`, `index.tsx` or `App.jsx` depending on the framework you use.

``` tsx title="main.tsx"
import React from 'react'
import ReactDOM from 'react-dom/client'
import { ChakraProvider } from '@chakra-ui/react'
import App from './App'
import './index.css'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <ChakraProvider>
      <App />
    </ChakraProvider>
  </React.StrictMode>
)
```

``` tsx title="App.tsx"
import { Button, ButtonGroup } from '@chakra-ui/react'

function App() {
  return <Button colorScheme='blue'>Button</Button>
}

export default App
```

## Building a Responsive Layout

- Base: mobile
- Lg: >= 1024 px

``` tsx title="App.tsx"
import { Grid, GridItem, Show } from "@chakra-ui/react";

function App() {
  return (
    <Grid
      templateAreas={{
        base: `"nav" "main"`,
        lg: `"nav nav" "aside main"`,
      }}
    >
      <GridItem area="nav" bg="coral">
        Nav
      </GridItem>
      <Show above="lg">
        <GridItem area="aside" bg="gold">
          Aside
        </GridItem>
      </Show>
      <GridItem area="main" bg="dodgerblue">
        Main
      </GridItem>
    </Grid>
  );
}

export default App;
```