# LLM Copilot for Chargeback Verification

This project is a proof of concept of an AI-powered copilot for verifying PDF‑based chargeback evidence, implemented with:

- **OpenAI GPT-4** + **LangChain** for prompt orchestration.  
- **Pinecone** for embedding storage and RAG architecture.  
- **PyPDF2** / **pdfplumber** for PDF parsing.  
- **SHAP** for explainability and audit trails.

---
## Features

- **PDF Parsing:** Extracts text from each page using pdfplumber.

- **Semantic Classification:** Generates embeddings with OpenAI and performs Retrieval-Augmented Generation (RAG) via Pinecone to classify evidence into predefined categories.

- **Explainability:** Uses SHAP to produce explanations for each classification, providing transparency and audit trails.

- **Modular Design:** Clear separation of code in src/, interactive exploration in notebooks/, and sample data in data/.

## Prerequisites

- Python 3.8 or newer

- An OpenAI account and API key

- A Pinecone account with an existing index (e.g. llm-evidence-index)

## Setup & Installation

1. Clone the repository

git clone https://github.com/<YOUR_USERNAME>/llm-chargeback-verification.git
cd llm-chargeback-verification

2. Create & activate a virtual environment

# Windows PowerShell
token python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install --upgrade pip
pip install -r requirements.txt

4. Configure environment variables

# OpenAI API key
export OPENAI_API_KEY="sk-..."

# Pinecone configuration
env: PINECONE_API_KEY="<your-pinecone-api-key>"
env: PINECONE_INDEX_NAME="llm-evidence-index"
env: PINECONE_ENV_REGION="us-east1-gcp"  # optional, defaults to this value

On Windows PowerShell:
$env:OPENAI_API_KEY = "sk-..."
$env:PINECONE_API_KEY = "<your-pinecone-api-key>"
$env:PINECONE_INDEX_NAME = "llm-evidence-index"
$env:PINECONE_ENV_REGION = "us-east1-gcp"

## Usage

Place a sample PDF in data/ (e.g. sample.pdf) or point to your own document, then run:

python src/main.py --input data/sample.pdf --output results.json

--input (-i): Path to the PDF file.

--output (-o): Path to write the JSON results.

After execution, results.json will contain an array of objects:

[
  {
    "text": "...",
    "prediction": "category_label",
    "explanation": {
      "shap_values": [ ... ]
    }
  },
  ...
]

## 📂 Project Structure

llm-chargeback-verification/
├── src/                          # Source code
│   ├── main.py                   # Entry point
│   ├── pdf_parser.py             # PDF text extraction
│   ├── semantic_classifier.py    # Embedding + Pinecone RAG
│   └── explainability.py         # SHAP explanations
├── notebooks/                    # Jupyter notebooks for exploration
│   └── exploration.ipynb
├── data/                         # Sample PDFs for testing
│   └── sample.pdf
├── results/                      # JSON outputs from runs
├── requirements.txt              # Python dependencies
├── .gitignore
└── README.md

## Customization & Next Steps

1. Populate Pinecone: Index real examples with metadata category to replace the unknown fallback.

2. Fine-tune prompts: Adjust LangChain templates or LLM parameters for higher accuracy.

3. Replace dummy model: Swap out the placeholder model_predict with your trained classifier for genuine SHAP insights.

4. Scale & Deploy: Containerize or orchestrate via CI/CD for production readiness.

## License

This project is released under the MIT License.