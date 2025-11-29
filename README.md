# React-to-Angular Transpiler – Cyncly Candidate Task

## Problem Understanding

The goal of this assignment is to write a Python script that reads a simple React functional component (`react/TodoList.jsx`) and generates an equivalent Angular component:

- `TodoList.component.ts` (TypeScript class)
- `TodoList.component.html` (Angular template)

The focus is on mapping JSX and React state to Angular template syntax and bindings, not on building a fully generic transpiler.

## Scope and Assumptions

For this task I only handle a specific pattern:

- A single functional component using `useState`
- JSX with:
  - A title (`<h1>`)
  - A list of todos rendered with `todos.map(...)`
  - A text `<input>` controlled by `value` and `onChange`
  - A `<button>` with an `onClick` handler
- The initial todos are defined inline in the first `useState([...])` call.

## High-Level Approach

1. **Read the React file**  
   Use Python to read `react/TodoList.jsx` into a string.

2. **Extract important data from the React code**  
   - Use a simple regex to find the initial todos array from `useState([...])`.
   - Use that list to initialize `todos` in the Angular component.
   - For this assignment, I do not fully parse JSX. Instead, I generate a fixed Angular template that matches the structure of `TodoList.jsx`.

3. **Generate Angular HTML template**  
   - Create a string containing an Angular template that:
     - Uses `*ngFor="let todo of todos"` for the list.
     - Uses `[(ngModel)]="newTodo"` for two-way binding of the input.
     - Uses `(click)="addTodo()"` for the button.

4. **Generate Angular TypeScript component**  
   - Create a string for `TodoListComponent` that:
     - Imports `Component` from `@angular/core`.
     - Declares `todos: string[]` initialized from the parsed React state.
     - Declares `newTodo: string` and an `addTodo()` method similar to the React logic.

5. **Write output files**  
   - Write the generated TypeScript to `generated/TodoList.component.ts`.
   - Write the generated HTML to `generated/TodoList.component.html`.

## Limitations

- Only supports the provided `TodoList.jsx` structure (or very similar components).
- Does not handle:
  - Props
  - Nested components
  - Conditional rendering
  - Complex hooks beyond `useState`.

## Ideas for Level 2 / Future Improvements

- Support multiple `useState` hooks and map them all to Angular fields.
- Add basic support for props and passing values between components.
- Replace regex-based parsing with a real JSX/AST parser.
- Add tests that verify the generated Angular code matches expected output.
