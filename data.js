const data = {
  topic1: {
    keyConcept: "Introduction to Web Development",
    bulletPoints: [
      "Web development involves building and maintaining websites.",
      "Frontend, backend, and full-stack development.",
      "Technologies: HTML, CSS, JavaScript, React.",
    ],
    paragraph:
      "Web development is creating websites, from simple static pages to dynamic applications.",
    links: ["https://developer.mozilla.org/", "https://react.dev/"],
    table: {
      headers: ["Technology", "Purpose"],
      rows: [
        ["HTML", "Structure of Web Page"],
        ["CSS", "Styling"],
        ["JavaScript", "Dynamic Content"],
      ],
    },
  },
  topic2: {
    keyConcept: "Machine Learning Basics",
    bulletPoints: [
      "ML enables computers to learn from data.",
      "Supervised, Unsupervised, Reinforcement Learning.",
      "Popular ML libraries: TensorFlow, Scikit-Learn.",
    ],
    paragraph:
      "Machine Learning is an AI field enabling systems to improve without explicit programming.",
    links: ["https://scikit-learn.org/", "https://www.tensorflow.org/"],
    table: {
      headers: ["ML Type", "Description"],
      rows: [
        ["Supervised", "Labeled data used for training"],
        ["Unsupervised", "No labels, finds patterns"],
      ],
    },
  },
};

export default data;
