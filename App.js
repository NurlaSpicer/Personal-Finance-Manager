import React, { useState, useEffect } from 'react';

function App() {
  const [expenses, setExpenses] = useState([]);

  useEffect(() => {
    fetch('/expenses')
      .then(response => response.json())
      .then(data => setExpenses(data));
  }, []);

  return (
    <div>
      <h1>Personal Finance Manager</h1>
      <ul>
        {expenses.map(expense => (
          <li key={expense.id}>{expense.description}: ${expense.amount}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
