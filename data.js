const data = {
  "Machine Learning": {
    title: "Introduction to Machine Learning",
    description:
      "Machine learning is a method of data analysis that automates analytical model building.",
    type: "text",
    content:
      "It is a branch of AI that allows systems to learn from data, identify patterns, and make decisions.",
  },
  Cybersecurity: {
    title: "Cybersecurity Measures",
    description:
      "Best practices to protect systems, networks, and programs from cyber attacks.",
    type: "image",
    image: "https://via.placeholder.com/300",
  },
  SpaceX: {
    title: "Latest SpaceX Mission",
    description: "Watch the latest SpaceX launch video.",
    type: "video",
    video: "https://www.youtube.com/embed/dQw4w9WgXcQ",
  },
  "Stock Market": {
    title: "Stock Market Trends",
    description: "A table showing recent stock market performance.",
    type: "table",
    tableData: [
      { company: "Apple", price: "$150", change: "+2.5%" },
      { company: "Tesla", price: "$700", change: "-1.2%" },
      { company: "Amazon", price: "$3300", change: "+0.8%" },
    ],
  },
  "AI vs. Humans": {
    title: "Comparison between AI and Humans",
    description: "A structured tabulated comparison.",
    type: "tabulated",
    tabulatedData: [
      { criteria: "Speed", AI: "Fast", Human: "Slow" },
      { criteria: "Creativity", AI: "Limited", Human: "High" },
      { criteria: "Consistency", AI: "High", Human: "Varies" },
    ],
  },
};

export default data;
