import React, { useState } from 'react';


function App() {
  const [todos, setTodos] = useState([]);
  const [todo, setTodo] = useState('');

  const handleInputChange = (e) => {
    setTodo(e.target.value);
  };

  const addTodo = () => {
    if (todo.trim() !== '') {
      setTodos([...todos, todo]);
      setTodo('');
    }
  };

  const deleteTodo = (index) => {
    const updatedTodos = todos.filter((_, i) => i !== index);
    setTodos(updatedTodos);
  };

  return (
    <div className="App">
      <h1>Todo List</h1>
      <div className="todo-form">
        <input
          type="text"
          value={todo}
          onChange={handleInputChange}
          placeholder="Enter your todo"
        />
        <button onClick={addTodo}>Add</button>
      </div>
      <ul>
        {todos.map((todo, index) => (
          <li key={index}>
            {todo}
            <button onClick={() => deleteTodo(index)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
