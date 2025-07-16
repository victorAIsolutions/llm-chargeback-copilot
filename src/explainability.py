import shap
import numpy as np

def explain_predictions(predictions, texts):
    """
    Generates SHAP explanations for predictions of text inputs.
    Falls back to empty explanations if SHAP explainer fails.
    """
    # Define a wrapper for model prediction probabilities
    def model_predict(texts_list):
        # Replace with your model's predict_proba if available
        # Here we return dummy probabilities for two classes
        return np.array([[0.1, 0.9] for _ in texts_list])

    explanations = []
    try:
        # Use universal SHAP explainer for text
        explainer = shap.Explainer(model_predict, shap.maskers.Text())
        # Compute explanations for all texts at once
        shap_explanations = explainer(texts)
        for exp in shap_explanations:
            # Store raw SHAP values
            explanations.append({"shap_values": exp.values.tolist()})
    except Exception:
        # If any error, return empty dicts for each input
        explanations = [{"shap_values": []} for _ in texts]

    return explanations