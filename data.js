const data = {
  topic1: {
    keyConcept: "Introduction to Web Development",
    bulletPoints: [
      "Web development involves building and maintaining websites.",
      "It consists of frontend, backend, and full-stack development.",
      "Technologies include HTML, CSS, JavaScript, and frameworks like React.",
    ],
    paragraph:
      "Web development is the work involved in developing a website for the Internet. It ranges from simple static pages to complex web applications.",
    links: [
      "https://developer.mozilla.org/en-US/docs/Learn",
      "https://www.w3schools.com/",
      "https://react.dev/",
      "https://css-tricks.com/",
      "https://frontendmasters.com/",
      "https://javascript.info/",
    ],
    table: {
      headers: ["Technology", "Purpose"],
      rows: [
        ["HTML", "Structure of Web Page"],
        ["CSS", "Styling"],
        ["JavaScript", "Dynamic Content"],
        ["React", "Component-Based UI"],
      ],
    },
  },
  topic2: {
    keyConcept: "Machine Learning Basics",
    bulletPoints: [
      "Machine Learning enables computers to learn from data.",
      "Supervised, Unsupervised, and Reinforcement Learning are key types.",
      "Popular ML libraries include TensorFlow and Scikit-Learn.",
    ],
    paragraph:
      "Machine Learning (ML) is a field of AI that enables systems to learn and improve from experience without being explicitly programmed.",
    links: [
      "https://www.coursera.org/learn/machine-learning",
      "https://scikit-learn.org/",
      "https://www.tensorflow.org/",
    ],
    table: {
      headers: ["ML Type", "Description"],
      rows: [
        ["Supervised", "Labeled data used for training"],
        ["Unsupervised", "No labels, finds patterns"],
        ["Reinforcement", "Rewards-based learning"],
      ],
    },
  },
  topic3: {
    keyConcept: "Cloud Computing Overview",
    bulletPoints: [
      "Cloud computing delivers computing services over the internet.",
      "Key providers include AWS, Azure, and Google Cloud.",
      "Models include IaaS, PaaS, and SaaS.",
    ],
    paragraph:
      "Cloud computing allows on-demand access to computing resources with minimal management effort.",
    links: [
      "https://aws.amazon.com/",
      "https://azure.microsoft.com/",
      "https://cloud.google.com/",
    ],
    table: {
      headers: ["Cloud Model", "Example"],
      rows: [
        ["IaaS", "AWS EC2"],
        ["PaaS", "Google App Engine"],
        ["SaaS", "Google Docs"],
      ],
    },
  },
};

export default data;
