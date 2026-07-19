# 🧠 DecisionLens AI

Natural Language Processing (NLP) application for analysing personal decisions using Machine Learning and Large Language Models (LLMs).

The project classifies user arguments as **Supporting** or **Opposing** using a Logistic Regression model and generates a structured decision analysis powered by OpenRouter.

The project was developed following an end-to-end Machine Learning workflow, from data preparation to deployment with Streamlit and Docker.

---

# 🚀 Live Demo

**DecisionLens AI**

https://decisionslens-ai-abyhw7po64hcehxztbceph.streamlit.app/

---

# Project Overview

Every day people make important personal and professional decisions involving uncertainty.

DecisionLens AI provides a structured approach to decision making by combining a Machine Learning classifier with a Large Language Model.

The application predicts whether a user's argument supports or opposes a decision and then generates an AI-assisted analysis including advantages, disadvantages, risks and reflection questions.

The application is designed as a **decision-support tool**, not as a replacement for human judgement.

---

# Business Problem

Decision making is often influenced by emotions, incomplete information and cognitive bias.

A structured AI-assisted analysis can help users:

- Organise their thoughts
- Identify potential risks
- Consider alternative perspectives
- Improve decision quality
- Support more informed decision making

---

# Dataset

### Dataset

IBM Debater® - Argument Quality Ranking Dataset

Source:

https://www.kaggle.com/datasets/iranmostafid/ibm-argq-ranking

### Characteristics

- Public NLP dataset
- Thousands of labelled arguments
- Argument stance classification
- Natural language text
- Binary classification

Variables used:

- argument
- stance_WA

The dataset was divided into:

- Training set
- Validation set
- Test set

---

# Technologies

- Python
- Pandas
- Scikit-Learn
- TF-IDF
- Logistic Regression
- OpenRouter API
- Streamlit
- Docker
- Git
- GitHub

---

# Project Structure

```
decisionlens-ai/

│

├── app/
│   ├── app.py
│   ├── constants.py
│   ├── prompts.py
│   └── utils.py
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_model_development.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── images/
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Project Workflow

The project follows a simplified CRISP-DM methodology.

## 1. Data Exploration

- Dataset inspection
- Missing values analysis
- Duplicate analysis
- Class distribution
- Feature selection

## 2. Data Preprocessing

- Text cleaning
- Lowercase conversion
- Whitespace normalization
- Train / Validation / Test split

## 3. Model Development

The following models were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- Naive Bayes

TF-IDF Vectorization was used to transform the text into numerical features.

---

# Model Evaluation

The models were evaluated using:

- Accuracy
- Model comparison
- Validation performance
- Test performance

| Model | Test Accuracy |
|--------|--------------:|
| Logistic Regression | 68.0% |
| Decision Tree | — |
| Random Forest | ~69% |
| SVM | ~69% |

---

# Why was Logistic Regression selected?

Although Random Forest and SVM achieved slightly higher accuracy, the improvement was approximately **1%**.

Logistic Regression was selected because it provides:

- Simpler implementation
- Faster inference
- Lower computational cost
- Easier deployment
- Better explainability

making it the best trade-off for this application.

---

# Streamlit Application

The deployed application allows users to analyse a personal decision by entering a short description.

The application returns:

- Argument Classification
- Prediction Confidence
- AI-generated Decision Analysis

---

# Docker

### Build

```bash
docker build -t decisionlens-ai .
```

### Run

```bash
docker run -p 8501:8501 --env-file .env decisionlens-ai
```

---

# Installation

### Clone repository

```bash
git clone https://github.com/hmmazuera/decisionlens-ai.git
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create `.env`

```text
OPENROUTER_API_KEY=your_api_key
```

### Run Streamlit

```bash
python -m streamlit run app/app.py
```

---

# Results

The final application combines Machine Learning and Generative AI to provide users with a structured decision-support tool.

The project demonstrates an end-to-end NLP workflow including data preprocessing, feature engineering, model development, deployment and cloud hosting.

---

# Future Improvements

- Hyperparameter optimisation
- Fine-tuned Transformer models
- Explainability using SHAP
- FastAPI REST API
- User authentication
- CI/CD pipeline

---

# Author

**Mauricio Mazuera**

GitHub:

https://github.com/hmmazuera/decisionlens-ai

LinkedIn:

https://www.linkedin.com/in/mauricio-mazuera-a0a7a933b