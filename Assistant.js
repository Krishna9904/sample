import React from "react";
import data from "./data";
import Template1 from "./Templste1";
import Template2 from "./Template2";
import "./Assistant.css";

const Assistant = ({ matchedTopic }) => {
  const topicData = data[matchedTopic];

  if (!topicData) {
    return <div className="assistant-container">No data available.</div>;
  }

  return (
    <div className="assistant-container">
      <h2 className="topic-name">{matchedTopic.toUpperCase()}</h2>

      {/* Use Template1 for Topic1 and Template2 for Topic2 */}
      {matchedTopic === "topic1" ? (
        <Template1 topicData={topicData} />
      ) : (
        <Template2 topicData={topicData} />
      )}
    </div>
  );
};

export default Assistant;
