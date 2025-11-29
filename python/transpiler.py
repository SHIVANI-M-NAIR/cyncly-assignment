"""
React-to-Angular transpiler.

Planned steps:
1. Read the React component file (TodoList.jsx).
2. Extract the initial todos array from the useState call.
3. Generate an Angular TypeScript component (TodoList.component.ts) string.
4. Generate an Angular HTML template (TodoList.component.html) string.
5. Write both strings into a 'generated/' folder.
"""

import re
from pathlib import Path

react_file = '../react/TodoList.jsx'   # adjusts path since script is inside python/

# Step 1: Read React file
with open(react_file, 'r', encoding='utf-8') as f:
    react_code = f.read()


def extract_initial_todos(react_code: str):
    """
    Extracts the initial todos array from the first useState([...]) pattern.

    Example to match:
    const [todos, setTodos] = useState(['Learn React', 'Build a transpiler']);

    Returns a Python list: ['Learn React', 'Build a transpiler']
    """
    match = re.search(r"useState\(\s*(\[[^\]]*\])\s*\)", react_code)
    if not match:
        return []

    array_text = match.group(1)
    try:
        todos_list = eval(array_text)   # safe here because input is controlled
    except Exception:
        todos_list = []

    return todos_list


def generate_angular_ts(todos_list):
    """
    Generates the Angular TypeScript component as a string.
    """
    todos_ts = ", ".join([f"'{t}'" for t in todos_list]) if todos_list else "'Learn React', 'Build a transpiler'"

    ts_code = f"""import {{ Component }} from '@angular/core';

@Component({{
  selector: 'app-todo-list',
  templateUrl: './TodoList.component.html',
  styleUrls: ['./TodoList.component.css']
}})
export class TodoListComponent {{
  todos: string[] = [{todos_ts}];
  newTodo: string = '';

  addTodo() {{
    if (this.newTodo.trim()) {{
      this.todos.push(this.newTodo);
      this.newTodo = '';
    }}
  }}
}}
"""
    return ts_code


def generate_angular_html():
    """
    Returns the Angular HTML template as a string.
    """
    html_code = """<div>
  <h1>Todo List</h1>
  <ul>
    <li *ngFor="let todo of todos">{{ todo }}</li>
  </ul>
  <input [(ngModel)]="newTodo" type="text" />
  <button (click)="addTodo()">Add Todo</button>
</div>
"""
    return html_code


def main():
    # Step 2: Extract initial todos list
    todos_list = extract_initial_todos(react_code)

    # Step 3 & 4: Generate Angular output
    angular_ts = generate_angular_ts(todos_list)
    angular_html = generate_angular_html()

    # Step 5: Write to output directory
    output_dir = Path("../generated")
    output_dir.mkdir(exist_ok=True)

    (output_dir / "TodoList.component.ts").write_text(angular_ts, encoding="utf-8")
    (output_dir / "TodoList.component.html").write_text(angular_html, encoding="utf-8")

    print("Angular files generated in 'generated/' folder.")


if __name__ == "__main__":
    main()
