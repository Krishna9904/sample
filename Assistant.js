import React from "react";
import data from "./data";

const Assistant = ({ matchedTopic }) => {
  if (!matchedTopic) {
    return <h2>Right side panel</h2>;
  }

  const topicData = data[matchedTopic];

  return (
    <div>
      <h2>{topicData.keyConcept}</h2>
      <ul>
        {topicData.bulletPoints.map((point, index) => (
          <li key={index}>{point}</li>
        ))}
      </ul>
      <p>{topicData.paragraph}</p>

      <h3>Useful Links:</h3>
      <ul>
        {topicData.links.map((link, index) => (
          <li key={index}>
            <a href={link} target="_blank" rel="noopener noreferrer">
              {link}
            </a>
          </li>
        ))}
      </ul>

      <h3>Table Information:</h3>
      <table border="1" style={{ borderCollapse: "collapse", width: "100%" }}>
        <thead>
          <tr>
            {topicData.table.headers.map((header, index) => (
              <th key={index} style={{ padding: "10px", background: "#ddd" }}>
                {header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {topicData.table.rows.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {row.map((cell, cellIndex) => (
                <td key={cellIndex} style={{ padding: "10px" }}>
                  {cell}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Assistant;
