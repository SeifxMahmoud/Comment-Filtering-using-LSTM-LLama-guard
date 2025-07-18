# Comment-Filtering-using-LSTM-LLama-guard

---

## 🚀 Features & Highlights

- ✅ Streaming large datasets using `datasets.load_dataset(streaming=True)`
- ✅ Prompt engineering for multi-column concatenation
- ✅ Integration with Hugging Face `AutoTokenizer` and model-specific tokenization
- ✅ LSTM model with TensorFlow/Keras
- ✅ Safety filtering using LLaMA Guard
- ✅ Padding/truncation configuration for uniform sequence lengths
- ✅ Label mapping (`label2id`) for classification targets

---

## 🔧 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/yourusername/Comment-Filtering-using-LSTM-LLama-guard.git
cd Comment-Filtering-using-LSTM-LLama-guard

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
