import React, { useState } from "react";
import Assistant from "./Assistant";
import data from "./data";

const App = () => {
  const [query, setQuery] = useState("");
  const [matchedTopic, setMatchedTopic] = useState(null);

  const handleSearch = (event) => {
    const inputText = event.target.value.toLowerCase();
    setQuery(inputText);

    let foundTopic = null;

    // Iterate through topics to find keywords in input
    Object.keys(data).forEach((topic) => {
      if (
        inputText.includes(topic.toLowerCase()) ||
        data[topic].keyConcept
          .toLowerCase()
          .split(" ")
          .some((word) => inputText.includes(word))
      ) {
        foundTopic = topic;
      }
    });

    setMatchedTopic(foundTopic);
  };

  return (
    <div style={{ display: "flex" }}>
      {/* Left Side: Search Input */}
      <div style={{ width: "30%", padding: "20px", background: "#f4f4f4" }}>
        <h2>Search Topics</h2>
        <input
          type="text"
          placeholder="Enter a topic..."
          value={query}
          onChange={handleSearch}
          style={{ width: "100%", padding: "10px", marginBottom: "10px" }}
        />
      </div>

      {/* Right Side: Assistant */}
      <div style={{ width: "70%", padding: "20px" }}>
        <Assistant matchedTopic={matchedTopic} />
      </div>
    </div>
  );
};

export default App;
