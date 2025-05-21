# advisor/knowledge/ai_analysis.py
from transformers import pipeline

# Create a text classification pipeline using a pre-trained model.
# (This is a simple example; in a real-world scenario, you might train your own model.)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def analyze_career_fit(text, candidate_labels=None):
    """
    Analyzes the free-text input (e.g., career goals or experiences) and
    returns scores for a list of candidate career labels.
    """
    if candidate_labels is None:
        candidate_labels = ["Software Developer", "Data Scientist", "UX Designer", 
                            "Cybersecurity Analyst", "Teacher","doctor"]

    result = classifier(text, candidate_labels)
    # Return the label with the highest score
    return result["labels"][0], result["scores"][0]
