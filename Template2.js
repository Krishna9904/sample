import React from "react";

const Template2 = ({ topicData }) => {
  return (
    <div className="template-container">
      <h3>{topicData.keyConcept}</h3>

      {/* Table First */}
      <table>
        <thead>
          <tr>
            {topicData.table.headers.map((header, index) => (
              <th key={index}>{header}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {topicData.table.rows.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {row.map((cell, cellIndex) => (
                <td key={cellIndex}>{cell}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>

      {/* Sections */}
      <p>{topicData.paragraph}</p>
      {topicData.bulletPoints.map((point, index) => (
        <p key={index}>➤ {point}</p>
      ))}

      {/* Links */}
      <h4>Learn More:</h4>
      <ul>
        {topicData.links.map((link, index) => (
          <li key={index}>
            <a href={link} target="_blank" rel="noopener noreferrer">
              {link}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Template2;
