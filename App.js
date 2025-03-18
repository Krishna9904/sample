import React, { useState } from "react";
import Assistant from "./Assistant";
import data from "./data";
import "./App.css";

const App = () => {
  const [query, setQuery] = useState("");
  const [matchedTopic, setMatchedTopic] = useState("topic1"); // Default to topic1
  const [isRightPanelOpen, setIsRightPanelOpen] = useState(false);

  const handleSearch = () => {
    if (!query.trim()) return;

    let foundTopic = "topic1"; // Default topic
    Object.keys(data).forEach((topic) => {
      if (
        query.toLowerCase().includes(topic.toLowerCase()) ||
        data[topic].keyConcept
          .toLowerCase()
          .split(" ")
          .some((word) => query.toLowerCase().includes(word))
      ) {
        foundTopic = topic;
      }
    });

    setMatchedTopic(foundTopic);
    setIsRightPanelOpen(true); // Show right panel on search
  };

  const handleClose = () => {
    setIsRightPanelOpen(false); // Hide right panel
  };

  return (
    <div className="app-container">
      {/* Left Panel */}
      <div className={`left-panel ${isRightPanelOpen ? "" : "full-width"}`}>
        <h2>Search Topics</h2>
        <input
          type="text"
          placeholder="Enter a topic..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="search-input"
        />
        <button onClick={handleSearch} className="search-button">
          Search
        </button>
      </div>

      {/* Right Panel */}
      {isRightPanelOpen && (
        <div className="right-panel">
          <button onClick={handleClose} className="close-button">
            ✖
          </button>
          <Assistant matchedTopic={matchedTopic} />
        </div>
      )}
    </div>
  );
};

export default App;
