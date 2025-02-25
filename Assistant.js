import React from "react";
import data from "./data";

function Assistant({ query }) {
  const matchedKey = Object.keys(data).find((key) =>
    key.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <div
      style={{
        width: "50%",
        padding: "20px",
        overflowY: "auto",
        backgroundColor: "#f4f4f4",
      }}
    >
      <h2>Assistant</h2>

      {matchedKey ? (
        <div
          style={{
            marginTop: "20px",
            padding: "20px",
            border: "1px solid #ccc",
            backgroundColor: "#fff",
          }}
        >
          <h3>{data[matchedKey].title}</h3>
          <p>{data[matchedKey].description}</p>

          {data[matchedKey].type === "text" && (
            <p>{data[matchedKey].content}</p>
          )}

          {data[matchedKey].type === "image" && (
            <img
              src={data[matchedKey].image}
              alt={data[matchedKey].title}
              style={{
                width: "100%",
                maxWidth: "400px",
                display: "block",
                margin: "10px auto",
              }}
            />
          )}

          {data[matchedKey].type === "video" && (
            <iframe
              width="100%"
              height="300"
              src={data[matchedKey].video}
              title={data[matchedKey].title}
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
              style={{ margin: "10px 0" }}
            ></iframe>
          )}

          {data[matchedKey].type === "table" && (
            <table
              border="1"
              style={{ width: "100%", textAlign: "left", marginTop: "10px" }}
            >
              <thead>
                <tr>
                  <th>Company</th>
                  <th>Price</th>
                  <th>Change</th>
                </tr>
              </thead>
              <tbody>
                {data[matchedKey].tableData.map((row, index) => (
                  <tr key={index}>
                    <td>{row.company}</td>
                    <td>{row.price}</td>
                    <td>{row.change}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}

          {data[matchedKey].type === "tabulated" && (
            <table
              border="1"
              style={{ width: "100%", textAlign: "left", marginTop: "10px" }}
            >
              <thead>
                <tr>
                  <th>Criteria</th>
                  <th>AI</th>
                  <th>Human</th>
                </tr>
              </thead>
              <tbody>
                {data[matchedKey].tabulatedData.map((row, index) => (
                  <tr key={index}>
                    <td>{row.criteria}</td>
                    <td>{row.AI}</td>
                    <td>{row.Human}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      ) : (
        <p>Enter a keyword on the left to search...</p>
      )}
    </div>
  );
}

export default Assistant;
