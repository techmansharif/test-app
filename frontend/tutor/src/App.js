import React, { useState } from "react";
import "./App.css";

function App() {
  const [a, setA] = useState("");
  const [b, setB] = useState("");
  const [result, setResult] = useState(null);

  const handleAdd = async () => {
 
    const res = await fetch("https://fastapi-backend-208251878692.us-central1.run.app/add", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ a: Number(a), b: Number(b) }),
    });
  
    const data = await res.json();
 
    setResult(data.result);
  };

  return (
    <div className="App">
      <h1>Add Two Numbers</h1>
      <input
        type="number"
        placeholder="Enter first number"
        value={a}
        onChange={(e) => setA(e.target.value)}
      />
      <input
        type="number"
        placeholder="Enter second number"
        value={b}
        onChange={(e) => setB(e.target.value)}
      />
      <button onClick={handleAdd}>Add</button>
      {result !== null && <h2>Result: {result}</h2>}
    </div>
  );
}

export default App;
