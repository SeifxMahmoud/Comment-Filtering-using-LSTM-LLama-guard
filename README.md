# 🛡️ Comment Filtering using LSTM and LLaMA Guard

This repository contains an end-to-end implementation of a hybrid comment moderation system. The pipeline combines traditional LSTM-based sequence modeling with transformer-based moderation using Meta's LLaMA Guard. It aims to classify and filter harmful or inappropriate content in text comments by leveraging both supervised training and prompt-based safety filtering.

---

## 🔍 Overview

The project explores:
- Using LSTM for supervised comment classification.
- Applying LLaMA Guard for post-generation filtering or safety validation.
- Tokenization strategies suited for transformer models.
- Efficient data loading via Hugging Face's `datasets` library, with support for streaming large datasets.

This work is a hands-on attempt to understand the challenges of integrating classical NLP architectures with modern LLM-based moderation tools.

---

## 📁 Directory Structure
├── data/ # Raw or preprocessed datasets
├── models/ # Checkpoints and saved models
├── notebooks/ # Jupyter notebooks for experimentation
├── src/ # Core Python scripts for training and inference
├── requirements.txt # Dependencies
└── README.md # Project documentation


---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Comment-Filtering-using-LSTM-LLama-guard.git
cd Comment-Filtering-using-LSTM-LLama-guard

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt

pip install --upgrade accelerate
