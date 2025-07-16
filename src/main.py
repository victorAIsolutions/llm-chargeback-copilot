import argparse
import json
from pdf_parser import extract_text
from semantic_classifier import classify_documents
from explainability import explain_predictions

def run_verification(input_path, output_path):
    """Run full verification pipeline: extract text, classify, and explain."""
    texts = extract_text(input_path)
    predictions = classify_documents(texts)
    explanations = explain_predictions(predictions, texts)
    results = [
        {"text": text, "prediction": pred, "explanation": expl}
        for text, pred, expl in zip(texts, predictions, explanations)
    ]
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="LLM Copilot for Chargeback Verification"
    )
    parser.add_argument(
        "--input", "-i", required=True, help="Path to input PDF file"
    )
    parser.add_argument(
        "--output", "-o", required=True, help="Path to output JSON file"
    )
    args = parser.parse_args()
    run_verification(args.input, args.output)