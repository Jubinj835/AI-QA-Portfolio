# AI QA Portfolio (`AI-QA-Portfolio`)

[![AI QA Evaluation Pipeline](https://github.com/Jubinj835/AI-QA-Portfolio/actions/workflows/ai_qa_tests.yml/badge.svg)](https://github.com/Jubinj835/AI-QA-Portfolio/actions/workflows/ai_qa_tests.yml)

A professional, local-first AI Quality Assurance and evaluation portfolio project built to test, evaluate, and validate Large Language Models (LLMs) locally without relying on external cloud APIs.

## 🛠️ Tech Stack
* **Language:** Python 3.12
* **Testing Framework:** `pytest`
* **Evaluation Framework:** `deepeval`
* **Local LLM Runtime:** `ollama` (`deepseek-r1:1.5b`)
* **CI/CD:** GitHub Actions (Push, PR, and Daily Cron triggers)

---

## 📂 Project Structure
```text
AI-QA-Portfolio/
│
├── .github/
│   └── workflows/
│       └── ai_qa_tests.yml
│
├── tests/
│   ├── lesson1_test.py
│   ├── lesson2_deepEval_test.py
│   ├── lesson3_faithfulness_test.py
│   └── lesson4_advanced_thresholds.py
│
├── run_evals.py
├── requirements.txt
├── .gitignore
└── README.md