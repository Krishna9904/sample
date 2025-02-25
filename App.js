import React, { useState } from "react";
import Assistant from "./Assistant";

function App() {
  const [query, setQuery] = useState("");

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      {/* Left Panel - Search Input */}
      <div
        style={{
          width: "50%",
          padding: "20px",
          backgroundColor: "#e3e3e3",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <h2>Welcome to the Learning Hub!</h2>
        <input
          type="text"
          placeholder="Enter keyword..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{ padding: "10px", width: "80%", marginTop: "10px" }}
        />
      </div>

      {/* Right Panel - Assistant with Search Query */}
      <Assistant query={query} />
    </div>
  );
}

export default App;
